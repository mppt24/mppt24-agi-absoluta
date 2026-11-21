# MPPT24 AGI Absoluta

Protótipo de chat local do [MPPT24OS](https://github.com/mppt24/MPPT24OS). Tem uma calculadora, um conversor de unidades e respostas predefinidas por tema. Funciona sem chaves de API.

[![MPPT24 AGI Absoluta. Protótipo de chat local com calculadora, conversões e respostas por temas.](docs/infografico.png)](docs/infografico.png)

## Experimentar

Com Docker Engine 28 ou posterior e Docker Compose, executa na pasta do repositório:

```bash
docker compose up --build --wait
```

Abre [http://127.0.0.1:5013](http://127.0.0.1:5013). Podes escrever uma mensagem ou escolher um exemplo na página.

| Experimenta | Resultado esperado |
| --- | --- |
| `calcular sqrt(16)` | `4.0` |
| `converter 1 hora em minutos` | `60 minutos` |
| `oxigénio` | Resposta predefinida sobre o elemento 8 |

Para parar o serviço, usa `docker compose down`. Para consultar os registos, usa `docker compose logs mppt24-agi`. Se a porta 5013 já estiver ocupada, usa `MPPT24_PORT=5014 docker compose up --build --wait` e abre a porta 5014 no navegador.

### Limites do protótipo

O serviço foi preparado para utilização local e não tem autenticação. O Docker publica a porta em `127.0.0.1`. Em versões anteriores à 28.0.0, equipamentos no mesmo segmento de rede podem alcançar portas publicadas em localhost. [Nota do Docker](https://docs.docker.com/engine/network/port-publishing/#setting-the-default-bind-address-for-containers)

Algumas mensagens e respostas ficam guardadas numa base SQLite local. O volume Docker conserva esse histórico quando paras os contentores. Evita introduzir dados privados no chat. As respostas por tema vêm de um conjunto local limitado e as integrações externas continuam em avaliação.

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
