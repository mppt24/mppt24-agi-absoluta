# Segurança

O AGI Absoluta é um protótipo de utilização local. O serviço não tem autenticação própria. A configuração fornecida publica a porta no endereço de loopback. Vê os [limites do protótipo](README.md#limites-do-protótipo) antes de arrancar.

A aplicação pode guardar mensagens e respostas numa base SQLite local. Usa dados fictícios em testes e nunca partilhes essa base, credenciais ou registos com dados pessoais.

## Comunicar um problema

Usa **Report a vulnerability** no separador [Security](https://github.com/mppt24/mppt24-agi-absoluta/security), se o GitHub apresentar essa opção. Se não estiver disponível, pede um canal privado numa issue sem incluir detalhes técnicos nem dados pessoais. Depois partilha a versão afetada e o impacto observado nesse canal.
