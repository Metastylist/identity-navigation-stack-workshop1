# Block 3 — System Architecture
### Identity Navigation Stack — Workshop 1: Reading the Field
### Duration: 90 min

---

## What this block does

Block 1 gave you the shift. Block 2 gave you the vocabulary.  
Block 3 gives you the architecture.

By the end of this block you will have a working system — not a concept, not a diagram.  
A running prototype that reads a topographic model through a live conversation.

**Materials needed:**
- `system/system_prompt.md`
- `system/schema.json`
- `system/cartographer.py`
- `handouts/dmes_reference.md`
- Python 3.9+ and Anthropic API key

**Setup before this block:**
```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
```

---

## Architecture overview

The system has four layers. Each layer answers one question.

| Layer | Question | File |
|-------|----------|------|
| **Data model** | What does the system accumulate? | `schema.json` |
| **Signal reading** | What does the system notice? | `system_prompt.md` §2 |
| **Probe logic** | What does the system do next? | `system_prompt.md` §3 + `cartographer.py` |
| **Stopping criterion** | When does the system stop? | `system_prompt.md` §5 + `cartographer.py` |

We build bottom-up: data model first, then signal reading, then probe logic, then stopping criterion. The system prompt and cartographer.py assemble all four into running behaviour.

---

## Level 1 — Data model (20 min)

Open `schema.json`.

The schema defines what the system accumulates across a session. Every field exists for a reason. Walk through the key structures:

### field_state
```json
"field_state": {
  "xi": 0.4,
  "beta": 0.6,
  "xi_signals": ["length changed sharply between turns 3 and 4"],
  "beta_signals": ["returned to same frame after scenario in turn 5"]
}
```

**ξ (xi)** — stochastic fluctuation. How much is the field being perturbed right now?  
**β (beta)** — attractor depth. How strongly does the current configuration resist change?

These two values determine which mode the system operates in — and together they define whether the cartographic window is open.

```
Cartographic window = ξ > threshold AND β < ceiling
```

Below threshold: field too stable, conversation produces narrative not topology.  
Above ceiling: field too mobile, subject closes or deflects.  
The system works in the space between.

**Discussion question:** what would produce high ξ in a real conversation? What would produce high β?  
*(Expected answers — ξ: sharp length changes, topic shifts, deflection. β: rationalisation of contradictions, return to dominant frame, narrative escape from scenario.)*

---

### dmes
```json
"direction": {
  "hypothesis": "moves toward recognition within legacy structures despite narrating liberation from them",
  "confidence": 0.85,
  "signals": [
    "advised another person to take institution — inverse of own stated choice",
    "could not sustain invisibility scenario even while performing acceptance of it",
    "final turn: primary audience for success is Logan, not market"
  ]
}
```

Three things to notice:

**Hypothesis is in the system's own words** — an interpretation, not a quote. The system reads pattern above content.

**Confidence accumulates across turns** — starts at 0.0, rises as signals confirm the hypothesis across different contexts. A signal in one context is a glimpse. The same signal across three contexts is topology.

**Signals are structural readings** — not "he said X" but "the field did Y when Z condition was present."

---

### faces
```json
{
  "id": "face_2",
  "label": "The Son Seeking Recognition",
  "confirmed_across_blocks": ["conflict", "future"],
  "antipode_hypothesis": "invisibility without witness"
}
```

A Face is **confirmed** when it appears in 2+ blocks. This is the invaraint test — not what the person said once, but what persists across varied conditions.

`antipode_hypothesis` is the field's shadow — the configuration it routes around. Required for duality. Null until localised.

---

### completeness
```json
"completeness": {
  "faces_found": true,
  "face_confirmed": true,
  "duality_satisfied": true,
  "all_dmes_partial": true,
  "ready_to_map": true
}
```

Four binary conditions. All four true = `ready_to_map`. At that point the system's next move is not a probe — it is the map.

**Exercise (5 min):** open a blank copy of `handouts/json_template.md`. Fill in a hypothetical INNER_STATE after 3 turns with a person you know — real or fictional. What would you have by turn 3? What would still be null?

---

## Level 2 — Signal reading (15 min)

Open `system_prompt.md`, Section 2.

The system prompt tells the model what to notice. Not "ask open questions" — that produces better chatbot behaviour, not topographic behaviour. Instead: four precise definitions of what each vector looks like in language.

Read the Direction definition aloud:

```
DIRECTION (D): Where does this person's field pull toward?
Not what they say they want — what they move toward when
narration is temporarily unavailable. Read it in:
- choices under mild pressure (not declarations)
- what they approach vs. avoid when both are available
- the gap between stated values and revealed preferences
```

Three things to notice about this instruction:

**"When narration is temporarily unavailable"** — this is the function of the probe. The probe creates a moment where the person cannot simply narrate. They must choose, imagine, or respond to a scenario. The field becomes briefly visible through the movement.

**"Not declarations"** — self-report is excluded by design. The system is not asking who the person is. It is watching what they do when the question is structural, not personal.

**"The gap"** — the system is explicitly looking for discrepancy. Not inconsistency as error, but as topographic data. Where choice and justification diverge: that is the signal.

---

## Level 3 — Probe logic (20 min)

Open `system_prompt.md`, Section 3. Then open `cartographer.py`, function `choose_next_probe`.

The probe selection algorithm has three steps:

### Step 1 — Select mode from field_state
```python
if xi < XI_THRESHOLD:
    mode = "narrative"      # field too stable, follow movement
elif beta > BETA_CEILING:
    mode = "narrative"      # field too mobile, reduce pressure
else:
    mode = "targeted"       # window open, intervene precisely
```

Play mode activates when β > 0.5 OR when conflict block is active — the scenario is a mechanism for reducing defensive β while maintaining ξ.

### Step 2 — Select target from uncharted zones
```python
target_vector = min(
    ["direction", "meaning", "expression", "state"],
    key=lambda v: dmes[v]["confidence"]
)
```

The system always targets the vector with the lowest confidence. The probe is a hypothesis about the most uncertain part of the map — not a general invitation to keep talking.

### Step 3 — Check for antipode
```python
needs_antipode = any(
    f["antipode_hypothesis"] is None for f in faces
)
```

When Faces are confirmed but no antipode is localised, the next probe is designed to surface the shadow — the configuration the field routes around. This is often done through a pressure or future simulation scenario.

**Critical distinction:**  
The probe is not written by this algorithm. The algorithm produces a `probe_instruction` — a directive to the model about what the next move should accomplish and why. The model writes the actual probe in natural language. The instruction is the hypothesis; the probe is the expression.

**Discussion question:** what is the difference between a probe and a question? Write one example of each targeting the same uncharted zone.  
*(Expected: a question requests information. A probe activates a configuration. "What do you value?" is a question. "You have two offers, same money — one is yours to build, one is safer. End of day decision." is a probe.)*

---

## Level 4 — Stopping criterion (10 min)

Open `system_prompt.md`, Section 5. Then `cartographer.py`, function `check_completeness`.

```python
def check_completeness(state):
    faces_found     = len(faces) >= 2
    face_confirmed  = any(len(f["confirmed_across_blocks"]) >= 2 for f in faces)
    duality_satisfied = any(f["antipode_hypothesis"] is not None for f in faces)
    all_dmes_partial  = all(dmes[v]["confidence"] > 0.2 for v in ["direction","meaning","expression","state"])
    ready = all([faces_found, face_confirmed, duality_satisfied, all_dmes_partial])
```

The system does not stop after a fixed number of turns. It stops when the map has structural completeness — minimum viable topology, not exhaustive coverage.

**Why Duality?**  
A map of only dominant Faces is a flattering portrait. The antipode — the configuration the field suppresses — is what gives the map its structural honesty. Without it the cartographer is producing a mirror, not a map.

When `ready_to_map` is true, the system's next output is not a probe. It is the map presentation — written according to the format in Section 5 of the system prompt.

---

## Assembly — running the system (25 min)

Open a terminal.

```bash
python system/cartographer.py
```

The system opens with the cartographer's first move — no greeting, no preamble. It invites the person to start wherever they want.

**What you see in the terminal:**

```
════════════════════════════════════════════════════════════
  INNER STATE — Turn 1
════════════════════════════════════════════════════════════
  Block:  narrative
  Mode:   narrative
  ξ: 0.2   β: 0.1

  DMES confidence:
  D  [░░░░░░░░░░] 0.0  —
  M  [░░░░░░░░░░] 0.0  —
  E  [░░░░░░░░░░] 0.0  —
  S  [░░░░░░░░░░] 0.0  —

  Faces found: 0
  Uncharted zones:
  · all vectors — no signal yet
════════════════════════════════════════════════════════════

────────────────────────────────────────────────────────────
  CARTOGRAPHER →
────────────────────────────────────────────────────────────

  I'm not going to ask you who you are. Tell me about
  something you've been working on lately — or something
  you've been thinking about. Wherever you want to start.

────────────────────────────────────────────────────────────
```

**Run 3–5 turns with yourself as subject.** Type real answers — not test inputs. The system needs real language to produce real signals.

Watch the INNER STATE panel after each turn:
- When does ξ start moving?
- When does a D-hypothesis first appear?
- When does mode shift from narrative to targeted?
- What does the system target first and why?

**Discuss in pairs (5 min):** where did the system behave as a cartographer? Where did it behave as a mirror — reflecting content rather than reading structure?

---

## What you leave Block 3 with

A running prototype. Four layers assembled into a system that:
- Reads structural patterns above response content
- Accumulates evidence across turns into a growing topographic model
- Selects its next move based on what it does not yet know
- Knows when the map is ready and presents topology, not summary

Block 4 will run this system with a real subject for 8–10 turns and produce a first map.

The architecture does not change in Block 4. What changes is that the subject is real, the signals are unpredictable, and you will see exactly where the theory meets its limits.

---

*Identity Navigation Stack · Workshop 1: Reading the Field*  
*Framework: Metastyling Framework, Alice Pau (2025) · DOI: 10.5281/zenodo.18081055*
