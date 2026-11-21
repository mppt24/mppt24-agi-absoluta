import ast
import operator
import os
import secrets
import re
import sqlite3
import random
import string
import math
from datetime import datetime
from pathlib import Path
from subprocess import DEVNULL, SubprocessError, run
from tempfile import TemporaryDirectory
from flask import Flask, Response, jsonify, render_template, request

from knowledge import normalizar, responder_topico
import hashlib
import threading
import base64


def calcular_expressao(expressao):
    """Avalia apenas operações e funções matemáticas suportadas."""
    if len(expressao) > 256:
        raise ValueError("Expressão demasiado longa.")

    operacoes = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }
    funcoes = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log10,
        "ln": math.log,
    }
    constantes = {"pi": math.pi, "e": math.e}

    def avaliar(no):
        if isinstance(no, ast.Constant) and type(no.value) in (int, float):
            valor = no.value
        elif isinstance(no, ast.Name) and no.id in constantes:
            valor = constantes[no.id]
        elif isinstance(no, ast.UnaryOp) and isinstance(no.op, (ast.UAdd, ast.USub)):
            operando = avaliar(no.operand)
            valor = -operando if isinstance(no.op, ast.USub) else operando
        elif isinstance(no, ast.BinOp) and type(no.op) in operacoes:
            esquerda, direita = avaliar(no.left), avaliar(no.right)
            if isinstance(no.op, ast.Pow) and abs(direita) > 100:
                raise ValueError("Expoente fora dos limites.")
            valor = operacoes[type(no.op)](esquerda, direita)
        elif (
            isinstance(no, ast.Call)
            and isinstance(no.func, ast.Name)
            and no.func.id in funcoes
            and len(no.args) == 1
            and not no.keywords
        ):
            valor = funcoes[no.func.id](avaliar(no.args[0]))
        else:
            raise ValueError("Expressão não suportada.")

        if type(valor) not in (int, float) or not -1e100 <= valor <= 1e100:
            raise ValueError("Resultado fora dos limites.")
        return valor

    texto = expressao.replace("×", "*").replace("x", "*").replace("÷", "/").replace("^", "**")
    return avaliar(ast.parse(texto.strip(), mode="eval").body)


def converter_unidades(pedido):
    formato = re.fullmatch(r"([+-]?\d+(?:[.,]\d+)?)\s+(.+)", pedido.strip())
    if not formato:
        return "🔄 Indica um valor e duas unidades. Exemplo: converter 1 metro em cm."

    valor = float(formato[1].replace(",", "."))
    unidades = tuple(
        unidade for unidade in normalizar(formato[2]).split()
        if unidade not in {"em", "para"}
    )
    conversoes = {
        ("metro", "cm"): (100, "centímetros"),
        ("km", "metros"): (1000, "metros"),
        ("kg", "gramas"): (1000, "gramas"),
        ("litro", "ml"): (1000, "mililitros"),
        ("hora", "minutos"): (60, "minutos"),
        ("dia", "horas"): (24, "horas"),
    }
    if unidades == ("celsius", "fahrenheit"):
        resultado, destino = valor * 9 / 5 + 32, "graus Fahrenheit"
    elif unidades == ("fahrenheit", "celsius"):
        resultado, destino = (valor - 32) * 5 / 9, "graus Celsius"
    elif unidades in conversoes:
        fator, destino = conversoes[unidades]
        resultado = valor * fator
    else:
        return "🔄 Conversão não suportada. Experimenta 1 km em metros ou 0 Celsius Fahrenheit."

    if not math.isfinite(resultado):
        return "🔄 O valor está fora dos limites."
    return f"🔄 Conversão: {resultado:g} {destino}"


# Funcionalidades extras seguras
class ExtraFeatures:
    """Funcionalidades extras que não interferem com o conhecimento existente"""
    
    @staticmethod
    def gerar_qr_code_texto(texto):
        """Gera representação ASCII simples de QR code"""
        try:
            # Simulação simples de QR code em ASCII
            hash_obj = hashlib.md5(texto.encode())
            hash_hex = hash_obj.hexdigest()
            
            qr_pattern = []
            for i in range(0, len(hash_hex), 4):
                chunk = hash_hex[i:i+4]
                row = ""
                for char in chunk:
                    if int(char, 16) % 2 == 0:
                        row += "██"
                    else:
                        row += "  "
                qr_pattern.append(row)
            
            qr_ascii = "\n".join(qr_pattern)
            return f"📱 Padrão ASCII ilustrativo para '{texto}':\n```\n{qr_ascii}\n```"
        except Exception as e:
            return f"❌ Erro ao gerar QR code: {str(e)}"
    
    @staticmethod
    def codificar_base64(texto):
        """Codifica texto em Base64"""
        try:
            encoded = base64.b64encode(texto.encode('utf-8')).decode('utf-8')
            return f"🔐 Base64: {encoded}"
        except Exception as e:
            return f"❌ Erro ao codificar: {str(e)}"
    
    @staticmethod
    def decodificar_base64(texto_codificado):
        """Decodifica texto de Base64"""
        try:
            decoded = base64.b64decode(texto_codificado).decode('utf-8')
            return f"🔓 Decodificado: {decoded}"
        except Exception as e:
            return f"❌ Erro ao decodificar: {str(e)}"
    
    @staticmethod
    def gerar_hash(texto, algoritmo="sha256"):
        """Gera hash do texto com algoritmo especificado"""
        try:
            if algoritmo.lower() == "md5":
                hash_obj = hashlib.md5(texto.encode())
            elif algoritmo.lower() == "sha1":
                hash_obj = hashlib.sha1(texto.encode())
            elif algoritmo.lower() == "sha256":
                hash_obj = hashlib.sha256(texto.encode())
            else:
                return f"❌ Algoritmo '{algoritmo}' não suportado. Use: md5, sha1, sha256"
            
            return f"🔐 Hash {algoritmo.upper()}: {hash_obj.hexdigest()}"
        except Exception as e:
            return f"❌ Erro ao gerar hash: {str(e)}"
    
    @staticmethod
    def contador_palavras(texto):
        """Conta palavras, caracteres e linhas do texto"""
        try:
            palavras = len(texto.split())
            caracteres = len(texto)
            caracteres_sem_espacos = len(texto.replace(' ', ''))
            linhas = len(texto.split('\n'))
            
            return f"📊 Estatísticas do texto:\n• Palavras: {palavras}\n• Caracteres: {caracteres}\n• Caracteres (sem espaços): {caracteres_sem_espacos}\n• Linhas: {linhas}"
        except Exception as e:
            return f"❌ Erro ao contar: {str(e)}"
    
    @staticmethod
    def gerar_lorem_ipsum(num_palavras=50):
        """Gera texto Lorem Ipsum"""
        lorem_words = [
            "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
            "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
            "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud",
            "exercitation", "ullamco", "laboris", "nisi", "aliquip", "ex", "ea", "commodo",
            "consequat", "duis", "aute", "irure", "in", "reprehenderit", "voluptate",
            "velit", "esse", "cillum", "fugiat", "nulla", "pariatur", "excepteur", "sint",
            "occaecat", "cupidatat", "non", "proident", "sunt", "culpa", "qui", "officia",
            "deserunt", "mollit", "anim", "id", "est", "laborum"
        ]
        
        try:
            num_palavras = min(max(int(num_palavras), 1), 200)  # Limite entre 1 e 200
            texto = []
            
            for i in range(num_palavras):
                palavra = random.choice(lorem_words)
                if i == 0:
                    palavra = palavra.capitalize()
                texto.append(palavra)
                
                # Adicionar pontuação ocasionalmente
                if (i + 1) % random.randint(8, 15) == 0 and i < num_palavras - 1:
                    texto[-1] += random.choice(['.', ',', ';'])
                    if texto[-1].endswith('.'):
                        # Próxima palavra com maiúscula
                        continue
            
            # Garantir que termina com ponto
            if not texto[-1].endswith(('.', '!', '?')):
                texto[-1] += '.'
            
            return f"📝 Lorem Ipsum ({num_palavras} palavras):\n{' '.join(texto)}"
        except Exception as e:
            return f"❌ Erro ao gerar Lorem Ipsum: {str(e)}"
    
    @staticmethod
    def validar_email(email):
        """Valida formato de email"""
        try:
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(pattern, email):
                return f"✅ Email '{email}' é válido"
            else:
                return f"❌ Email '{email}' é inválido"
        except Exception as e:
            return f"❌ Erro ao validar email: {str(e)}"
    
    @staticmethod
    def gerar_cores_hex():
        """Gera cores hexadecimais aleatórias"""
        try:
            cores = []
            for i in range(5):
                cor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                cores.append(cor)
            
            return f"🎨 Cores hexadecimais aleatórias:\n" + "\n".join([f"• {cor}" for cor in cores])
        except Exception as e:
            return f"❌ Erro ao gerar cores: {str(e)}"
    
    @staticmethod
    def calcular_imc(peso, altura):
        """Calcula Índice de Massa Corporal"""
        try:
            peso = float(peso)
            altura = float(altura)
            
            if altura <= 0 or peso <= 0:
                return "❌ Peso e altura devem ser valores positivos"
            
            # Se altura parece estar em cm, converter para metros
            if altura > 3:
                altura = altura / 100
            
            imc = peso / (altura ** 2)
            
            if imc < 18.5:
                categoria = "Abaixo do peso"
            elif imc < 25:
                categoria = "Peso normal"
            elif imc < 30:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidade"
            
            return f"⚖️ IMC: {imc:.1f} - {categoria}\n(Peso: {peso}kg, Altura: {altura:.2f}m)"
        except ValueError:
            return "❌ Peso e altura devem ser números válidos"
        except Exception as e:
            return f"❌ Erro ao calcular IMC: {str(e)}"

# Instância global das funcionalidades extras
extra_features = ExtraFeatures()

class MPPT24_Absoluta:
    def __init__(self):
        self.setup_database()
        
    def setup_database(self):
        """Base de dados local para conversas"""
        self.lock = threading.Lock()
        self.conn = sqlite3.connect(
            os.environ.get("MPPT24_DB_PATH", "mppt24_absoluta.db"),
            check_same_thread=False,
        )
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversas (
                id INTEGER PRIMARY KEY,
                pergunta TEXT,
                resposta TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def salvar_conversa(self, pergunta, resposta):
        """Salva conversa na base de dados"""
        with self.lock, self.conn:
            self.conn.execute(
                "INSERT INTO conversas (pergunta, resposta) VALUES (?, ?)",
                (pergunta, resposta),
            )
    
    def responder(self, mensagem):
        """Processa um comando ou procura uma resposta local."""
        texto_original = mensagem.strip()
        mensagem = texto_original.lower()
        
        # FUNCIONALIDADES EXTRAS SEGURAS (verificar primeiro para não interferir)
        pedido_qr = re.match(r"^qr(?: code)?\s+(.+)$", texto_original, flags=re.IGNORECASE)
        if pedido_qr:
            return extra_features.gerar_qr_code_texto(pedido_qr.group(1))
        
        if mensagem.startswith("codificar "):
            texto = texto_original[10:]
            return extra_features.codificar_base64(texto)
        
        if mensagem.startswith("decodificar "):
            texto = texto_original[12:]
            return extra_features.decodificar_base64(texto)
        
        if mensagem.startswith("hash "):
            partes = texto_original[5:].split()
            if len(partes) >= 2:
                algoritmo = partes[0]
                texto = " ".join(partes[1:])
                return extra_features.gerar_hash(texto, algoritmo)
            else:
                texto = " ".join(partes)
                return extra_features.gerar_hash(texto)
        
        if "contar palavras" in mensagem or "estatisticas texto" in mensagem:
            # Extrair texto após o comando
            texto = mensagem.replace("contar palavras", "").replace("estatisticas texto", "").strip()
            if texto:
                return extra_features.contador_palavras(texto)
            else:
                return "📊 Use: 'contar palavras [seu texto aqui]'"
        
        if "lorem ipsum" in mensagem:
            # Extrair número de palavras se especificado
            match = re.search(r'(\d+)', mensagem)
            num_palavras = int(match.group(1)) if match else 50
            return extra_features.gerar_lorem_ipsum(num_palavras)
        
        if "validar email" in mensagem:
            email = mensagem.replace("validar email", "").strip()
            if email:
                return extra_features.validar_email(email)
            else:
                return "📧 Use: 'validar email exemplo@email.com'"
        
        if "gerar cores" in mensagem or "cores hex" in mensagem:
            return extra_features.gerar_cores_hex()
        
        if "calcular imc" in mensagem or "imc" in mensagem:
            # Extrair peso e altura
            numeros = re.findall(r'\d+(?:\.\d+)?', mensagem)
            if len(numeros) >= 2:
                peso = numeros[0]
                altura = numeros[1]
                return extra_features.calcular_imc(peso, altura)
            else:
                return "⚖️ Use: 'calcular imc [peso] [altura]' (ex: calcular imc 70 1.75)"
        
        # CONVERSAÇÃO NATURAL (mantida intacta)
        respostas_simples = {
            "ola": "Olá! Como estás?", "oi": "Oi! Tudo bem?", "olá": "Olá! Como estás?",
            "tudo bem": "Tudo bem! E tu?", "como estas": "Estou bem, obrigado! E tu?",
            "ola tudo bem": "Olá! Tudo bem, e contigo?", "obrigado": "Obrigado pela conversa!",
            "bom dia": "Bom dia! Como amanheceste?", "boa tarde": "Boa tarde! Como vai o dia?",
            "tchau": "Tchau! Até logo!", "adeus": "Adeus! Cuida-te!",
        }
        
        saudacao = normalizar(mensagem)
        if saudacao in respostas_simples:
            resposta = respostas_simples[saudacao]
            self.salvar_conversa(mensagem, resposta)
            return resposta
        
        # FUNCIONALIDADES AVANÇADAS
        
        # CALCULADORA CIENTÍFICA AVANÇADA
        if mensagem.startswith("calcular ") or mensagem.startswith("calcula "):
            expressao = mensagem.split(maxsplit=1)[1]
            try:
                resultado = calcular_expressao(expressao)
                resposta = f"🧮 Resultado: {resultado}"
                self.salvar_conversa(mensagem, resposta)
                return resposta
            except (ArithmeticError, SyntaxError, ValueError):
                resposta = "🧮 Erro no cálculo. Tenta algo como: calcular 2+2, sqrt(16), sin(pi/2)"
                self.salvar_conversa(mensagem, resposta)
                return resposta
        
        # TRADUTOR MULTI-IDIOMAS
        if mensagem.startswith("traduzir ") or mensagem.startswith("traduz "):
            texto_traduzir = mensagem.replace("traduzir ", "").replace("traduz ", "")
            
            # Traduções básicas português-inglês-espanhol
            traducoes = {
                "olá": "🌐 Tradução: Hello (EN), Hola (ES), Bonjour (FR), Ciao (IT)",
                "obrigado": "🌐 Tradução: Thank you (EN), Gracias (ES), Merci (FR), Grazie (IT)",
                "amor": "🌐 Tradução: Love (EN), Amor (ES), Amour (FR), Amore (IT)",
                "água": "🌐 Tradução: Water (EN), Agua (ES), Eau (FR), Acqua (IT)",
                "casa": "🌐 Tradução: House (EN), Casa (ES), Maison (FR), Casa (IT)",
                "carro": "🌐 Tradução: Car (EN), Coche (ES), Voiture (FR), Auto (IT)",
                "comida": "🌐 Tradução: Food (EN), Comida (ES), Nourriture (FR), Cibo (IT)",
                "família": "🌐 Tradução: Family (EN), Familia (ES), Famille (FR), Famiglia (IT)",
                "trabalho": "🌐 Tradução: Work (EN), Trabajo (ES), Travail (FR), Lavoro (IT)",
                "escola": "🌐 Tradução: School (EN), Escuela (ES), École (FR), Scuola (IT)",
            }
            
            if texto_traduzir in traducoes:
                resposta = traducoes[texto_traduzir]
            else:
                resposta = "🌐 Tradução: Palavra não encontrada. Tenta: olá, obrigado, amor, água, casa"
            
            self.salvar_conversa(mensagem, resposta)
            return resposta
        
        if mensagem.startswith(("converter ", "converte ")):
            resposta = converter_unidades(mensagem.split(maxsplit=1)[1])
            self.salvar_conversa(texto_original, resposta)
            return resposta

        if mensagem in {"gerar senha", "criar senha", "gerar palavra-passe", "criar palavra-passe"}:
            caracteres = string.ascii_letters + string.digits + "!@#$%&*"
            senha = "".join(secrets.choice(caracteres) for _ in range(12))
            return f"🔐 Senha gerada: {senha}"

        # INFORMAÇÕES DO SISTEMA
        if "que horas" in mensagem or "hora atual" in mensagem:
            agora = datetime.now()
            resposta = f"🕐 Hora atual: {agora.strftime('%H:%M:%S de %d/%m/%Y')}"
            self.salvar_conversa(mensagem, resposta)
            return resposta
        
        if "data hoje" in mensagem or "que dia" in mensagem:
            hoje = datetime.now()
            dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
            dia_semana = dias_semana[hoje.weekday()]
            resposta = f"📅 Hoje é {dia_semana}, {hoje.strftime('%d/%m/%Y')}"
            self.salvar_conversa(mensagem, resposta)
            return resposta
        
        # MATEMÁTICA AVANÇADA
        if "derivada" in mensagem and ("x²+5x+3" in mensagem or "x2+5x+3" in mensagem):
            resposta = "🧮 Matemática: A derivada de x²+5x+3 é 2x+5"
            self.salvar_conversa(mensagem, resposta)
            return resposta
        
        if mensagem.startswith(("gpt4 ", "blockchain ")):
            return "Essa integração está em avaliação."

        resposta = responder_topico(mensagem)
        if resposta is None:
            resposta = "Ainda não tenho uma resposta para esse tema. Tenta uma palavra-chave ou um dos exemplos."
        self.salvar_conversa(texto_original, resposta)
        return resposta

# Aplicação Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16_384
mppt24 = MPPT24_Absoluta()

@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/voz")
def voz():
    data = request.get_json(silent=True)
    text = data.get("text") if isinstance(data, dict) else None
    if not isinstance(text, str) or not text.strip() or len(text) > 4000:
        return jsonify(error="Envia entre 1 e 4000 caracteres para ler."), 400

    try:
        with TemporaryDirectory() as directory:
            audio = Path(directory) / "resposta.wav"
            run(
                ["espeak-ng", "-v", "pt", "-b", "1", "-w", str(audio), "--stdin"],
                input=text.encode("utf-8", errors="replace"),
                stdout=DEVNULL,
                stderr=DEVNULL,
                check=True,
                timeout=8,
            )
            content = audio.read_bytes()
    except (OSError, SubprocessError):
        return jsonify(error="A voz local do AGI está indisponível."), 503

    return Response(content, mimetype="audio/wav", headers={"Cache-Control": "no-store"})


GESTOS_LGP = {
    "ola": ("Olá!", "Ol%C3%A1"),
    "bom dia": ("Bom dia!", "bom%20dia"),
    "adeus": ("Adeus!", "adeus"),
    "obrigado": ("Obrigado!", "obrigado"),
    "desculpa": ("Desculpa!", "desculpa"),
    "sim": ("Sim.", "SIM"),
}
CUMPRIMENTOS_LGP = {"ola", "bom dia", "adeus"}
PEDIDO_GESTO = "mostra o gesto de "


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get('message'), str):
        return jsonify({'error': 'Envia uma mensagem de texto em JSON.'}), 400
    if len(data['message']) > 2000:
        return jsonify({'error': 'A mensagem pode ter até 2000 caracteres.'}), 400
    message = data["message"]
    normalized = normalizar(message)
    lookup = normalized.startswith(PEDIDO_GESTO)
    wants_sign = data.get("lgp") is True or lookup
    if wants_sign:
        term = normalized.removeprefix(PEDIDO_GESTO)
        gesture = GESTOS_LGP.get(term) if lookup or term in CUMPRIMENTOS_LGP else None
        if gesture:
            response, entry = gesture
            mppt24.salvar_conversa(message, response)
            return jsonify(response=response, lgp={
                "source": "Infopédia",
                "url": "https://www.infopedia.pt/dicionarios/lingua-gestual/" + entry,
            })

    result = {"response": processar_mensagem(message)}
    if wants_sign:
        result["lgp"] = None
    return jsonify(result)


def processar_mensagem(mensagem):
    return mppt24.responder(mensagem)


if __name__ == '__main__':
    app.run(
        host=os.environ.get("MPPT24_HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5013")),
        debug=False,
    )

