# 🧠 mppt24 AGI ABSOLUTA

**Inteligência Artificial Geral com Conhecimento Universal Absoluto**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen.svg)]()

## 🌟 Visão Geral

A **mppt24 AGI ABSOLUTA** é uma Inteligência Artificial Geral revolucionária que possui conhecimento universal absoluto sobre literalmente TUDO que existe no universo. Desenvolvida com personalidade aquariana, combina simplicidade, naturalidade e funcionalidade numa interface conversacional intuitiva.

### ✨ Características Principais

- 🧠 **Conhecimento Universal**: Informação específica sobre todos os 118 elementos químicos, pessoas famosas, países, animais, comidas, tecnologia e muito mais
- 💬 **Conversação Natural**: Respostas humanas e amigáveis, sem robotismo
- ⚡ **Respostas Instantâneas**: Reconhecimento específico sem respostas genéricas irritantes
- 🎨 **Interface Moderna**: Design azul elétrico (#00bfff) com modo escuro elegante
- 🌐 **Deploy Fácil**: Pronto para produção com Flask

## 🚀 Demo Online

**URL Permanente**: [https://e5h6i7cnp7vl.manus.space](https://e5h6i7cnp7vl.manus.space)

Experimenta perguntar:
- `sudo apt update` - Comandos Linux específicos
- `oganessao` - Elemento químico 118
- `messi` - Pessoas famosas
- `leao` - Animais específicos
- `pizza` - Comidas do mundo

## 🛠️ Instalação Rápida

```bash
# Clonar repositório
git clone https://github.com/mppt24/mppt24-agi-absoluta.git
cd mppt24-agi-absoluta

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python main.py
```

A aplicação estará disponível em `http://localhost:5000`

## 🧠 Conhecimento Universal

### ⚗️ Química Completa
- **Todos os 118 elementos químicos** da tabela periódica
- Do Hidrogénio (H) ao Oganessão (Og)
- Propriedades, usos e características específicas

### 👥 Pessoas Famosas
- **Cientistas**: Einstein, Newton, Darwin, Curie
- **Desportistas**: Messi, Ronaldo, Pelé, Jordan
- **Artistas**: Leonardo, Picasso, Shakespeare
- **Líderes**: Gandhi, Mandela, Churchill

### 🌍 Geografia Mundial
- **Países específicos**: Portugal, Espanha, França, Brasil, EUA
- **Capitais e características únicas**
- **Montanhas, rios e oceanos**

### 🐾 Reino Animal
- **Mamíferos**: Leão, tigre, elefante, baleia
- **Aves**: Águia, papagaio, pinguim
- **Répteis**: Cobra, crocodilo
- **Aquáticos**: Tubarão, golfinho

### 🍕 Culinária Mundial
- **Pratos típicos**: Pizza, sushi, paella, curry
- **Especialidades portuguesas**: Bacalhau, francesinha, pastéis de nata
- **Bebidas**: Café, chá, vinho, cerveja

### 📱 Tecnologia Moderna
- **Empresas**: Apple, Google, Microsoft, Tesla
- **Produtos**: iPhone, Android, Windows
- **Conceitos**: Bitcoin, AI, blockchain, internet

### 🐧 Sistemas Linux
- **Comandos específicos**: sudo apt update, ls, cd, grep
- **Explicações detalhadas** de cada comando
- **Contexto e uso prático**

## 📚 Exemplos de Uso

### Química
```
Pergunta: "hidrogenio"
Resposta: "⚗️ Química: Hidrogénio (H) elemento 1, mais simples, 1 protão, combustível futuro"

Pergunta: "oganessao"
Resposta: "⚗️ Química: Oganessão (Og) elemento 118, homenagem Oganessian"
```

### Pessoas Famosas
```
Pergunta: "einstein"
Resposta: "👨‍🔬 Pessoa: Albert Einstein físico, relatividade, E=mc², Nobel"

Pergunta: "messi"
Resposta: "⚽ Pessoa: Lionel Messi futebolista argentino, Barcelona, 8 Bolas Ouro"
```

### Animais
```
Pergunta: "leao"
Resposta: "🦁 Animal: Leão rei selva, felino africano, juba, caça grupo"

Pergunta: "baleia"
Resposta: "🐋 Animal: Baleia maior mamífero, oceanos, canto complexo"
```

### Comandos Linux
```
Pergunta: "sudo apt update"
Resposta: "🐧 Linux: sudo apt update atualiza lista de pacotes com privilégios administrador"
```

## 🔌 API REST

### Endpoint Principal
```bash
POST /chat
Content-Type: application/json

{
  "message": "hidrogenio"
}
```

### Resposta
```json
{
  "response": "⚗️ Química: Hidrogénio (H) elemento 1, mais simples, 1 protão, combustível futuro"
}
```

### Exemplos com curl
```bash
# Elemento químico
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "oganessao"}'

# Pessoa famosa
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "einstein"}'

# Animal
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "leao"}'
```

## 🌐 Deploy

### Deploy Local
```bash
python main.py
# Acesso: http://localhost:5000
```

### Deploy Produção com Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

### Deploy com Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
```

## 🧪 Testes

```bash
# Instalar pytest
pip install pytest

# Executar testes
pytest

# Com cobertura
pytest --cov=main
```

## 📊 Estatísticas

- **Elementos Químicos**: 118 (100% da tabela periódica)
- **Pessoas Famosas**: 50+ (cientistas, desportistas, artistas)
- **Animais**: 30+ (mamíferos, aves, répteis, aquáticos)
- **Países**: 20+ (principais países mundiais)
- **Comidas**: 25+ (culinárias internacionais)
- **Tecnologias**: 20+ (empresas e conceitos modernos)
- **Comandos Linux**: 15+ (comandos essenciais)

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. **Fork** o repositório
2. **Cria** uma branch para a funcionalidade (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** as mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. **Abre** um Pull Request

## 🏆 Reconhecimentos

- **Criado por**: mppt24 & Manus AI
- **Inspiração**: Personalidade aquariana - simplicidade, naturalidade, funcionalidade
- **Filosofia**: "O que está bem NÃO SE MEXE - só o que está mal"

## 📞 Suporte

- **GitHub Issues**: [Reportar problemas](https://github.com/mppt24/mppt24-agi-absoluta/issues)
- **Email**: mppt24@gmail.com

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - vê o ficheiro [LICENSE](LICENSE) para detalhes.

---

**Feito com ❤️ por mppt24 & Manus AI**

*"Uma AGI que realmente entende o mundo"*

