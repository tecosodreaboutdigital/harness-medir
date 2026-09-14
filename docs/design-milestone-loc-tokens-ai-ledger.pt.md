# Especificação: milestone-loc-tokens-ai-ledger

Documento de trabalho interno do harness-medir, não é conteúdo publicado da série. Escrito em 13 de setembro de 2026, ao fim de uma sessão de brainstorming completa (quatro blocos apresentados e aprovados, mais duas rodadas de refinamento). Descreve um repositório público que ainda não existe.

## 1. Origem e relação com o harness-medir

Este projeto nasce do item 5 de `NEXT-STEPS.md` (extrair o motor de métrica do diário de bordo para uma skill própria), depois de duas rodadas de pesquisa real que mudaram e validaram o escopo:

- `docs/research-logbook-skill-extraction.pt.md`: buscou em cinco eixos (governança de decisão de agente, contadores de LOC, rastreadores de custo de token, geradores de changelog, comparadores de preço entre provedores) se algum repositório GitHub maduro já resolvia isso, pra decidir entre fork, combinação de peças, ou construção própria. Conclusão verificada: nenhum candidato cobre a combinação central, a recomendação é construir do zero, estendendo o motor já validado deste repositório.
- `docs/research-agent-skill-install-paths.pt.md`: verificou, contra a documentação oficial de cada fornecedor, como Claude Code, Cursor, Codex CLI, Gemini CLI, Google Antigravity e VS Code (via GitHub Copilot) carregam uma skill instalável. Confirmou que "Agent Skills" (`agentskills.io`) é um padrão aberto real, com adoção nomeada por cada um desses fornecedores na própria documentação deles, não uma convergência de pasta por acidente.

O repositório nasce como projeto público próprio, separado do monorepo do harness-medir, no mesmo padrão já usado pelo `intake-briefing`: diretório local irmão, git próprio, publicado depois em `github.com/tecosodreaboutdigital/`.

## 2. O que o v1 entrega, eixo por eixo

Escopo deliberadamente contido (YAGNI), mapeado contra os cinco eixos da pesquisa:

| Eixo | Tratamento no v1 |
|---|---|
| LOC e palavras produzidas | Completo. Extensão direta e generalizada do motor já provado no harness-medir |
| Custo e uso de token de LLM | Completo, com o refinamento do histórico de preço datado (seção 6) |
| Marco de projeto e changelog | Completo. É o próprio painel HTML publicado |
| Governança de decisão de agente | Leve. Um campo opcional de uma linha por marco, sem subsistema de ADR separado |
| Comparação entre provedores de LLM | Leve, mas real. A mesma tabela de preço multi-linha permite recalcular o mesmo consumo sob qualquer provedor ou data já registrados, sem tela nova |

**Fora de escopo do v1, deliberadamente:** leitores de transcript para ambientes além do Claude Code (ponto de extensão documentado, nunca alegação de suporte não verificado); qualquer recurso de agregação entre múltiplos membros de um time (a pesquisa de segurança desta sessão não pediu isolamento por pessoa, só por projeto e por máquina); qualquer chamada de rede em tempo de execução da página publicada.

## 3. Por que construir do zero, e não fork ou combinação de peças

Decisão já tomada e verificada em `docs/research-logbook-skill-extraction.pt.md`. Resumo: `boyter/scc` chega mais perto (LOC + HTML + estimativa de custo de LLM) mas erra o requisito central (custo hipotético de regeneração, não real; preço só configurável por flag de build, nunca na página publicada). `simonw/llm-prices` já tem o mecanismo exato de preço editável com recálculo ao vivo, mas é trivial de reimplementar e não lida com marco de projeto. Nenhuma combinação das peças existentes produz menos trabalho do que escrever direto, porque as arquiteturas são opostas entre si (CLI/servidor de um lado, gerador de HTML sem noção de token do outro).

## 4. Estrutura do repositório

```
milestone-loc-tokens-ai-ledger/
├── SKILL.md                 Claude Code / Agent Skills, entrada da skill
├── AGENTS.md                protocolo de máquina, mesmo molde do harness-medir
├── llms.txt                 índice de descoberta
├── README.md                visão geral, matriz de instalação, origem
├── LICENSE                  MIT
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── engine/
│   ├── generate_metrics.py  o motor, generaliza generate_logbook_metrics.py
│   ├── update_prices.py     apensa entradas novas em prices.json, nunca sobrescreve
│   ├── config.example.json  globs de arquivo, nome da pasta de marco, leitor de transcript
│   ├── prices.json          livro-razão de preço, multi-provedor, multi-data, multi-fonte
│   └── readers/
│       └── claude_code.py   único leitor de transcript completo no v1
├── template/
│   ├── dashboard.html       o painel estático
│   └── dashboard.js         gráficos, tabela de marco, painel de preço, tudo client-side
└── logbook/                 o próprio diário de bordo deste repositório, ver seção 9
```

Sem `.pt.md` nem `.es.md` em nenhum arquivo. Todo o conteúdo nasce e permanece em inglês nativo, sem travessão, decisão explícita desta sessão que distingue este repositório do próprio harness-medir (trilíngue por ser conteúdo editorial) e ajusta a prática que o `intake-briefing` de fato segue hoje (que tem traduções PT/ES): esta skill nova não carrega esse padrão.

## 5. O motor (`engine/generate_metrics.py`)

**Generalização.** Nada de lista fixa de arquivo. Tudo vem de `config.json`: nome da pasta de marco (`logbook` por padrão, configurável), globs de LOC, globs de palavras, padrões de exclusão, e qual leitor de transcript usar (`claude_code` no v1).

**Bootstrap.** Primeira execução num repositório sem a pasta configurada: cria a pasta com `config.json` de exemplo preenchido, `dashboard.html`/`dashboard.js` copiados do template, e `data.json` vazio. Não exige montagem manual prévia.

**Leitor de transcript, com honestidade de escopo.** Só `readers/claude_code.py` é completo no v1, portando a correção de dedup por `message.id` já validada em produção fora deste repositório. Qualquer outro ambiente listado na matriz de instalação (seção 8) pode instalar e usar a skill para orientar um agente, mas a contagem de token daquele ambiente específico não tem leitor ainda: o `README.md` declara isso explicitamente, nunca por omissão silenciosa.

**As três regras de segurança, concretas:**

1. **Sem vazar dado de máquina local.** Todo campo de string que chega em `data.json` passa por um scrub obrigatório antes de gravar: remove path absoluto, nome de usuário do sistema operacional, hostname, e qualquer trecho bruto de transcript. Só sobrevive número agregado e o texto curto que o próprio usuário escreveu como nota de marco. Formaliza como regra de arquitetura o bug real que o motor original já teve (vazamento de path local) e corrigiu uma vez.
2. **Isolamento entre projetos.** O leitor de transcript localiza sessões pelo caminho completo codificado que o Claude Code usa para nomear a pasta de projeto (não por sufixo de nome, que pode colidir entre dois projetos parecidos, fraqueza real do motor original). Só agrega uso cujo caminho decodificado bate exatamente com o diretório de trabalho atual.
3. **Consistência entre os seis ambientes.** O mesmo `data.json` e o mesmo par `dashboard.html`/`dashboard.js` saem do build não importa qual ambiente disparou o script, porque é sempre o mesmo Python rodando por trás. Rodar o gerador duas vezes sem novidade no meio produz saída idêntica byte a byte, verificado antes de cada commit, mesma disciplina que os builds do harness-medir já seguem.

## 6. Dados: marco e preço

**`data.json`, um registro por marco:**

```json
{
  "date": "2026-09-13",
  "commit": "a1b2c3d",
  "subject": "Bootstrap the metrics folder",
  "loc_delta": 240,
  "words_delta": 0,
  "tokens": {"input": 18400, "output": 3200, "cache_read": 91000, "cache_creation": 4100},
  "cost_recorded": {"amount": 0.87, "currency": "USD", "priced_at": "2026-09-13", "provider": "anthropic", "model": "claude-sonnet-5"},
  "note": "Marco opcional de decisão, uma linha, eixo de governança leve"
}
```

`cost_recorded` é calculado uma única vez, no momento em que o marco é gerado, usando a entrada de `prices.json` com a data mais recente até aquela data, e depois **nunca recalculado retroativamente**, mesmo que o preço mude no futuro. O passado fica registrado no momento em que aconteceu.

**`prices.json`, livro-razão apensado, nunca sobrescrito:**

```json
{
  "provider": "anthropic", "model": "claude-sonnet-5", "currency": "USD",
  "entries": [
    {
      "effective_date": "2026-09-13",
      "input_price": 3.00, "output_price": 15.00,
      "cache_read_price": 0.30, "cache_creation_price": 3.75,
      "sources": [
        {"name": "Anthropic pricing page", "url": "https://www.anthropic.com/pricing", "checked_at": "2026-09-13"},
        {"name": "litellm model_prices_and_context_window.json", "url": "https://github.com/BerriAI/litellm", "checked_at": "2026-09-13"}
      ]
    }
  ]
}
```

Uma linha especial `provider: "custom"` cobre modelo on-premise ou local: preços zerados por padrão, com um comentário convidando o usuário a preencher seu próprio custo (energia, amortização de hardware) ou deixar zero para inferência sem custo direto atribuído.

`engine/update_prices.py` sempre apensa uma entrada nova quando o preço muda, checando pelo menos duas fontes independentes na mesma rodada e registrando as duas, mesmo quando concordam. Se divergirem, ambas ficam gravadas, sem escolher uma calada. Rodado pelo mantenedor, nunca automaticamente pela página publicada.

## 7. O painel (`dashboard.html` / `dashboard.js`)

Dois gráficos SVG empilhados (nunca eixo duplo, mesma regra que `docs/logbook.html` já segue): esforço (palavras e linhas) e tokens, ao longo dos marcos. Tabela de marco abaixo, mostrando a nota de decisão quando existir (eixo de governança, seção 2).

**Painel de preço, dois modos que não devem ser confundidos:**

- **Custo registrado** (o `cost_recorded` de cada marco): mostrado por padrão na tabela, imutável, é o que o eixo custou de verdade, no preço vigente naquele dia.
- **Recálculo ao vivo**: um seletor de provedor/modelo/data pré-popula os quatro campos de preço com qualquer entrada do livro-razão (histórica ou mais recente, de qualquer provedor), cada campo continua editável num `<input type="number">`, e o custo de qualquer marco recalcula na hora em JS puro. Isso cobre o eixo 5 (outro provedor) e uma pergunta adicional que só existe por causa do livro-razão datado: quanto o mesmo trabalho custaria hoje, no preço de hoje. Nenhuma chamada de rede sai da página publicada em nenhum dos dois modos; a tabela de preço é embutida no build.

Preferência de seleção (qual provedor, qual data) salva só em `localStorage` do visitante, conveniência, nunca sincronizada, nunca fonte de verdade.

Rodapé discreto: "metrics engine originated in the harness-medir project", com link.

## 8. Matriz de instalação

Verificada em 13/09/2026 contra a documentação oficial de cada fornecedor (`docs/research-agent-skill-install-paths.pt.md`), reproduzida no `README.md` do repositório novo com a mesma data de verificação declarada.

| Ambiente | Caminho | Ressalva |
|---|---|---|
| Claude Code | `.claude/skills/milestone-loc-tokens-ai-ledger/` (projeto), `~/.claude/skills/...` (pessoal), ou plugin via `.claude-plugin/` | Nenhuma |
| Cursor | `.cursor/skills/...` ou `.agents/skills/...` (projeto e pessoal) | Também lê `AGENTS.md` na raiz como alternativa a `.cursor/rules` |
| Codex CLI | `AGENTS.md` hierárquico (`~/.codex/AGENTS.md` até o diretório atual); skills em `.agents/skills/...` | Nenhuma |
| Gemini CLI | `GEMINI.md`; `.gemini/skills/...` ou `.agents/skills/...` | Produto standalone parou de atender contas free, Pro e Ultra desde 18/06/2026, substituído pela Antigravity CLI. Só licença corporativa Gemini Code Assist mantém acesso |
| Google Antigravity | `.agents/skills/...` (projeto, confirmado e consistente) | Caminho pessoal não afirmado: três páginas oficiais do próprio fornecedor documentam três strings diferentes. README declara "a confirmar", não escolhe um palpite |
| VS Code (via GitHub Copilot) | `.github/skills/`, `.claude/skills/` ou `.agents/skills/` (Agent Skills); `.github/copilot-instructions.md` (clássico) | A extensão do Claude Code dentro do VS Code segue o veredito da primeira linha desta tabela |

## 9. O repositório se autotesta

`milestone-loc-tokens-ai-ledger` roda o próprio motor contra o próprio histórico de git e a própria sessão de desenvolvimento, publicando seu próprio `logbook/` dentro do repositório, não um exemplo hipotético separado. `README.md` aponta pra ele como prova de funcionamento, mesma disciplina que a seção "This project also inspects itself" já aplica no harness-medir. Um bug no motor aparece primeiro no próprio marco do criador, antes de qualquer usuário externo encontrar.

## 10. Documentos da skill

- **`SKILL.md`.** Regra não negociável, no molde do `intake-briefing`: nenhum número entra sem uma fonte contada de verdade, e nenhum detalhe da máquina local sai no que é publicado.
- **`AGENTS.md`.** Protocolo de máquina no formato já usado pelo harness-medir (red flags, passos de verificação, seção Never), com uma regra herdada explicitamente: a matriz de instalação e o livro-razão de preço carregam data de verificação, não são estado ao vivo, checar a fonte antes de confiar. O caso do Gemini CLI descontinuado é citado como o motivo concreto dessa regra existir.
- **`README.md`.** Visão geral, a matriz da seção 8, a seção Origin creditando o harness-medir (mesma fórmula do `intake-briefing`), e a seção "This repository logs itself" apontando pro `logbook/` real.
- **`llms.txt`** e **`.claude-plugin/`** (`plugin.json`, `marketplace.json`): mesmo par de arquivos do `intake-briefing`, adaptado ao nome novo.

## 11. Onde o repositório vive, localmente

`Dropbox\negocios parcerias e clientes\AboutDigital\milestone-loc-tokens-ai-ledger\`, irmão do `harness-medir`, git próprio e independente desde a criação, mesmo padrão do `intake-briefing`. Justificativa registrada na conversa: o próprio produto exige projetos de verdade, separados, pra que a Regra 2 (isolamento entre projetos) e o autoteste da seção 9 façam sentido, e um repositório público não deve viver como subpasta de outro.

Eu crio o diretório e todos os arquivos descritos aqui.

## 12. Integração de volta ao harness-medir, depois de pronto

Só depois que o repositório novo existir, tiver rodado o próprio autoteste com sucesso, e estiver publicado no GitHub: integrar como uma skill própria deste projeto, mesmo tratamento do `intake-briefing` hoje.

- `TOOLS.md`: entrada nova na lista de skills que este projeto produziu e usa.
- `sources/inventory.md`: entrada com origem, status e data de verificação.
- `toolkit.json`: nova entrada `kind: "own_skill"`, mesma forma da entrada do `intake-briefing`.
- `harness-toolkit.html`: card novo no guia compacto, três idiomas.
- Opcional: cópia não versionada em `harness-medir\.claude\skills\milestone-loc-tokens-ai-ledger\`, pra uso local como skill instalada aqui, mesmo padrão do `intake-briefing`.

Não fazer isso antes da hora. Listar uma skill que ainda não existe ou não foi verificada violaria a própria regra que o `AGENTS.md` deste repositório aplica a qualquer outra curadoria.

## 13. Riscos e questões em aberto

- **Antigravity, caminho pessoal.** Não usar nenhuma das três strings encontradas sem reconferir a documentação oficial primeiro, ela pode ter se resolvido sozinha até a implementação acontecer.
- **Gemini CLI, descontinuação.** O aviso registrado na seção 8 tem validade a partir de 13/09/2026. Reconferir se a transição para Antigravity CLI mudou de data ou de escopo antes de publicar.
- **Leitores de transcript além de Claude Code.** Ponto de extensão documentado, não implementado. Um contribuidor externo pode trazer um leitor novo, mas este projeto não deve alegar suporte a nenhum ambiente que não testou.
- **Fonte de preço para atualização periódica.** `update_prices.py` precisa de pelo menos duas fontes públicas por provedor. Para provedores menores ou modelos novos, pode não haver uma segunda fonte independente disponível: documentar esse caso como "uma fonte só, sinalizado", nunca inventar uma segunda referência.

## 14. Referências

- `docs/research-logbook-skill-extraction.pt.md` (esta sessão, 13/09/2026)
- `docs/research-agent-skill-install-paths.pt.md` (esta sessão, 13/09/2026)
- `.claude/skills/intake-briefing/` (o precedente estrutural direto)
- `AGENTS.md` do harness-medir (o molde do protocolo de máquina)
