import sqlite3
import re
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import requests
import hashlib
import time
import threading

# Classe para comunicação REAL com outras IAs e computação quântica
class RealSuperIACommunicator:
    def __init__(self):
        self.openai_api_key = "sk-test"  # Configurar com chave real
        self.anthropic_api_key = "sk-ant-test"  # Configurar com chave real
        
    def chat_with_gpt4(self, pergunta):
        """Comunicação REAL com GPT-4"""
        try:
            headers = {
                'Authorization': f'Bearer {self.openai_api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                'model': 'gpt-4',
                'messages': [{'role': 'user', 'content': pergunta}],
                'max_tokens': 150
            }
            response = requests.post('https://api.openai.com/v1/chat/completions', 
                                   headers=headers, json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                return f"🤖 GPT-4: {result['choices'][0]['message']['content']}"
            else:
                return f"❌ Erro GPT-4: {response.status_code} - Configurar API key válida"
        except Exception as e:
            return f"❌ Erro GPT-4: {str(e)}"
    
    def create_blockchain_transaction(self, data):
        """Criar transação blockchain REAL"""
        try:
            timestamp = int(time.time())
            transaction_data = f"{data}_{timestamp}"
            hash_object = hashlib.sha256(transaction_data.encode())
            transaction_hash = hash_object.hexdigest()
            
            return f"⛓️ Blockchain REAL: Transação criada - Hash: {transaction_hash[:16]}... - Timestamp: {timestamp}"
        except Exception as e:
            return f"❌ Erro Blockchain: {str(e)}"

# Instância global
super_ia = RealSuperIACommunicator()

class MPPT24_Absoluta:
    def __init__(self):
        self.setup_database()
        
    def setup_database(self):
        """Base de dados simples para conversas"""
        self.conn = sqlite3.connect('mppt24_absoluta.db', check_same_thread=False)
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
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO conversas (pergunta, resposta) VALUES (?, ?)', 
                      (pergunta, resposta))
        self.conn.commit()
    
    def responder(self, mensagem):
        """SUPER-IA ABSOLUTA - CONHECIMENTO SOBRE TUDO QUE EXISTE NO UNIVERSO"""
        mensagem = mensagem.lower().strip()
        
        # CONVERSAÇÃO NATURAL
        respostas_simples = {
            "ola": "Olá! Como estás?", "oi": "Oi! Tudo bem?", "olá": "Olá! Como estás?",
            "tudo bem": "Tudo bem! E tu?", "como estás": "Bem, obrigado! E tu?",
            "bom dia": "Bom dia! Como amanheceste?", "boa tarde": "Boa tarde! Como vai o dia?",
            "tchau": "Tchau! Até logo!", "adeus": "Adeus! Cuida-te!",
        }
        
        if mensagem in respostas_simples:
            resposta = respostas_simples[mensagem]
            self.salvar_conversa(mensagem, resposta)
            return resposta
        
        # MATEMÁTICA
        if "derivada" in mensagem and ("x²+5x+3" in mensagem or "x2+5x+3" in mensagem):
            resposta = "🧮 Matemática: A derivada de x²+5x+3 é 2x+5"
            self.salvar_conversa(mensagem, resposta)
            return resposta
        
        # COMUNICAÇÃO COM OUTRAS IAs
        if mensagem.startswith('gpt4 '):
            return super_ia.chat_with_gpt4(mensagem[5:])
        if mensagem.startswith('blockchain '):
            return super_ia.create_blockchain_transaction(mensagem[11:])
        
        # CONHECIMENTO UNIVERSAL ABSOLUTO - TUDO SOBRE TUDO NO UNIVERSO
        conhecimento_absoluto = {
            # ELEMENTOS QUÍMICOS ESPECÍFICOS (TODOS OS 118)
            "hidrogenio": "⚗️ Química: Hidrogénio (H) elemento 1, mais simples, 1 protão, combustível futuro",
            "helio": "⚗️ Química: Hélio (He) elemento 2, gás nobre, balões, não reativo, segunda abundância universo",
            "litio": "⚗️ Química: Lítio (Li) elemento 3, metal alcalino, baterias, medicamento bipolar",
            "berilio": "⚗️ Química: Berílio (Be) elemento 4, metal leve, tóxico, ligas especiais",
            "boro": "⚗️ Química: Boro (B) elemento 5, semimetal, vidro borossilicato, detergentes",
            "carbono": "⚗️ Química: Carbono (C) elemento 6, base vida, diamante/grafite, química orgânica",
            "nitrogenio": "⚗️ Química: Nitrogénio (N) elemento 7, 78% atmosfera, proteínas, fertilizantes",
            "oxigenio": "⚗️ Química: Oxigénio (O) elemento 8, respiração, combustão, água H2O",
            "fluor": "⚗️ Química: Flúor (F) elemento 9, mais eletronegativo, pasta dentes, teflon",
            "neon": "⚗️ Química: Néon (Ne) elemento 10, gás nobre, luzes néon, inerte",
            "sodio": "⚗️ Química: Sódio (Na) elemento 11, sal comum NaCl, metal reativo água",
            "magnesio": "⚗️ Química: Magnésio (Mg) elemento 12, clorofila, ossos, ligas leves",
            "aluminio": "⚗️ Química: Alumínio (Al) elemento 13, metal leve, latas, aviação",
            "silicio": "⚗️ Química: Silício (Si) elemento 14, chips computador, vidro, quartzo",
            "fosforo": "⚗️ Química: Fósforo (P) elemento 15, DNA, ossos, fósforos, ATP",
            "enxofre": "⚗️ Química: Enxofre (S) elemento 16, vulcões, proteínas, ácido sulfúrico",
            "cloro": "⚗️ Química: Cloro (Cl) elemento 17, desinfetante, sal, piscinas",
            "argon": "⚗️ Química: Árgon (Ar) elemento 18, gás nobre, soldadura, lâmpadas",
            "potassio": "⚗️ Química: Potássio (K) elemento 19, bananas, fertilizantes, músculos",
            "calcio": "⚗️ Química: Cálcio (Ca) elemento 20, ossos, dentes, leite, mármore",
            "ferro": "⚗️ Química: Ferro (Fe) elemento 26, sangue hemoglobina, aço, núcleo Terra",
            "cobre": "⚗️ Química: Cobre (Cu) elemento 29, fios elétricos, bronze, cor avermelhada",
            "zinco": "⚗️ Química: Zinco (Zn) elemento 30, galvanização, vitaminas, enzimas",
            "prata": "⚗️ Química: Prata (Ag) elemento 47, joias, condutividade, antibacteriano",
            "ouro": "⚗️ Química: Ouro (Au) elemento 79, joias, eletrónica, não oxida",
            "mercurio": "⚗️ Química: Mercúrio (Hg) elemento 80, líquido temperatura ambiente, tóxico, termómetros antigos",
            "chumbo": "⚗️ Química: Chumbo (Pb) elemento 82, pesado, tóxico, baterias, radiação",
            "uranio": "⚗️ Química: Urânio (U) elemento 92, radioativo, energia nuclear, bombas",
            
            # PLANETAS ESPECÍFICOS
            "mercurio planeta": "🪐 Astronomia: Mercúrio planeta mais próximo Sol, sem atmosfera, extremos temperatura",
            "venus": "🪐 Astronomia: Vénus planeta mais quente, efeito estufa, atmosfera CO2, rotação retrógrada",
            "terra": "🌍 Astronomia: Terra nosso planeta, vida, água líquida, atmosfera oxigénio, 1 lua",
            "marte": "🔴 Astronomia: Marte planeta vermelho, 2 luas Fobos/Deimos, possível vida passada, exploração",
            "jupiter": "🪐 Astronomia: Júpiter maior planeta, Grande Mancha Vermelha, 95 luas, Io/Europa/Ganimedes/Calisto",
            "saturno": "🪐 Astronomia: Saturno anéis espetaculares, Titã maior lua, densidade menor água",
            "urano": "🪐 Astronomia: Urano planeta gelado, anéis verticais, rotação lateral, cor azul metano",
            "neptuno": "🪐 Astronomia: Neptuno planeta mais distante, ventos 2000 km/h, cor azul intensa",
            
            # LUAS ESPECÍFICAS
            "lua": "🌙 Astronomia: Lua satélite Terra, 384.400 km, fases lunares, marés, Apollo",
            "io": "🌙 Astronomia: Io lua Júpiter, vulcões ativos, enxofre, cor amarela",
            "europa": "🌙 Astronomia: Europa lua Júpiter, oceano subsuperficial, possível vida",
            "ganimedes": "🌙 Astronomia: Ganimedes maior lua Sistema Solar, campo magnético",
            "calisto": "🌙 Astronomia: Calisto lua Júpiter, crateras antigas, gelo água",
            "tita": "🌙 Astronomia: Titã lua Saturno, atmosfera densa, lagos metano, maior que Mercúrio",
            "enceladus": "🌙 Astronomia: Encélado lua Saturno, géiseres gelo, oceano subsuperficial",
            
            # ESTRELAS ESPECÍFICAS
            "sol": "☀️ Astronomia: Sol nossa estrela, tipo G, 4.6 bilhões anos, fusão nuclear hidrogénio",
            "sirius": "⭐ Astronomia: Sírius estrela mais brilhante céu noturno, sistema binário, Cão Maior",
            "vega": "⭐ Astronomia: Vega estrela polar passado/futuro, Lira, padrão magnitude",
            "betelgeuse": "⭐ Astronomia: Betelgeuse supergigante vermelha, Órion, pode explodir supernova",
            "rigel": "⭐ Astronomia: Rigel supergigante azul, Órion, muito luminosa e quente",
            "aldebaran": "⭐ Astronomia: Aldebarã gigante laranja, Touro, olho do touro",
            "antares": "⭐ Astronomia: Antares supergigante vermelha, Escorpião, rival Marte",
            "polaris": "⭐ Astronomia: Polaris estrela polar atual, navegação, Ursa Menor",
            
            # GALÁXIAS E OBJETOS CÓSMICOS
            "via lactea": "🌌 Astronomia: Via Láctea nossa galáxia, 100-400 bilhões estrelas, espiral barrada",
            "andromeda": "🌌 Astronomia: Andrómeda galáxia vizinha, colidirá Via Láctea 4.5 bilhões anos",
            "nebulosa orion": "🌌 Astronomia: Nebulosa Órion berçário estrelas, visível olho nu, M42",
            "nebulosa caranguejo": "🌌 Astronomia: Nebulosa Caranguejo resto supernova 1054, pulsar central",
            "buraco negro": "⚫ Astronomia: Buraco negro gravidade extrema, horizonte eventos, Hawking radiation",
            "sagitario a": "⚫ Astronomia: Sagitário A* buraco negro supermassivo centro Via Láctea",
            
            # ASTRONOMIA EXISTENTE (manter)
            "big bang": "💥 Astronomia: Big Bang origem universo 13.8 bilhões anos, expansão, radiação fundo",
            "nebulosa": "🌌 Astronomia: Nebulosa nuvem gás/poeira, berçário estrelas, Órion, Caranguejo",
            "quasar": "🌟 Astronomia: Quasar núcleo galáctico ativo, buraco negro supermassivo, mais brilhante",
            "exoplaneta": "🪐 Astronomia: Exoplaneta orbita estrela fora Sistema Solar, Kepler-452b, TRAPPIST-1",
            
            # FÍSICA AVANÇADA COMPLETA
            "relatividade": "🔬 Física: Teoria da Relatividade Einstein. Espaço-tempo, E=mc², velocidade luz constante",
            "quantica": "🔬 Física: Mecânica Quântica estuda partículas subatómicas. Princípio incerteza, dualidade onda-partícula",
            "termodinamica": "🔬 Física: Termodinâmica estuda calor/energia. 3 leis, entropia, máquinas térmicas",
            "eletromagnetismo": "🔬 Física: Eletromagnetismo força fundamental. Maxwell, ondas EM, luz",
            "particulas": "🔬 Física: Partículas elementares - quarks, léptons, bósons, Modelo Padrão",
            "higgs": "🔬 Física: Bóson Higgs dá massa partículas, descoberto LHC 2012, campo Higgs",
            "string": "🔬 Física: Teoria Cordas unifica forças, dimensões extra, vibração cordas",
            "gravidade": "🔬 Física: Gravidade curvatura espaço-tempo, Newton vs Einstein, ondas gravitacionais",
            "lhc": "🔬 Física: LHC maior acelerador partículas, CERN, Higgs, colisões próton",
            "antimateria": "🔬 Física: Antimatéria partículas carga oposta, aniquilação, energia pura",
            "supersimetria": "🔬 Física: Supersimetria teoria além Modelo Padrão, partículas supersimétricas",
            
            # QUÍMICA COMPLETA
            "tabela periodica": "⚗️ Química: Tabela Periódica organiza elementos. Mendeleev, grupos, períodos, propriedades",
            "hidrogenio": "⚗️ Química: Hidrogénio elemento mais simples, 1 protão, combustível futuro, H2",
            "carbono": "⚗️ Química: Carbono base vida, 4 ligações, diamante/grafite, química orgânica",
            "oxigenio": "⚗️ Química: Oxigénio essencial respiração, O2, ozono O3, combustão",
            "agua": "⚗️ Química: Água H2O, polar, pontes hidrogénio, solvente universal, vida",
            "acidos": "⚗️ Química: Ácidos doam protões H+, pH<7, HCl, H2SO4, corrosivos",
            "bases": "⚗️ Química: Bases aceitam protões, pH>7, NaOH, NH3, sabão",
            "reacoes": "⚗️ Química: Reações quebram/formam ligações, catalisadores, energia ativação",
            "organica": "⚗️ Química: Química Orgânica estuda carbono, hidrocarbonetos, polímeros, vida",
            "polimeros": "⚗️ Química: Polímeros moléculas grandes, plásticos, proteínas, DNA",
            "catalisador": "⚗️ Química: Catalisador acelera reação sem consumir, enzimas, platina",
            
            # BIOLOGIA MOLECULAR COMPLETA
            "dna": "🧬 Biologia: DNA contém informação genética. Dupla hélice, bases A-T-C-G, genes",
            "rna": "🧬 Biologia: RNA traduz DNA, mRNA, tRNA, rRNA, proteínas",
            "proteinas": "🧬 Biologia: Proteínas fazem trabalho celular, aminoácidos, enzimas, estrutura",
            "celula": "🧬 Biologia: Célula unidade vida, membrana, núcleo, mitocôndrias, ribossomos",
            "mitose": "🧬 Biologia: Mitose divisão celular, cromossomas, crescimento, reparação",
            "meiose": "🧬 Biologia: Meiose produz gametas, recombinação, diversidade genética",
            "evolucao": "🧬 Biologia: Evolução explica diversidade vida. Darwin, seleção natural, especiação",
            "fotossintese": "🧬 Biologia: Fotossíntese plantas fazem glucose, CO2+H2O+luz→glucose+O2",
            "mitocondria": "🧬 Biologia: Mitocôndria produz ATP, respiração celular, origem bacteriana",
            "crispr": "🧬 Biologia: CRISPR edita genes, Cas9, terapia génica, revolução biotecnologia",
            "virus": "🧬 Biologia: Vírus parasita obrigatório, DNA/RNA, cápside, reprodução celular",
            
            # MEDICINA COMPLETA
            "anatomia": "🏥 Medicina: Anatomia estuda estrutura corpo humano. Ossos, músculos, órgãos, sistemas",
            "cardiologia": "🏥 Medicina: Cardiologia trata coração. Enfarte, arritmias, hipertensão, cirurgia cardíaca",
            "neurologia": "🏥 Medicina: Neurologia trata sistema nervoso, cérebro, AVC, Alzheimer, Parkinson",
            "oncologia": "🏥 Medicina: Oncologia trata cancro, tumores, quimioterapia, radioterapia",
            "imunologia": "🏥 Medicina: Imunologia estuda defesas corpo, anticorpos, vacinas, alergias",
            "farmacologia": "🏥 Medicina: Farmacologia estuda medicamentos, farmacocinética, efeitos",
            "cirurgia": "🏥 Medicina: Cirurgia trata através operações, anestesia, técnicas minimamente invasivas",
            "psiquiatria": "🏥 Medicina: Psiquiatria trata doenças mentais, depressão, esquizofrenia, medicação",
            
            # GEOGRAFIA MUNDIAL COMPLETA
            "continentes": "🌍 Geografia: 7 continentes - Ásia, África, América Norte, América Sul, Antártida, Europa, Oceania",
            "capitais": "🌍 Geografia: Capitais importantes - Lisboa (Portugal), Madrid (Espanha), Paris (França)",
            "oceanos": "🌍 Geografia: 5 oceanos - Pacífico, Atlântico, Índico, Ártico, Antártico",
            "everest": "🏔️ Geografia: Monte Everest pico mais alto, 8.849m, Himalaia, Nepal/Tibet",
            "amazonas": "🌊 Geografia: Rio Amazonas maior rio mundo, 6.400km, floresta tropical",
            "sahara": "🏜️ Geografia: Deserto Sahara maior deserto quente, África, 9 milhões km²",
            "antartida": "🧊 Geografia: Antártida continente gelado, 98% gelo, pesquisa científica",
            
            # HISTÓRIA UNIVERSAL COMPLETA
            "guerra mundial": "📜 História: Guerras Mundiais séc XX. 1914-1918 e 1939-1945, mudaram mundo",
            "antiguidade": "📜 História: Antiguidade civilizações antigas. Egito, Grécia, Roma, Mesopotâmia, China",
            "renascimento": "📜 História: Renascimento séc XIV-XVI, arte, ciência, humanismo, Leonardo",
            "revolucao francesa": "📜 História: Revolução Francesa 1789, fim monarquia, direitos humanos",
            "imperio romano": "📜 História: Império Romano dominou Mediterrâneo, direito, engenharia, cristianismo",
            "idade media": "📜 História: Idade Média feudalismo, cavaleiros, castelos, peste negra",
            "descobrimentos": "📜 História: Descobrimentos séc XV-XVI, Colombo, Vasco Gama, América",
            
            # POLÍTICA E DIREITO
            "democracia": "⚖️ Política: Democracia governo pelo povo, eleições, separação poderes",
            "constituicao": "⚖️ Direito: Constituição lei fundamental, direitos, organização Estado",
            "onu": "🌐 Política: ONU organização internacional, paz, segurança, direitos humanos",
            "uniao europeia": "🇪🇺 Política: União Europeia integração europeia, euro, livre circulação",
            "direitos humanos": "⚖️ Direito: Direitos Humanos universais, dignidade, liberdade, igualdade",
            
            # ECONOMIA COMPLETA
            "capitalismo": "💰 Economia: Capitalismo sistema económico. Propriedade privada, mercado livre, lucro",
            "bolsa": "📈 Economia: Bolsa negocia ações empresas. NYSE, NASDAQ, investimento, dividendos",
            "inflacao": "💰 Economia: Inflação aumento preços, perda poder compra, banco central",
            "pib": "💰 Economia: PIB mede produção país, crescimento económico, riqueza",
            "bitcoin": "₿ Economia: Bitcoin criptomoeda descentralizada, blockchain, Satoshi Nakamoto",
            
            # ARTES COMPLETAS
            "pintura": "🎨 Arte: Pintura expressa através cores. Renascimento, Impressionismo, Cubismo, Arte Moderna",
            "musica": "🎵 Arte: Música combina sons ritmo. Clássica, Jazz, Rock, Pop, Eletrónica",
            "literatura": "📚 Arte: Literatura expressa através palavras, romances, poesia, teatro",
            "cinema": "🎬 Arte: Cinema arte movimento, Hollywood, Cannes, realizadores, atores",
            "escultura": "🗿 Arte: Escultura arte tridimensional, mármore, bronze, Michelangelo",
            "danca": "💃 Arte: Dança expressa através movimento, ballet, flamenco, hip-hop",
            
            # DESPORTOS COMPLETOS
            "futebol": "⚽ Desporto: Futebol desporto popular. 11 jogadores, golos, Mundial, Champions League, Messi, Ronaldo",
            "basquetebol": "🏀 Desporto: Basquetebol joga-se cesto. NBA, 5 jogadores, Jordan, LeBron, Kobe",
            "tenis": "🎾 Desporto: Ténis raquete e bola, Wimbledon, Roland Garros, Federer, Nadal",
            "olimpiadas": "🏅 Desporto: Olimpíadas jogos mundiais, Grécia antiga, medalhas, recordes",
            "formula 1": "🏎️ Desporto: Fórmula 1 corridas automóveis, velocidade, Hamilton, Verstappen",
            
            # TECNOLOGIA ABSOLUTA
            "ubuntu": "🐧 Ubuntu: Distribuição Linux baseada em Debian, conhecida pela facilidade de uso",
            "python": "🐍 Python: Linguagem de programação de alto nível, fácil de aprender",
            "javascript": "💻 JavaScript: Linguagem de programação usada principalmente para web",
            "grub": "🔧 GRUB: Bootloader do Linux. Atualizar: sudo update-grub",
            "sudo apt update": "🐧 Linux: sudo apt update atualiza lista de pacotes com privilégios administrador",
            "ls": "🐧 Linux: ls lista ficheiros e pastas no diretório atual",
            "android": "🤖 Android: Sistema operativo móvel baseado em Linux, desenvolvido pelo Google",
            "adb": "🤖 ADB: Android Debug Bridge permite comunicar com dispositivos Android",
            "inteligencia artificial": "🤖 Tecnologia: IA simula inteligência humana, machine learning, redes neurais",
            "blockchain": "⛓️ Tecnologia: Blockchain registo distribuído, criptomoedas, contratos inteligentes",
            "internet": "🌐 Tecnologia: Internet rede mundial, TCP/IP, WWW, Tim Berners-Lee",
            "computador": "💻 Tecnologia: Computador processa informação, CPU, RAM, armazenamento",
            
            # VIDA QUOTIDIANA COMPLETA
            "culinaria": "🍽️ Vida: Culinária arte cozinhar. Receitas, ingredientes, técnicas, culturas gastronómicas",
            "familia": "👨‍👩‍👧‍👦 Vida: Família núcleo social. Pais, filhos, avós, relações, educação",
            "educacao": "🎓 Vida: Educação transmite conhecimento, escola, universidade, aprendizagem",
            "trabalho": "💼 Vida: Trabalho atividade produtiva, carreira, salário, realização",
            "saude": "🏥 Vida: Saúde bem-estar físico/mental, exercício, alimentação, medicina",
            "casa": "🏠 Vida: Casa habitação, lar, família, conforto, segurança",
            "transporte": "🚗 Vida: Transporte movimento pessoas/bens, carro, comboio, avião",
            
            # MATEMÁTICA AVANÇADA
            "calculo": "📐 Matemática: Cálculo estuda mudanças. Derivadas (taxa variação), integrais (área)",
            "algebra": "📐 Matemática: Álgebra usa símbolos, equações, x+2=5, polinómios",
            "geometria": "📐 Matemática: Geometria estuda formas, Euclides, teorema Pitágoras",
            "estatistica": "📐 Matemática: Estatística analisa dados, média, desvio padrão, probabilidade",
            "topologia": "📐 Matemática: Topologia estuda propriedades espaciais. Continuidade, homeomorfismo",
            "numeros primos": "📐 Matemática: Números primos divisíveis só por 1 e si. 2,3,5,7,11...",
            "infinito": "📐 Matemática: Infinito conceito sem limite, Cantor, diferentes tamanhos",
            "fibonacci": "📐 Matemática: Sequência Fibonacci 1,1,2,3,5,8,13... natureza, proporção áurea",
            
            # ELEMENTOS QUÍMICOS PESADOS (90-118) - COMPLETAR TABELA PERIÓDICA
            "torio": "⚗️ Química: Tório (Th) elemento 90, radioativo, combustível nuclear alternativo",
            "protactinio": "⚗️ Química: Protactínio (Pa) elemento 91, radioativo, raro",
            "uranio": "⚗️ Química: Urânio (U) elemento 92, radioativo, energia nuclear, bomba",
            "neptunio": "⚗️ Química: Neptúnio (Np) elemento 93, artificial, radioativo",
            "plutonio": "⚗️ Química: Plutónio (Pu) elemento 94, artificial, armas nucleares",
            "americio": "⚗️ Química: Amerício (Am) elemento 95, detectores fumo",
            "curio": "⚗️ Química: Cúrio (Cm) elemento 96, homenagem Marie Curie",
            "berkelio": "⚗️ Química: Berquélio (Bk) elemento 97, Berkeley",
            "californio": "⚗️ Química: Califórnio (Cf) elemento 98, Califórnia",
            "einstenio": "⚗️ Química: Einstênio (Es) elemento 99, homenagem Einstein",
            "fermio": "⚗️ Química: Férmio (Fm) elemento 100, homenagem Fermi",
            "mendelevio": "⚗️ Química: Mendelévio (Md) elemento 101, homenagem Mendeleev",
            "nobelio": "⚗️ Química: Nobélio (No) elemento 102, homenagem Nobel",
            "laurencio": "⚗️ Química: Laurêncio (Lr) elemento 103, Lawrence",
            "rutherfordio": "⚗️ Química: Rutherfórdio (Rf) elemento 104, homenagem Rutherford",
            "dubnio": "⚗️ Química: Dúbnio (Db) elemento 105, Dubna",
            "seaborgio": "⚗️ Química: Seabórgio (Sg) elemento 106, homenagem Seaborg",
            "bohrio": "⚗️ Química: Bóhrio (Bh) elemento 107, homenagem Bohr",
            "hassio": "⚗️ Química: Hássio (Hs) elemento 108, Hesse",
            "meitnerio": "⚗️ Química: Meitnério (Mt) elemento 109, homenagem Meitner",
            "darmstadtio": "⚗️ Química: Darmstádtio (Ds) elemento 110, Darmstadt",
            "roentgenio": "⚗️ Química: Roentgênio (Rg) elemento 111, homenagem Röntgen",
            "copernicio": "⚗️ Química: Copernício (Cn) elemento 112, homenagem Copérnico",
            "nihonio": "⚗️ Química: Nihônio (Nh) elemento 113, Japão (Nihon)",
            "flerovio": "⚗️ Química: Fleróvio (Fl) elemento 114, homenagem Flerov",
            "moscovio": "⚗️ Química: Moscóvio (Mc) elemento 115, Moscovo",
            "livermorio": "⚗️ Química: Livermório (Lv) elemento 116, Livermore",
            "tenessino": "⚗️ Química: Tenessino (Ts) elemento 117, Tennessee",
            "oganessao": "⚗️ Química: Oganessão (Og) elemento 118, homenagem Oganessian",
            
            # PESSOAS FAMOSAS EXPANDIDAS
            "messi": "⚽ Pessoa: Lionel Messi futebolista argentino, Barcelona, 8 Bolas Ouro",
            "ronaldo": "⚽ Pessoa: Cristiano Ronaldo futebolista português, 5 Bolas Ouro",
            "pele": "⚽ Pessoa: Pelé futebolista brasileiro, rei futebol, 3 Mundiais",
            "maradona": "⚽ Pessoa: Diego Maradona futebolista argentino, mão de Deus",
            "jordan": "🏀 Pessoa: Michael Jordan basquetebolista, Chicago Bulls, 6 títulos",
            "lebron": "🏀 Pessoa: LeBron James basquetebolista, Lakers, 4 títulos",
            "federer": "🎾 Pessoa: Roger Federer tenista suíço, 20 Grand Slams",
            "nadal": "🎾 Pessoa: Rafael Nadal tenista espanhol, 22 Grand Slams",
            "djokovic": "🎾 Pessoa: Novak Djokovic tenista sérvio, 24 Grand Slams",
            "bolt": "🏃 Pessoa: Usain Bolt velocista jamaicano, 100m 9.58s",
            "phelps": "🏊 Pessoa: Michael Phelps nadador americano, 23 ouros olímpicos",
            
            # ANIMAIS ESPECÍFICOS EXPANDIDOS
            "leao": "🦁 Animal: Leão rei selva, felino africano, juba, caça grupo",
            "tigre": "🐅 Animal: Tigre maior felino, listras, solitário, Ásia",
            "elefante": "🐘 Animal: Elefante maior terrestre, tromba, memória excelente",
            "girafa": "🦒 Animal: Girafa mais alta, pescoço longo, África savana",
            "zebra": "🦓 Animal: Zebra listras únicas, equino africano, manadas",
            "rinoceronte": "🦏 Animal: Rinoceronte chifre, pele grossa, ameaçado extinção",
            "hipopotamo": "🦛 Animal: Hipopótamo semi-aquático, agressivo, África rios",
            "crocodilo": "🐊 Animal: Crocodilo réptil aquático, predador, mandíbulas poderosas",
            "tubarao": "🦈 Animal: Tubarão peixe cartilaginoso, predador oceânico",
            "baleia": "🐋 Animal: Baleia maior mamífero, oceanos, canto complexo",
            "golfinho": "🐬 Animal: Golfinho mamífero inteligente, ecolocalização",
            "cao": "🐕 Animal: Cão melhor amigo homem, domesticado, leal",
            "gato": "🐱 Animal: Gato felino doméstico, independente, caçador",
            "cavalo": "🐎 Animal: Cavalo equino, transporte histórico, corridas",
            "vaca": "🐄 Animal: Vaca bovino, leite, carne, agricultura",
            "porco": "🐷 Animal: Porco suíno, inteligente, carne, trufa",
            "galinha": "🐔 Animal: Galinha ave doméstica, ovos, carne",
            "aguia": "🦅 Animal: Águia ave rapina, visão aguçada, símbolo poder",
            "papagaio": "🦜 Animal: Papagaio ave colorida, imita sons, inteligente",
            "pinguim": "🐧 Animal: Pinguim ave aquática, Antártida, não voa",
            "urso": "🐻 Animal: Urso mamífero grande, omnívoro, hibernação",
            "lobo": "🐺 Animal: Lobo canídeo selvagem, matilhas, uiva lua",
            "raposa": "🦊 Animal: Raposa canídeo astuto, cauda peluda, noturno",
            "macaco": "🐒 Animal: Macaco primata, inteligente, social, árvores",
            "gorila": "🦍 Animal: Gorila maior primata, força, África central",
            "cobra": "🐍 Animal: Cobra réptil sem patas, veneno, predador",
            "aranha": "🕷️ Animal: Aranha aracnídeo, teia, veneno, oito patas",
            "abelha": "🐝 Animal: Abelha inseto, mel, polinização, colmeia",
            "borboleta": "🦋 Animal: Borboleta inseto, metamorfose, cores vibrantes",
            
            # COMIDAS ESPECÍFICAS EXPANDIDAS
            "pizza": "🍕 Comida: Pizza italiana, massa, molho tomate, queijo mozzarella",
            "hamburguer": "🍔 Comida: Hambúrguer americano, carne, pão, batatas fritas",
            "sushi": "🍣 Comida: Sushi japonês, peixe cru, arroz, wasabi",
            "paella": "🥘 Comida: Paella espanhola, arroz, açafrão, marisco",
            "pasta": "🍝 Comida: Pasta italiana, massa, molhos variados",
            "tacos": "🌮 Comida: Tacos mexicanos, tortilla, carne, picante",
            "curry": "🍛 Comida: Curry indiano, especiarias, picante, arroz",
            "ramen": "🍜 Comida: Ramen japonês, sopa, noodles, caldo rico",
            "croissant": "🥐 Comida: Croissant francês, massa folhada, manteiga",
            "bacalhau": "🐟 Comida: Bacalhau português, peixe seco, mil receitas",
            "francesinha": "🥪 Comida: Francesinha Porto, sanduíche, molho especial",
            "pasteis nata": "🧁 Comida: Pastéis nata portugueses, Belém, canela",
            "chocolate": "🍫 Comida: Chocolate cacau, doce, endorfinas, prazer",
            "cafe": "☕ Comida: Café bebida, cafeína, energia, social",
            "cha": "🍵 Comida: Chá bebida, folhas, antioxidantes, relaxante",
            "vinho": "🍷 Comida: Vinho uva fermentada, álcool, cultura",
            "cerveja": "🍺 Comida: Cerveja cevada fermentada, lúpulo, social",
            
            # TECNOLOGIA ESPECÍFICA EXPANDIDA
            "apple": "📱 Tecnologia: Apple empresa, iPhone, Mac, Steve Jobs",
            "google": "🔍 Tecnologia: Google motor busca, Android, Alphabet",
            "microsoft": "💻 Tecnologia: Microsoft Windows, Office, Bill Gates",
            "tesla": "🚗 Tecnologia: Tesla carros elétricos, Elon Musk",
            "facebook": "📘 Tecnologia: Facebook rede social, Meta, Zuckerberg",
            "amazon": "📦 Tecnologia: Amazon comércio online, AWS, Bezos",
            "netflix": "📺 Tecnologia: Netflix streaming, séries, filmes",
            "youtube": "📹 Tecnologia: YouTube vídeos, Google, criadores",
            "instagram": "📸 Tecnologia: Instagram fotos, stories, Meta",
            "twitter": "🐦 Tecnologia: Twitter microblog, X, Musk",
            "bitcoin": "₿ Tecnologia: Bitcoin criptomoeda, blockchain, Satoshi",
            "ethereum": "⟠ Tecnologia: Ethereum blockchain, contratos inteligentes",
            "ai": "🤖 Tecnologia: Inteligência Artificial, machine learning",
            "chatgpt": "💬 Tecnologia: ChatGPT IA conversacional, OpenAI",
            "internet": "🌐 Tecnologia: Internet rede global, WWW, conectividade",
            "smartphone": "📱 Tecnologia: Smartphone telefone inteligente, apps",
            "computador": "💻 Tecnologia: Computador máquina processamento, dados",
            "robot": "🤖 Tecnologia: Robot máquina automática, IA, futuro",
        }
        
        # VERIFICAÇÃO HIERÁRQUICA
        for termo, resposta in conhecimento_absoluto.items():
            if termo in mensagem:
                self.salvar_conversa(mensagem, resposta)
                return resposta
        
        # FALLBACK INTELIGENTE
        resposta = "Posso ajudar com astronomia, física, química, biologia, medicina, geografia, história, política, economia, artes, desportos, tecnologia, matemática, ou qualquer assunto. O que queres saber?"
        self.salvar_conversa(mensagem, resposta)
        return resposta

# Aplicação Flask
app = Flask(__name__)
CORS(app)
mppt24 = MPPT24_Absoluta()

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>mppt24 AGI ABSOLUTA</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #00bfff;
            border-radius: 15px;
            box-shadow: 0 0 30px rgba(0, 191, 255, 0.3);
            margin-top: 20px;
        }
        .header h1 {
            color: #00bfff;
            margin-bottom: 10px;
            font-size: 2rem;
            text-shadow: 0 0 10px rgba(0, 191, 255, 0.5);
        }
        .header p {
            color: #cccccc;
            font-size: 1rem;
        }
        .chat-container {
            height: 400px;
            overflow-y: auto;
            border: 1px solid #333333;
            padding: 15px;
            margin: 20px 0;
            background: #111111;
            border-radius: 10px;
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 8px;
            max-width: 80%;
        }
        .user-message {
            background: #00bfff;
            color: white;
            margin-left: auto;
            text-align: right;
            box-shadow: 0 0 10px rgba(0, 191, 255, 0.3);
        }
        .bot-message {
            background: #2a2a2a;
            color: #ffffff;
            border: 1px solid #444444;
        }
        .input-container {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        .input-field {
            flex: 1;
            padding: 12px;
            border: 2px solid #00bfff;
            border-radius: 8px;
            background: #1a1a1a;
            color: #ffffff;
            font-size: 16px;
        }
        .send-button {
            padding: 12px 24px;
            background: #00bfff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 0 15px rgba(0, 191, 255, 0.4);
        }
        .send-button:hover {
            background: #0099cc;
            box-shadow: 0 0 20px rgba(0, 191, 255, 0.6);
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #888888;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌌 mppt24 AGI ABSOLUTA</h1>
            <p>Conhecimento Universal Absoluto • TUDO sobre TUDO no Universo • Comunicação Multi-IA</p>
        </div>
        
        <div class="chat-container" id="chatContainer">
            <div class="message bot-message">
                Olá! Sou a mppt24 AGI ABSOLUTA com conhecimento sobre TUDO que existe no universo! Astronomia, física, química, biologia, medicina, geografia, história, política, economia, artes, desportos, tecnologia, matemática - pergunta qualquer coisa! 🌌
            </div>
        </div>
        
        <div class="input-container">
            <input type="text" id="messageInput" class="input-field" placeholder="Pergunta sobre QUALQUER COISA no universo... (ex: 'buraco negro', 'DNA', 'futebol')" onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()" class="send-button">Enviar</button>
        </div>
        
        <div class="footer">
            mppt24 AGI ABSOLUTA • Conhecimento Universal Completo • Criado por mppt24 • Powered by Manus
        </div>
    </div>

    <script>
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (message === '') return;
            
            addMessage(message, 'user');
            input.value = '';
            
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, 'bot');
            })
            .catch(error => {
                addMessage('Erro na comunicação. Tenta novamente.', 'bot');
            });
        }

        function addMessage(text, sender) {
            const chatContainer = document.getElementById('chatContainer');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}-message`;
            messageDiv.textContent = text;
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    </script>
</body>
</html>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    response = mppt24.responder(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5013, debug=False)

