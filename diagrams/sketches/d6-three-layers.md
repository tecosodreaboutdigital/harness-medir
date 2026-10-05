# D6 · The three layers of the framework

*Working directory, not reader-facing.* The Mermaid sketch is the plain-text plan a diagram is drawn from. Per `STANDARDS.md`, change this file first, then redraw `../part4/d6-three-layers.svg` by hand to match. Labels below are the published ones.

**Purpose.** Place the reader in the whole and show there are only three layers, crossed by a single ruler. The closing diagram of the whole series.

**Where it goes.** Part 4, section 1.

```mermaid
flowchart TD
    subgraph L3["GOVERNANCE · AGENT OFFICE"]
        G["How many exist, who owns each one,<br/>which ones still pay for themselves"]
    end
    subgraph L2["OPERATION · SEPARATION OF POWERS"]
        O["What it can do,<br/>and who answers for it"]
    end
    subgraph L1["BUILD · THE MEDIR CYCLE"]
        C["How you build<br/>a reliable agent"]
    end
    L1 --> L2 --> L3
    N["TIERS N0 TO N3<br/>the one ruler shared across all three layers"]
    N -.-> L1
    N -.-> L2
    N -.-> L3
```

**Rendering note.** Three stacked layers and the ruler as a vertical element touching all three. The ruler touching all three is the message: it is the only shared vocabulary, and what keeps the framework from becoming three loose things.

**Caption.** THE ONE RULER SHARED ACROSS ALL THREE LAYERS.
