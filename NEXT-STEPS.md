# Próximos passos

Em ordem. Cada item traz o critério de pronto.

---

## Concluído em 30 de agosto de 2026

**Repositório GitHub público criado**, em `github.com/tecosodreaboutdigital/harness-medir`. Commit inicial com os 23 arquivos existentes, sem dado sensível. LICENSE (MIT) adicionada dentro de `skills/levantando-briefing/`, consistente com o que o README da skill já declarava. Nada de licença na raiz, porque os artigos seguem todos os direitos reservados.

**Guia compacto reescrito por completo.** Ver a entrada correspondente em `STATUS.md` para o detalhamento. Critério de pronto batido: dezessete fichas de seis campos, toda ferramenta verificada em `sources/inventory.md` (três fontes novas verificadas nesta rodada: Semgrep, LangGraph, GitHub Spec Kit com link direto), e cada passo do MEDIR com crítica registrada.

**Parte 2 traduzida para inglês e espanhol**, no mesmo arquivo, com o seletor. `build/build_p2.py` reescrito para montagem trilíngue, no mesmo padrão de `build/build_all.py`: extrai o corpo PT do arquivo vigente (que é a fonte da verdade, não `build/body_p2_pt.html`, que estava desatualizado), monta EN e ES a partir de `build/body_p2_en.html` e `build/body_p2_es.html`, prefixa tudo por idioma via `scope()`. Os três botões funcionam e não há âncora quebrada. Como efeito colateral, o JavaScript de troca de idioma de `harness-p1.html` e `harness-p2.html` ganhou roteamento por âncora (`#en-opening` seleciona a aba certa antes de rolar), para que um link cruzado entre as peças em inglês ou espanhol não caia sempre na aba em português.

**Trinta skills de terceiro instaladas para uso neste projeto**, cinco coleções (superpowers inteira, seleção curada de doze do mattpocock/skills, c4-skills inteira, o guia inspirado em Karpathy, ai-slop-cleaner), todas MIT, todas auditadas contra o checklist do próprio guia compacto antes de instalar. Vivem em `.claude/skills/`, fora do controle de versão. Documentação completa, com registro de uso real a crescer por sessão, em `TOOLS.md`. Crédito visível no rodapé de `harness-p1.html`, `harness-p2.html` (três idiomas) e `harness-toolkit.html`.

**levantando-briefing separada em repositório próprio**, `github.com/tecosodreaboutdigital/levantando-briefing`, público, MIT, no mesmo padrão das demais skills citadas no guia compacto. Removida de `skills/` dentro do harness-medir, que agora só aponta para lá. Ativa neste ambiente via cópia local em `.claude/skills/levantando-briefing/`, fora do controle de versão.

**Diário de bordo criado**, `docs/logbook.html`, trilíngue, gerado em duas etapas: `build/generate_logbook_metrics.py` reconstrói a série real (palavras publicadas por `git show` em cada commit, linhas de `build/` e dos documentos de governança, tokens somados do `usage` real de cada mensagem no transcript `.jsonl` da sessão, atribuídos ao commit cronologicamente seguinte) e escreve `docs/assets/logbook-metrics.json`; `build/build_logbook.py` monta a página a partir desse JSON, nunca escrita à mão. Dois gráficos SVG empilhados, mesmo eixo X, sem eixo Y duplo. Seis marcos reais registrados (o histórico completo do projeto até aqui, não uma amostra), mais o que ainda não fechou marco. Referenciado em `TOOLS.md` e no rodapé de `harness-p1.html`, `harness-p2.html` (três idiomas) e do guia compacto.

**GitHub Pages ativado**, publicando o repositório em `tecosodreaboutdigital.github.io/harness-medir`. `.nojekyll` adicionado para servir os HTML como estão, sem processamento Jekyll. Sem isso, nenhum artigo era de fato legível como página na web, só como código-fonte no visualizador do GitHub.

---

## 1. Traduzir o guia compacto

Inglês e espanhol, no mesmo arquivo `harness-toolkit.html`, com o seletor.

Reutilizar `build/build_toolkit.py` como base, no mesmo padrão trilíngue que `build/build_p2.py` passou a seguir: corpo PT extraído do arquivo vigente, corpos EN e ES escritos à parte e prefixados por `scope()`.

**Pronto quando:** os três botões funcionam e não há âncora quebrada, incluindo as âncoras que a parte 2 já referencia (`#pt-equipar`, `#pt-delegar`, `#pt-ambientes`, `#pt-inspecionar`, `#pt-riscos-2`, `#pt-reforcar`, `#pt-seguranca`), que passam a precisar de equivalentes `#en-` e `#es-`.

---

## 2. Traduzir a skill de briefing

Inglês e espanhol, como arquivos separados no repositório da skill, não como seletor.

Nome sugerido: `SKILL.en.md` e `SKILL.es.md`, seguindo a convenção de README multilíngue.

---

## 3. Rodada de pesquisa da parte 3

Rodada dedicada, não complemento. O que precisa ser levantado:

- Literatura de segurança de agentes, com foco em instrução maliciosa vinda de dado
- Incidentes reais documentados envolvendo agentes com efeito externo
- Posição da autoridade brasileira de proteção de dados sobre decisão automatizada
- Obrigações regulatórias europeias para sistemas classificados como de alto risco
- Padrões de auditoria e registro aplicáveis a agentes
- O que existe de prática estabelecida sobre alçada e aprovação em sistemas autônomos

**Pronto quando:** cada um dos seis eixos tem pelo menos duas fontes primárias verificadas.

---

## 4. Escrever a parte 3

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

## 5. Consolidar o playbook

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

**Publicação.** Resolvida em 30 de agosto de 2026: GitHub Pages ativo em `tecosodreaboutdigital.github.io/harness-medir`. Verificar depois do primeiro build automático se os quatro documentos renderizam corretamente lá (o link mais provável de precisar ajuste é algum caminho relativo entre eles).
