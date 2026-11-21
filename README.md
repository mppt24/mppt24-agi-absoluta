# MPPT24 AGI Absoluta

Protótipo de chat local do [MPPT24OS](https://github.com/mppt24/MPPT24OS). Tem uma calculadora, um conversor de unidades e respostas predefinidas por tema. Funciona sem chaves de API.

[Experimentar o chat](#experimentar) · [Ver o infográfico](#infogr%C3%A1fico) · [Guia de leitura e cuidados](GUIA.md)

## Experimentar

Usa um computador com Git, Docker Engine 28 ou posterior e Docker Compose. No terminal, `git --version`, `docker version` e `docker compose version` ajudam a confirmar os requisitos. Em `docker version`, verifica a versão em **Server**. Se estiveres a navegar pelo telemóvel, podes ler os [exemplos do chat](#exemplos-do-chat) e ver o [infográfico](#infogr%C3%A1fico) antes de instalar.

Se já tens o código, abre a sua pasta e executa apenas a última linha. Para uma primeira utilização, executa as três linhas pela ordem apresentada.

```bash
git clone https://github.com/mppt24/mppt24-agi-absoluta.git
cd mppt24-agi-absoluta
docker compose up --build --wait
```

Quando o comando terminar, abre o chat no computador onde arrancaste o Docker e escolhe um dos exemplos. [Abrir o chat local](http://127.0.0.1:5013)

### Exemplos do chat

| Experimenta | Resultado esperado |
| --- | --- |
| `calcular sqrt(16)` | `4.0` |
| `converter 1 hora em minutos` | `60 minutos` |
| `oxigénio` | Resposta predefinida sobre o elemento 8 |

### Se o chat não abrir

- **O Docker não responde.** Confirma que `docker version` mostra as secções **Client** e **Server**.
- **A página dá erro.** Dentro da pasta do projeto, verifica o estado com `docker compose ps` e lê as últimas mensagens com `docker compose logs --tail=30 mppt24-agi`.
- **A porta 5013 está ocupada.** Executa `MPPT24_PORT=5014 docker compose up --build --wait`. [Abrir o chat na porta 5014](http://127.0.0.1:5014)

Quando acabares, usa `docker compose down` na pasta do projeto para parar o serviço. Para testar a edição atual, usa a branch `main`. A tag histórica `v1.3.0` tem um erro de sintaxe confirmado.

### Limites do protótipo

O serviço foi preparado para utilização local e não tem autenticação. O Docker publica a porta em `127.0.0.1`. Em versões anteriores à 28.0.0, equipamentos no mesmo segmento de rede podem alcançar portas publicadas em localhost. [Nota do Docker](https://docs.docker.com/engine/network/port-publishing/#setting-the-default-bind-address-for-containers)

Algumas mensagens e respostas ficam guardadas numa base SQLite local. O volume Docker conserva esse histórico quando paras os contentores. Evita introduzir dados privados no chat. As respostas por tema vêm de um conjunto local limitado e as integrações externas continuam em avaliação.

## Infográfico

[![MPPT24 AGI Absoluta. Protótipo de chat local com calculadora, conversões e respostas por temas.](docs/infografico.png)](docs/infografico.png)

## Desenvolvimento e testes

Com Python 3.12, a partir da raiz do repositório:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
MPPT24_DB_PATH=:memory: python -m unittest discover -s tests -v
```

Para arrancar sem Docker, usa `python main.py` e abre a mesma página local. Os testes usam uma base de dados em memória e não fazem chamadas a serviços externos.

- [Aplicação Flask](main.py), [respostas por tema](knowledge.py) e [interface](templates/index.html)
- [Verificações no GitHub Actions](https://github.com/mppt24/mppt24-agi-absoluta/actions/workflows/ci.yml)
- [Contribuir](CONTRIBUTING.md) e [licença MIT](LICENSE)

Se encontrares um problema, inclui a versão usada, os passos para reproduzir e o resultado esperado. Usa mensagens de exemplo ao partilhar registos.
