# D3 · Where the order enters inside the data

*Working directory, not reader-facing.* The Mermaid sketch is the plain-text plan a diagram is drawn from. Per `STANDARDS.md`, change this file first, then redraw `../part3/d3-order-inside-the-data.svg` by hand to match. Labels below are the published ones.

**Purpose.** Explain, without jargon, why instruction injection is architecture and not configuration. The hardest diagram to get right and the most valuable in the piece.

**Where it goes.** Part 3, section 5.

```mermaid
flowchart TD
    subgraph TRUSTED["TRUSTED ZONE"]
        A["Task contract"]
        B["Own guides and skills"]
    end
    subgraph UNTRUSTED["UNTRUSTED ZONE"]
        C["Email, PDF, web page"]
        D["External system response"]
        E["Third-party skill"]
        G["Document sent by a customer"]
    end
    A --> T
    B --> T
    C --> T
    D --> T
    E --> T
    G --> T
    T["SINGLE STREAM OF SYMBOLS<br/>no reliable marking separates<br/>command from data"]
    T --> Z["PROPOSED ACTION"]
```

**Rendering note.** The two zones stay visually apart until the point of convergence, and the funnel has to be obvious.

**Caption.** THE BOUNDARY EXISTS IN YOUR DIAGRAM, NOT INSIDE THE MODEL.
