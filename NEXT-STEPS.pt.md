*Leia em [English](NEXT-STEPS.md) · [Español](NEXT-STEPS.es.md).*

# Próximos passos

Em ordem. Cada item traz seu critério de pronto.

---

## Concluído em 30 de agosto de 2026

**Repositório GitHub público criado**, em `github.com/tecosodreaboutdigital/harness-medir`. Commit inicial com os 23 arquivos que existiam na época, sem dado sensível. LICENSE (MIT) acrescentada dentro do que então era `skills/levantando-briefing/`, coerente com o que o README da skill já declarava. Nenhuma licença na raiz, porque os artigos seguem todos os direitos reservados.

**Guia compacto reescrito por completo.** Ver a entrada correspondente em `STATUS.md` para o detalhamento. Critério de pronto cumprido: dezessete fichas de seis campos, toda ferramenta verificada em `sources/inventory.md` (três fontes novas verificadas nessa rodada: Semgrep, LangGraph, GitHub Spec Kit com link direto), e cada passo do MEDIR carregando uma crítica registrada.

**Parte 2 traduzida para inglês e espanhol**, no mesmo arquivo, com o seletor. `build/build_p2.py` reescrito para montagem trilíngue, no mesmo padrão que `build/build_all.py` já usava: extrai o corpo em PT do arquivo vigente (que é a fonte da verdade, não `build/body_p2_pt.html`, que estava desatualizado), monta EN e ES a partir de `build/body_p2_en.html` e `build/body_p2_es.html`, prefixa tudo por idioma via `scope()`. Os três botões funcionam e não há âncora quebrada. Como efeito colateral, o JavaScript de troca de idioma em `harness-p1.html` e `harness-p2.html` ganhou roteamento por âncora (`#en-opening` seleciona a aba certa antes de rolar), para que um link cruzado entre as peças em inglês ou espanhol não caísse sempre na aba em português.

**Trinta skills de terceiro instaladas para uso neste projeto**, cinco coleções (superpowers inteira, uma seleção curada de doze do mattpocock/skills, c4-skills inteira, o guia inspirado em Karpathy, ai-slop-cleaner), todas MIT, todas auditadas contra o próprio checklist do guia compacto antes de instalar. Vivem em `.claude/skills/`, fora do controle de versão. Documentação completa, com um registro de uso real que cresce a cada sessão, em `TOOLS.md`. Crédito visível no rodapé de `harness-p1.html`, `harness-p2.html` (três idiomas) e `harness-toolkit.html`.

**A skill separada em repositório próprio**, no que então era `github.com/tecosodreaboutdigital/levantando-briefing`, público, MIT, no mesmo padrão das demais skills citadas no guia compacto. Removida de `skills/` dentro do harness-medir, que agora só aponta para lá.

**Diário de bordo criado**, `docs/logbook.html`, trilíngue, gerado em duas etapas: `build/generate_logbook_metrics.py` reconstrói a série real (palavras publicadas por `git show` em cada commit, linhas em `build/` e nos documentos de governança, tokens somados do `usage` real de cada mensagem no transcript `.jsonl` da sessão, atribuídos ao commit cronologicamente seguinte) e escreve `docs/assets/logbook-metrics.json`; `build/build_logbook.py` monta a página a partir desse JSON, nunca escrita à mão. Dois gráficos SVG empilhados, mesmo eixo X, sem eixo Y duplo. Seis marcos reais registrados (o histórico completo do repositório até aqui, não uma amostra), mais o que ainda não tinha fechado marco.

**GitHub Pages ativado**, publicando o repositório em `tecosodreaboutdigital.github.io/harness-medir`. `.nojekyll` acrescentado para servir os arquivos HTML como estão, sem processamento Jekyll. Sem isso, nenhum artigo era de fato legível como página na web ali, só como código-fonte no visualizador do GitHub.

**Reestruturação para inglês primário nos dois repositórios públicos.** O inglês se tornou o idioma de produção primário, decisão tomada no meio desta sessão. Todo documento de governança renomeado e reescrito com o inglês na frente (`PADROES.md` → `STANDARDS.md`, `ESTADO.md` → `STATUS.md`, `PROXIMOS-PASSOS.md` → `NEXT-STEPS.md`, `FERRAMENTAS.md` → `TOOLS.md`, `fontes/inventario.md` → `sources/inventory.md`), cada um com uma tradução em português e espanhol ao lado. `harness-caixa-de-ferramentas.html` → `harness-toolkit.html`, `docs/diario-de-bordo.html` → `docs/logbook.html`, com os scripts correspondentes em `build/` renomeados e, no caso do guia compacto, reescritos numa montagem trilíngue com inglês como aba padrão. `harness-p1.html`, `harness-p2.html` e `docs/logbook.html` tiveram a aba padrão trocada de português para inglês, tanto nos arquivos montados quanto nos scripts que os regeneram. Um banner de dica de idioma do navegador foi acrescentado às quatro páginas trilíngues (navegadores em português ou espanhol recebem uma oferta dispensável de troca, qualquer outro cai silenciosamente para o inglês). O repositório da skill foi renomeado de `levantando-briefing` para `intake-briefing`, e cada um dos seus quatro arquivos foi reescrito com o inglês na frente, com traduções `.pt.md`/`.es.md`, além de uma linha estática de navegação de idioma no topo de cada um, já que o GitHub não executa JavaScript dentro do Markdown renderizado. Ver `STATUS.md` para o detalhamento completo e a seção Idiomas de `STANDARDS.md` para a regra em si.

**Quatro skills recomendadas de fora, avaliadas, uma adotada.** `ponytail`, `no-ai-slop`, `taste-skill` e `impeccable` foram comparadas por relevância, sinal de manutenção, número de contribuidores e licença antes de qualquer uma tocar este repositório. `ponytail` (117 mil estrelas, com benchmark, mantida ativamente) teria resolvido a ressalva de atribuição indevida que já pesa sobre `karpathy-guidelines`, mas ficou de fora por ora, não descartada. `no-ai-slop` é uma skill de limpeza de prosa genuinamente útil cuja lista de palavras banidas inclui, por acaso, o termo central deste projeto, "harness", e também ficou de fora até decidirmos como fazer a exceção. `taste-skill` foi recusada de vez: suas dez subskills usam exatamente o registro de hype que um projeto sobre evidência em vez de opinião não deveria citar, e seis contribuidores contra 82 mil estrelas é uma base frágil. `impeccable` foi adotada: Apache-2.0, 30 contribuidores, versionada (v4.1.2), deriva da própria skill frontend-design da Anthropic, e suas 61 regras determinísticas de detector combinam com a própria definição de Inspecionar, evidência em vez de opinião, aplicada especificamente a design de frontend. Instalada só como documentação, `SKILL.md` e `reference/`, deixando de propósito a árvore `scripts/` que o CLI dela precisa, ver `TOOLS.md`. Acrescentada como a décima oitava ficha do guia compacto, em Inspecionar, nos três idiomas, ver `sources/inventory.md` para o registro de verificação.

---

## 1. Rodada de pesquisa da parte 3

**Superada por um dossiê de trabalho.** `docs/harness-p3-p4-briefing.pt.md`, acrescentado em 30 de agosto de 2026, já levanta sete eixos de pesquisa (um a mais que a lista abaixo) com fontes primárias verificadas, um diagnóstico estrutural, e uma especificação visual, e também propõe uma quarta parte para a série, ainda não refletida em `README.md` ou `STATUS.md`. Só em português, documento de trabalho interno, não voltado ao leitor, a mesma exceção que `sources/inventory.md` já tem. Trate o dossiê como o ponto de partida real desta rodada; a lista abaixo é o escopo original da rodada, mantida como registro.

Rodada dedicada, não complemento. O que ainda falta levantar:

- Literatura de segurança de agentes, com foco em instrução maliciosa que chega dentro de um dado
- Incidentes reais documentados envolvendo agentes com efeito externo
- A posição da autoridade brasileira de proteção de dados sobre decisão automatizada
- Obrigações regulatórias europeias para sistemas classificados como de alto risco
- Padrões de auditoria e registro aplicáveis a agentes
- O que já existe de prática estabelecida sobre alçada e aprovação em sistemas autônomos

**Pronto quando:** cada um dos seis eixos tiver ao menos duas fontes primárias verificadas.

---

## 2. Escrever a parte 3

Estrutura prevista, sujeita ao que a pesquisa revelar:

1. A primeira ação irreversível (abertura, com a diretora em N2 diante do primeiro envio a um cliente)
2. Permissão não é instrução (por que a alçada precisa viver fora do modelo)
3. Quando a ordem chega dentro do dado
4. O que precisa estar registrado
5. Reversão: o que significa desfazer, de fato
6. Skill de terceiro é código de terceiro
7. Obrigações legais
8. Quem responde
9. O que muda na mesa do seu conselho
10. Onde você está (o fechamento da série)

**Pronto quando:** as três versões estiverem prontas, o arco da personagem se fechar, e a peça funcionar sozinha para um leitor que não leu as anteriores.

---

## 3. Consolidar o playbook

Reaproveita as três partes e o guia, e acrescenta o que ainda não existe:

- Modelo de contrato de tarefa
- Modelo de skill, derivado dos três exemplos da parte 2
- Modelo de recibo de execução
- Matriz de risco por faixa
- Diagnóstico de faixa, versão questionário
- Trilha de implantação de N0 a N3

---

## Pendências menores, a decidir a qualquer momento

**Caso real de abertura.** A cena é composta. Se surgir um caso real anonimizado do ecossistema do autor, substituí-la elevaria bastante o texto.

**Borda da caixa do sumário.** É a única borda de caixa que sobrou nos documentos. Decidir se ela sai, para ficar coerente com a remoção das demais.

**Fundo da citação em destaque na impressão.** Depende de o navegador estar configurado para imprimir gráficos de plano de fundo. Alternativa sem dependência: um filete fino acima e abaixo do bloco.

**Grafia do inglês.** Hoje é britânica, e essa é a leitura padrão do projeto agora. Se o público-alvo migrar para os Estados Unidos, converter.

**Publicação.** Resolvida em 30 de agosto de 2026: GitHub Pages ativo em `tecosodreaboutdigital.github.io/harness-medir`. Verificar, depois do primeiro build automático, se os documentos renderizam corretamente lá (o link com maior chance de precisar de ajuste é algum caminho relativo entre eles).
