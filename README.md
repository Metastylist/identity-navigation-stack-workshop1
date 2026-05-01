# Identity Navigation Stack
## Workshop 1: Reading the Field

This repository contains all materials for the first workshop in the **Identity Navigation Stack** series — a set of technical workshops for developers building systems grounded in DMES and Faces architecture.

> Framework: Metastyling Framework (Alice Pau, 2025)  
> Canonical DOI: [10.5281/zenodo.18081055](https://doi.org/10.5281/zenodo.18081055)  
> Reference paper: *How AI Talks to a Human: Structural Homology, Field Cartography, and a New Measurement Paradigm for Identity* (Pau, 2025)

---

## About the author

This system was designed by Alice Pau, Navigation Architect working with identity as a dynamic field.

---

## What this is

This is Workshop 1 in the Identity Navigation Stack series — a set of technical workshops for developers building systems grounded in DMES and Faces architecture.

Before a navigation system can work, it needs a map of the field. This workshop builds the data collection layer: a system that reads identity topology through conversation — not through questionnaires or self-report.

If your system is not built on DMES and Faces as its foundation, this workshop is not for you. If it is — this is where navigation starts.

The architecture you leave with:
- Reads structural patterns above response content
- Accumulates topographic evidence across a session
- Knows what it doesn't know yet (uncharted zones)
- Knows when the map is ready (Duality Principle)

---

## Workshop structure

| Block | Duration | Focus | Output |
|-------|----------|-------|--------|
| 1 — Ontological Shift | 45 min | Query-response vs. topographic logic | See the difference in your own questions |
| 2 — Signal Layer | 60 min | Reading DMES patterns above content | Signal reading vocabulary |
| 3 — System Architecture | 90 min | Prompt, schema, probe algorithm, stopping criterion | Working architecture |
| 4 — Live Build | 60 min | Real prototype with real subject | MVP identity cartographer |

---

## Repository structure

```
metastyling-cartography-workshop/
│
├── README.md
│
├── workshop/
│   ├── block1_ontological_shift.md    # Exercise + theory minimum
│   ├── block2_signal_layer.md         # Transcript exercises + answer keys
│   ├── block3_architecture.md         # Technical walkthrough
│   └── block4_live_build.md           # Build instructions + debrief
│
├── system/
│   ├── system_prompt.md               # Full cartographer system prompt
│   ├── schema.json                    # Topographic session state schema
│   └── cartographer.py               # Anthropic API wrapper (dual-channel)
│
├── transcripts/
│   ├── kendall.md                     # Signal exercise: D-vector gap
│   ├── shiv.md                        # Signal exercise: E concealing S
│   └── roman.md                       # Signal exercise: play mode as defense
│
└── handouts/
    ├── dmes_reference.md              # One-pager: vectors, modes, criterion
    ├── signal_reading.md              # Signal reading cheat sheet
    └── json_template.md              # Blank session state for live build
```

---

## Quick start (Block 4 / live prototype)

```bash
pip install anthropic
```

```python
# Set your API key
export ANTHROPIC_API_KEY=your_key_here

# Run the cartographer
python system/cartographer.py
```

The terminal shows dual-channel output:
- **Left / JSON** — internal topographic state (developer view)
- **Right / text** — what the system says to the user

---

## Key concepts

**Face** — an attractor configuration in the identity field. Not a personality type. A recurring pattern of how a person shows up, orients, and moves. Crystallises across repeated observations, not from a single response.

**DMES** — four coordinates of any Face configuration:
- **D** Direction — gravitational pull of the field
- **M** Meaning — what carries weight, what is avoided
- **E** Expression — how the field presents itself
- **S** State — current activation depth

**Cartographic Window** — the operating condition where topology becomes observable: fluctuation (ξ) above threshold, attractor depth (β) below ceiling. Too stable: field stays closed. Too mobile: field shuts down.

**Duality Principle** — the map is complete when every major Face has a localised structural counterpart (antipode). MVP criterion: minimum 2 Faces, 1 confirmed across blocks, 1 antipode hypothesis, all DMES partially covered.

**Nelson Reversal** — the cartographic conversation moves in reverse developmental order: from narrative → choices → conflict → pressure → future simulation. Each block reaches deeper into the field.

---

## Extending the MVP

The architecture is subject-agnostic. To map a company instead of a person:
- Replace DMES signal definitions with organisational equivalents
- Adjust block scenarios to surface institutional attractors
- Keep the schema and probe logic unchanged

The same principle applies to teams, products, or any system with attractor dynamics.

---

## License

MIT — use freely, attribution appreciated.

If you publish work built on this architecture, please cite:  
Pau, A. (2025). *How AI Talks to a Human: Structural Homology, Field Cartography, and a New Measurement Paradigm for Identity.* Metastyling Series.
