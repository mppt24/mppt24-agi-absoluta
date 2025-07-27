# 🤝 Guia de Contribuição - mppt24 AGI ABSOLUTA

**Bem-vindo à comunidade mppt24! Juntos vamos construir o futuro da Inteligência Artificial Geral.**

## 🌟 Por que Contribuir?

A mppt24 AGI ABSOLUTA é mais que um projeto - é um movimento para democratizar o acesso ao conhecimento universal. Ao contribuir, você está:

- 🧠 **Avançando a IA**: Ajudando a criar uma AGI verdadeiramente útil
- 🌍 **Impactando o mundo**: Democratizando acesso ao conhecimento
- 🚀 **Crescendo profissionalmente**: Desenvolvendo skills em IA de ponta
- 🤝 **Construindo comunidade**: Conectando-se com desenvolvedores globais

## 🎯 Tipos de Contribuição

### 💻 **Desenvolvimento de Código**
- Novas funcionalidades e melhorias
- Correções de bugs e otimizações
- Testes automatizados
- Refatoração e limpeza de código

### 📚 **Conhecimento e Conteúdo**
- Expansão da base de conhecimento
- Novos domínios de especialização
- Verificação e correção de informações
- Tradução para novos idiomas

### 📖 **Documentação**
- Guias de uso e tutoriais
- Documentação técnica
- Exemplos práticos
- Vídeos explicativos

### 🎨 **Design e UX**
- Interface de utilizador
- Experiência do utilizador
- Acessibilidade
- Design visual

### 🧪 **Testes e QA**
- Testes manuais
- Automação de testes
- Relatórios de bugs
- Validação de funcionalidades

### 🌐 **Comunidade**
- Suporte a outros utilizadores
- Organização de eventos
- Criação de conteúdo educacional
- Evangelização do projeto

## 🚀 Primeiros Passos

### 1. **Configuração do Ambiente**

```bash
# Fork o repositório no GitHub
# Clone o seu fork
git clone https://github.com/SEU_USERNAME/mppt24-agi-absoluta.git
cd mppt24-agi-absoluta

# Adicione o repositório original como upstream
git remote add upstream https://github.com/mppt24/mppt24-agi-absoluta.git

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Instale dependências de desenvolvimento
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. **Executar Localmente**

```bash
# Execute a aplicação
python main.py

# Execute os testes
pytest

# Execute linting
flake8 .

# Execute formatação
black .
```

### 3. **Encontrar uma Tarefa**

- 🔍 **Issues para iniciantes**: Procure por `good first issue`
- 🆘 **Ajuda necessária**: Procure por `help wanted`
- 🐛 **Bugs**: Procure por `bug`
- ✨ **Funcionalidades**: Procure por `enhancement`

## 📋 Processo de Contribuição

### **Fluxo de Trabalho Git**

```bash
# 1. Sincronize com upstream
git checkout main
git pull upstream main

# 2. Crie uma branch para sua funcionalidade
git checkout -b feature/nome-da-funcionalidade

# 3. Faça suas mudanças
# ... desenvolva ...

# 4. Commit suas mudanças
git add .
git commit -m "feat: adiciona nova funcionalidade X"

# 5. Push para seu fork
git push origin feature/nome-da-funcionalidade

# 6. Abra um Pull Request no GitHub
```

### **Convenções de Commit**

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
tipo(escopo): descrição

[corpo opcional]

[rodapé opcional]
```

**Tipos:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Mudanças na documentação
- `style`: Formatação, sem mudança de lógica
- `refactor`: Refatoração de código
- `test`: Adicionar ou corrigir testes
- `chore`: Tarefas de manutenção
- `perf`: Melhorias de performance
- `ci`: Mudanças no CI/CD

**Exemplos:**
```
feat(conhecimento): adiciona elementos químicos 90-118

fix(api): corrige resposta para mensagens vazias

docs(readme): atualiza instruções de instalação

test(core): adiciona testes para processamento de mensagens
```

## 🧠 Contribuindo com Conhecimento

### **Estrutura da Base de Conhecimento**

```python
conhecimento_absoluto = {
    # Categoria: Descrição formatada
    "palavra_chave": "🔸 Categoria: Informação específica e concisa",
    
    # Exemplos:
    "hidrogenio": "⚗️ Química: Hidrogénio (H) elemento 1, mais simples, 1 protão, combustível futuro",
    "einstein": "👨‍🔬 Pessoa: Albert Einstein físico, relatividade, E=mc², Nobel",
    "leao": "🦁 Animal: Leão rei selva, felino africano, juba, caça grupo"
}
```

### **Diretrizes para Adicionar Conhecimento**

#### **Elementos Químicos**
```python
"elemento": "⚗️ Química: Nome (Símbolo) elemento X, propriedades principais, uso comum"
```

#### **Pessoas Famosas**
```python
"pessoa": "👨‍🔬 Pessoa: Nome completo profissão, principais conquistas, contexto histórico"
```

#### **Animais**
```python
"animal": "🦁 Animal: Nome características físicas, habitat, comportamento distintivo"
```

#### **Países**
```python
"pais": "🌍 País: Nome capital, continente, características únicas, cultura"
```

#### **Tecnologia**
```python
"tecnologia": "📱 Tecnologia: Nome descrição, empresa/criador, impacto/uso"
```

#### **Comandos Linux**
```python
"comando": "🐧 Linux: comando descrição da funcionalidade e uso prático"
```

### **Critérios de Qualidade**

- ✅ **Precisão**: Informação factualmente correta
- ✅ **Concisão**: Máximo 80 caracteres
- ✅ **Relevância**: Informação mais importante primeiro
- ✅ **Consistência**: Seguir formato estabelecido
- ✅ **Emoji apropriado**: Usar emoji representativo da categoria

## 🧪 Padrões de Teste

### **Estrutura de Testes**

```python
def test_novo_conhecimento():
    """Testa nova categoria de conhecimento"""
    agi = MPPT24AGI()
    
    # Teste básico
    response = agi.processar_mensagem("nova_palavra")
    assert "categoria_esperada" in response
    
    # Teste case-insensitive
    response_upper = agi.processar_mensagem("NOVA_PALAVRA")
    assert response == response_upper
    
    # Teste com variações
    response_var = agi.processar_mensagem("nova palavra")
    assert "categoria_esperada" in response_var
```

### **Cobertura de Testes**

- **Funcionalidade nova**: 100% cobertura obrigatória
- **Conhecimento novo**: Teste para palavra exata e variações
- **API endpoints**: Teste casos de sucesso e erro
- **Edge cases**: Teste entradas inválidas e extremas

## 📖 Padrões de Documentação

### **Docstrings**

```python
def processar_mensagem(self, mensagem: str) -> str:
    """
    Processa uma mensagem do utilizador e retorna resposta apropriada.
    
    Args:
        mensagem: A mensagem do utilizador (case-insensitive)
        
    Returns:
        Resposta formatada da AGI com emoji e categoria
        
    Examples:
        >>> agi = MPPT24AGI()
        >>> agi.processar_mensagem("hidrogenio")
        "⚗️ Química: Hidrogénio (H) elemento 1, mais simples, 1 protão, combustível futuro"
    """
```

### **README Updates**

Ao adicionar funcionalidades, atualize:
- Seção de funcionalidades
- Exemplos de uso
- Estatísticas (contadores)
- Screenshots se aplicável

## 🎨 Padrões de Design

### **Interface Web**

- **Cores principais**: #00bfff (azul elétrico), #1a1a1a (fundo escuro)
- **Tipografia**: Sans-serif, legível em todos os tamanhos
- **Responsividade**: Mobile-first design
- **Acessibilidade**: Contraste WCAG AA, navegação por teclado

### **Componentes**

```css
/* Exemplo de componente */
.chat-message {
    background: #333;
    color: #fff;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 2px 10px rgba(0, 191, 255, 0.3);
}
```

## 🔍 Processo de Review

### **Checklist para Pull Requests**

#### **Código**
- [ ] Código segue padrões de estilo (black, flake8)
- [ ] Testes passam (pytest)
- [ ] Cobertura de testes mantida/melhorada
- [ ] Sem warnings ou erros
- [ ] Performance não degradada

#### **Funcionalidade**
- [ ] Funcionalidade funciona como esperado
- [ ] Edge cases considerados
- [ ] Compatibilidade mantida
- [ ] Documentação atualizada

#### **Conhecimento**
- [ ] Informação factualmente correta
- [ ] Formato consistente
- [ ] Emoji apropriado
- [ ] Testes incluídos

### **Processo de Aprovação**

1. **Automated checks**: CI/CD deve passar
2. **Code review**: Pelo menos 1 aprovação de maintainer
3. **Testing**: Funcionalidade testada manualmente
4. **Documentation**: Documentação revista e aprovada

## 🏆 Reconhecimento de Contribuidores

### **Níveis de Contribuição**

#### 🥉 **Contribuidor Bronze**
- 1+ PR aceite
- Badge no perfil GitHub
- Menção no CONTRIBUTORS.md

#### 🥈 **Contribuidor Prata**
- 5+ PRs aceites
- Acesso a canal privado Discord
- Convite para reuniões mensais

#### 🥇 **Contribuidor Ouro**
- 20+ PRs aceites
- Direitos de review
- Participação em decisões técnicas

#### 💎 **Core Contributor**
- 50+ PRs aceites
- Acesso de commit direto
- Participação em roadmap

### **Programa de Mentoria**

- **Mentores experientes** para novos contribuidores
- **Sessões 1:1** mensais
- **Workshops técnicos** trimestrais
- **Certificados oficiais** de participação

## 📅 Eventos e Comunidade

### **Eventos Regulares**

#### **Hackathons Trimestrais**
- Desenvolvimento de funcionalidades específicas
- Prémios para melhores contribuições
- Networking com equipa core

#### **Webinars Mensais**
- Apresentação de novas funcionalidades
- Tutoriais técnicos
- Q&A com maintainers

#### **Conferência Anual mppt24Con**
- Apresentações técnicas
- Workshops práticos
- Networking global

### **Canais de Comunicação**

- **GitHub Discussions**: Discussões técnicas e ideias
- **Discord**: Chat em tempo real
- **Email**: mppt24@gmail.com para questões privadas
- **Twitter**: @mppt24agi para atualizações

## 🚨 Código de Conduta

### **Nossos Valores**

- **Respeito**: Tratamos todos com dignidade
- **Inclusão**: Valorizamos diversidade de perspectivas
- **Colaboração**: Trabalhamos juntos para objetivos comuns
- **Excelência**: Buscamos sempre a melhor qualidade
- **Transparência**: Comunicamos aberta e honestamente

### **Comportamentos Esperados**

- ✅ Linguagem respeitosa e inclusiva
- ✅ Feedback construtivo e específico
- ✅ Foco em soluções, não problemas
- ✅ Reconhecimento de contribuições alheias
- ✅ Paciência com iniciantes

### **Comportamentos Inaceitáveis**

- ❌ Linguagem ofensiva ou discriminatória
- ❌ Assédio de qualquer tipo
- ❌ Ataques pessoais ou trolling
- ❌ Spam ou autopromoção excessiva
- ❌ Violação de privacidade

### **Enforcement**

Violações podem resultar em:
1. **Aviso**: Primeira ocorrência
2. **Suspensão temporária**: Reincidência
3. **Banimento permanente**: Violações graves

## 📊 Métricas e Objetivos

### **Objetivos da Comunidade 2025**

- 🎯 **100+ contribuidores ativos**
- 🎯 **500+ PRs aceites**
- 🎯 **1000+ issues resolvidas**
- 🎯 **50+ novos domínios de conhecimento**
- 🎯 **10+ idiomas suportados**

### **Métricas de Qualidade**

- **Time to first response**: <24h para issues
- **Time to merge**: <7 dias para PRs
- **Bug resolution**: <48h para bugs críticos
- **Documentation coverage**: 100% para APIs públicas

## 🎓 Recursos de Aprendizagem

### **Para Iniciantes**

- [Python Basics](https://python.org/about/gettingstarted/)
- [Flask Tutorial](https://flask.palletsprojects.com/tutorial/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Open Source Guide](https://opensource.guide/)

### **Para Desenvolvimento IA**

- [Machine Learning Basics](https://ml-course.github.io/)
- [Natural Language Processing](https://web.stanford.edu/class/cs224n/)
- [AI Ethics](https://www.partnershiponai.org/)
- [Responsible AI](https://ai.google/responsibilities/responsible-ai-practices/)

### **Para Contribuidores Avançados**

- [System Design](https://github.com/donnemartin/system-design-primer)
- [API Design](https://restfulapi.net/)
- [Testing Best Practices](https://testdriven.io/)
- [Documentation Writing](https://www.writethedocs.org/)

## 🔮 Visão de Futuro

### **Próximos 12 Meses**

A comunidade mppt24 crescerá para se tornar uma das principais comunidades de IA open-source do mundo. Esperamos:

- **Comunidade global** com contribuidores de 50+ países
- **Ecossistema robusto** de plugins e extensões
- **Parcerias académicas** com universidades de prestígio
- **Impacto social** mensurável na educação e pesquisa

### **Como Você Pode Ajudar**

- 🚀 **Contribua regularmente** com código ou conhecimento
- 🌟 **Evangelize o projeto** nas suas redes
- 🤝 **Mentorize novos contribuidores**
- 💡 **Proponha ideias inovadoras**
- 📢 **Participe em eventos** e discussões

## 📞 Suporte e Contato

### **Precisa de Ajuda?**

- **GitHub Issues**: Para bugs e funcionalidades
- **GitHub Discussions**: Para perguntas gerais
- **Discord**: Para chat em tempo real
- **Email**: mppt24@gmail.com para questões privadas

### **Quer Contribuir Mas Não Sabe Como?**

1. **Junte-se ao Discord** e apresente-se
2. **Procure issues** marcadas como `good first issue`
3. **Participe em discussões** para entender o projeto
4. **Contacte um mentor** através do programa de mentoria

---

## 🙏 Agradecimentos

Obrigado por considerar contribuir para a mppt24 AGI ABSOLUTA! Cada contribuição, por menor que seja, nos aproxima da visão de democratizar o acesso ao conhecimento universal.

Juntos, estamos construindo não apenas uma ferramenta, mas um movimento que pode transformar como a humanidade acede e utiliza o conhecimento.

**Bem-vindo à família mppt24!** 🎉

---

*Este documento é atualizado regularmente. Última atualização: Janeiro 2025*

