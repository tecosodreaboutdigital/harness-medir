# Próximos passos

Em ordem. Cada item traz o critério de pronto.

---

## 1. Reescrever o guia compacto

**Arquivo:** `harness-caixa-de-ferramentas.html`

Refazer inteiro, organizado pelos cinco passos do MEDIR em vez de por categoria de produto.

Toda entrada vira ficha de seis campos, conforme `PADROES.md`: qual problema resolve, o que você ganha, para quem serve por faixa, faixa mínima, quando não usar, como começar em quinze minutos.

Distribuição por passo:

| Passo | Fichas |
|---|---|
| Mapear | levantando-briefing (nossa), guia inspirado em Karpathy, c4-skills, especificação antes do código com a crítica |
| Equipar | superpowers, mattpocock/skills, planning-with-files |
| Delegar | holdfast, classes de ambiente, orquestração programada |
| Inspecionar | dependency-cruiser, Stryker, Semgrep, sensors-cli |
| Reforçar | ai-slop-cleaner, limpeza como cadência, coleta de lixo |

Manter as três seções que não são fichas: como usar o documento, os três roteiros práticos, e antes de instalar qualquer coisa.

Adicionar seção de diagnóstico no início, para o leitor que chega da parte 1 descobrir em que faixa está.

Manter o aviso de validade datado no topo.

**Pronto quando:** cada uma das dezesseis fichas tem os seis campos preenchidos, toda ferramenta citada consta como verificada em `fontes/inventario.md`, e cada passo do MEDIR tem pelo menos uma crítica registrada.

---

## 2. Traduzir a parte 2 e o guia compacto

Inglês e espanhol, no mesmo arquivo, com o seletor.

Reutilizar `build/build_all.py` como referência de montagem trilíngue. Os identificadores precisam ser prefixados por idioma através da função `scope()`.

**Pronto quando:** os três botões funcionam nas quatro peças e não há âncora quebrada.

---

## 3. Traduzir a skill de briefing

Inglês e espanhol, como arquivos separados no repositório da skill, não como seletor.

Nome sugerido: `SKILL.en.md` e `SKILL.es.md`, seguindo a convenção de README multilíngue.

---

## 4. Rodada de pesquisa da parte 3

Rodada dedicada, não complemento. O que precisa ser levantado:

- Literatura de segurança de agentes, com foco em instrução maliciosa vinda de dado
- Incidentes reais documentados envolvendo agentes com efeito externo
- Posição da autoridade brasileira de proteção de dados sobre decisão automatizada
- Obrigações regulatórias europeias para sistemas classificados como de alto risco
- Padrões de auditoria e registro aplicáveis a agentes
- O que existe de prática estabelecida sobre alçada e aprovação em sistemas autônomos

**Pronto quando:** cada um dos seis eixos tem pelo menos duas fontes primárias verificadas.

---

## 5. Escrever a parte 3

Estrutura prevista, sujeita ao que a pesquisa revelar:

1. A primeira ação irreversível (abertura, com a diretora em N2 diante do primeiro envio ao cliente)
2. Permissão não é instrução (por que alçada precisa viver fora do modelo)
3. Quando a ordem chega dentro do dado
4. O que precisa estar registrado
5. Reversão: o que significa desfazer
6. Skill de terceiro é código de terceiro
7. Obrigações legais
8. Quem responde
9. O que muda no seu comitê
10. Onde você está (fechamento da série)

**Pronto quando:** as três versões estão prontas, a personagem fecha o arco, e a peça funciona sozinha para um leitor que não leu as anteriores.

---

## 6. Consolidar o playbook

Reaproveita as três partes e o guia, e acrescenta o que não existe:

- Modelo de contrato de tarefa
- Modelo de skill, derivado dos três exemplos da parte 2
- Modelo de recibo de execução
- Matriz de risco por faixa
- Diagnóstico de faixa, versão questionário
- Trilha de implantação de N0 a N3

---

## Pendências menores, a decidir a qualquer momento

**Caso real de abertura.** A cena é composta. Se surgir um caso real anonimizado do ecossistema do autor, substituir eleva o texto.

**Borda da caixa de índice.** É a única borda de caixa que sobrou nos documentos. Decidir se sai, para ficar coerente com a remoção das demais.

**Fundo das citações em destaque na impressão.** Depende da opção de imprimir gráficos de plano de fundo no navegador. Alternativa sem dependência: filete fino acima e abaixo do bloco.

**Grafia do inglês.** Hoje é britânica. Se o alvo for os Estados Unidos, converter.

**Publicação.** Definir onde os HTMLs ficam hospedados e como apontam para os repositórios de skill no GitHub.
