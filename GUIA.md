# Guia de MPPT24 AGI Absoluta

**Estado:** Chat local validado.

Calculadora, conversões e respostas por temas.

[![MPPT24 AGI Absoluta. Exemplos no navegador. 43 testes e arranque Docker. Histórico SQLite local.](docs/guia-visual.png)](docs/guia-visual.png)

## Onde começar

Segue [Experimentar o chat no computador](README.md#experimentar). Para ver o que a aplicação faz sem instalar, lê os [exemplos do chat](README.md#exemplos-do-chat) e consulta o [infográfico da aplicação](README.md#infogr%C3%A1fico).

## Como confirmar

Corre a suite indicada no README ou consulta «Testar o AGI Absoluta» em **Actions**. A CI também verifica o arranque em Docker e uma resposta pela API.

## Como ler os registos

`docker compose logs mppt24-agi` mostra o arranque e os pedidos HTTP. Para confirmar uma versão, abre a execução do commit em **Actions**. O histórico de conversas fica separado, em SQLite.

### Exemplo fictício

```text
OK · Chat local · Conversão devolveu 60 minutos
```

Este exemplo resume o que viste no chat. O registo HTTP confirma se o pedido foi atendido. Compara o texto da resposta com o resultado esperado para confirmar o cálculo ou a conversão. Se a página não abrir, segue o [diagnóstico do chat](README.md#se-o-chat-n%C3%A3o-abrir).

## Cuidados

O serviço destina-se a uso local. Evita dados privados nas mensagens. A tag antiga `v1.3.0` tem um erro de sintaxe confirmado. Para testar a base atual, segue o README da `main`.

Vê também o [infográfico da aplicação](docs/infografico.png).
