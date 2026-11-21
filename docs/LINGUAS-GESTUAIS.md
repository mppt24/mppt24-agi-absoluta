# Línguas gestuais no AGI Absoluta

Abre **Acessibilidade** e escolhe uma língua. Cada opção mantém o seu nome e as suas fontes. A aplicação pode carregar os vídeos selecionados, mas as conversas do chat não são enviadas aos sites aqui indicados.

## Disponível no painel

| Língua | Recurso |
| --- | --- |
| LGP · Língua Gestual Portuguesa | Alfabeto manual local, seis entradas da Infopédia, Dicionário Geral de LGP, reportagem da Lusa com intérprete no leitor integrado, vídeo do EstudoEmCasa e demonstrações do avatar PE2LGP. |
| LSE · Língua de Sinais Espanhola | Amostra gravada com Mónica, reproduzida no painel a partir do Wikimedia Commons, e Dicionário DILSE da Fundação CNSE. |
| BSL · Língua Gestual Britânica | Dicionário e vídeos do BSL SignBank da University College London. |
| Libras · Língua Brasileira de Sinais | Ligação às ferramentas VLibras do Governo do Brasil. |

A soletração manual serve para representar letras. Um dicionário permite consultar gestos isolados. A tradução de uma frase exige que o significado e a gramática da língua de destino sejam preservados.

## Código, modelos e integração

| Projeto | Resultado da verificação |
| --- | --- |
| [TALG](https://talg.pt/) · Portugal | O site apresenta um MVP em desenvolvimento. A ligação pública de código indicada pelo autor devolveu 404. A licença do motor, os modelos e uma API integrável ficaram por confirmar. |
| [PE2LGP](https://github.com/mattgoncalves/PE2LGP) · Portugal | Repositório do tradutor disponível sob MIT. Produz glosas e marcadores linguísticos e requer FreeLing 4.1 e um modelo português do spaCy. [O animator PE2LGP](https://www.hlt.inesc-id.pt/w/PE2LGP_Avatar) é um trabalho separado, com exemplos publicados. A demonstração do tradutor indicada na continuação do trabalho devolveu HTTP 502 e 503 nas verificações. |
| [SignON](https://signon-project.eu/about-signon/project-objectives/) · Europa | Investigação em ISL, BSL, NGT, VGT e LSE. Serve de referência para separar texto, tradução e animação. A LGP está fora das línguas indicadas pelo projeto. |
| [EASIER](https://www.project-easier.eu/about-easier/) e [ZurichNLP](https://github.com/sign-language-processing/spoken-to-signed-translation) · Europa | Existem resultados de investigação e código de processamento de texto para glosas e pose. A demonstração da ZurichNLP documenta variedades gestuais suíças. |
| [VLibras](https://www.gov.br/conecta/catalogo/apis/vlibras) · Brasil | O catálogo oficial descreve um serviço para texto, glosas e vídeo em Libras. O painel abre a fonte oficial. A ligação ao serviço de tradução ainda está por desenvolver. |

Para publicar uma integração de tradução, é preciso confirmar a licença do código, do modelo e das animações, ensaiar a reprodução e validar frases completas com pessoas que usam a língua gestual em causa.

## Créditos do material

- [Alfabeto Manual LGP](https://commons.wikimedia.org/wiki/File:Alfabeto_Manual_LGP.jpg), Lúcia Carvalho, Wikimedia Commons. Domínio público. O JPEG original é incluído sem alterações.
- [Mónica a usar LSE](https://commons.wikimedia.org/wiki/File:WIKITONGUES-_M%C3%B3nica_signing_Spanish_Sign_Language.webm), Wikitongues e Ana Laguna. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). O leitor carrega o vídeo original, sem edição.

- [Interpretação em LGP no Rock in Rio Lisboa](https://commons.wikimedia.org/wiki/File:L%C3%ADngua_Gestual_Portuguesa_chegou_aos_palcos_principais_do_Rock_In_Rio.webm), Lusa, 2022. [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). O painel usa a versão de 480p do Wikimedia Commons, com o áudio original, um resumo em texto e [texto sincronizado em português](../static/lgp-rock-in-rio-resumo.pt.vtt). O texto acompanha as ideias principais do áudio e descreve algumas imagens. Foi adaptado a partir da reportagem com apoio de reconhecimento local de voz. A faixa de origem está sob CC BY 3.0.
