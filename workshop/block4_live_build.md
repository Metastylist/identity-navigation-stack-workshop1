# Block 4 — Live Build
### Identity Navigation Stack — Workshop 1: Reading the Field
### Duration: 60 min

---

## What this block does

Block 3 gave you a running system.  
Block 4 runs it with a real person.

This is where theory meets its limits — and where you learn what the architecture actually does under real conditions. A real subject produces signals the synthetic transcript didn't have: resistance, deflection, unexpected compression, moments where the system loses topographic focus and becomes a mirror.

Seeing that happen in real time is the most valuable part of the workshop.

**Materials needed:**
- `system/cartographer.py` (running)
- `handouts/json_template.md` (one copy per team, printed or open)
- `handouts/signal_reading.md`

---

## Setup (5 min)

Form teams of 3–4 people.

Each team assigns three roles:

| Role | Responsibility |
|------|---------------|
| **Operator** | Types inputs into `cartographer.py`, manages the terminal |
| **Observer** | Watches the INNER STATE panel, tracks the JSON template by hand, flags when system loses focus |
| **Subject** | The person being mapped — answers as themselves, not as a test case |

The Subject does not see the INNER STATE panel during the session.  
The Operator and Observer do.

**One rule for the Subject:** answer as you actually would. Not helpfully, not as a test. If a question feels off — say so. That response is topographic data too.

---

## Live session (30 min)

Run the cartographer for **8–10 turns.**

The system opens with its standard first move. The Subject responds. The Operator reads the response into the terminal. The Observer tracks INNER STATE and fills in `handouts/json_template.md` in parallel.

**Observer checklist — after each turn:**

- [ ] Did ξ change? What caused it?
- [ ] Did β change? What caused it?
- [ ] Which DMES vector gained confidence this turn?
- [ ] Did the system target the right uncharted zone?
- [ ] Is the mode appropriate for the current field state?
- [ ] Is the system behaving as a cartographer or as a mirror?

**Mirror mode** — when to flag it:

The system has slipped into mirror mode when:
- It reflects back what the Subject said without adding topographic movement
- It asks for more information about content rather than probing structure
- It validates or empathises instead of probing
- The INNER STATE is not updating meaningfully between turns

When the Observer flags mirror mode — note the turn number. Do not interrupt the session. Continue. The slip is data for the debrief.

---

## Target for the session

By turn 8–10, aim to have:

| Target | Status |
|--------|--------|
| Minimum 2 Face hypotheses named | ○ |
| At least 1 Face confirmed across 2 blocks | ○ |
| At least 1 antipode hypothesis localised | ○ |
| All DMES vectors partially covered (confidence > 0.2) | ○ |
| `ready_to_map: true` | ○ |

If `ready_to_map` is true — let the system present the map to the Subject.  
If not reached by turn 10 — the Operator presents the partial map from whatever the system has accumulated. Partial maps are valid. Name what is there and what is still uncharted.

---

## Map moment (5 min)

When the map is presented — the Subject hears it and responds with one sentence:

*"What did I recognise, and what surprised me?"*

No discussion yet. One sentence only. Write it down.

This is the first validation signal: does the map describe structure the person didn't fully articulate — but recognises as true?

A good topographic map is not flattering. It is accurate. The Subject may recognise something they weren't expecting to hear named. That recognition is the signal that the system read topology, not narrative.

---

## Debrief — full team (15 min)

Three questions. Work through them in order.

### 1. Where did the system work as a cartographer?

Identify 2–3 specific moments where the probe was topographically targeted — where it moved toward an uncharted zone, activated a configuration, or surfaced something the Subject hadn't narrated.

Look for:
- Turns where DMES confidence jumped
- Turns where a new Face hypothesis appeared
- Turns where the Subject's response produced a signal the system correctly read as high ξ or β

### 2. Where did the system slip into mirror mode?

Identify the moments the Observer flagged. For each:
- What happened in the Subject's input that triggered the slip?
- What did the system do instead of a topographic probe?
- What would the correct next move have been?

This is not a critique of the system prompt. It is a diagnosis of the boundary between the architecture and its limits. Every system has a mirror edge — the point where narrative pressure pulls it toward reflection rather than reading.

### 3. What is the next probe?

The session ended — but the map is not finished. Based on the accumulated INNER STATE:

- What is the largest remaining uncharted zone?
- What is the most uncertain DMES vector?
- Is the antipode fully localised or still a hypothesis?

Write one probe — not a question, a topographic move — that would be the next right step if the session continued.

---

## Full group share (5 min)

One person from each team shares:
- The map they presented (2–3 sentences)
- One moment where the system slipped into mirror mode
- Their next probe

The facilitator listens for a pattern across teams: **where do cartographic systems consistently lose focus?**

Common failure modes:
- **Empathy collapse** — system detects emotional content and shifts to support mode
- **Content elaboration** — Subject adds rich narrative and system follows the content instead of reading the structure
- **Premature closure** — system reaches a confident DMES hypothesis and stops probing that vector before confirming across blocks
- **Antipode avoidance** — system finds two Faces but never moves toward the shadow configuration because the Subject's β is high there

Name which failure mode appeared in your session.

## Validation criteria — did the map work?
A map is not valid because the system produced it. It is valid because of what happens when the Subject hears it.

Four criteria to check after map presentation:

**1. Recognition from within**
The Subject recognises themselves in the map — not because they were told what it means, but because it activates something they already inhabit. The signal is: "yes, that's me" — not "I suppose that's accurate."
**2. Surprise at one element**
At least one element of the map reveals a configuration the Subject had not consciously held. Surprise — not confusion, not resistance — means the cartography reached below the narrative layer.
**3. Resistance at the antipode**
The Subject resists the antipode or shadow Face. "That's not who I am" is the correct response — it means the shadow has been correctly localised. Full acceptance of the antipode would mean it was not a real shadow.
**4. The map is not advice**

After hearing the map, the Subject does not ask "so what should I do?" — or if they do, the cartographer can honestly say: "That belongs to you. The map shows where you are. Navigation is yours."
If criteria 1 and 2 are met — the session worked.
If criterion 3 is met — the Duality Principle was correctly applied.
If the Subject immediately asks for advice — the map collapsed into interpretation somewhere. Find where.

---

## What you leave Block 4 with

A working MVP — the `cartographer.py` prototype running the full architecture — and a first-hand experience of where it works and where it doesn't.

The gap between Block 3 and Block 4 is not a flaw. It is the research question.  
Every place the system slipped into mirror mode is a place the architecture can be refined.

---

## Extending the MVP

The architecture you built today is subject-agnostic. The DMES vectors and Face logic apply to any system with attractor dynamics.

To map a **company** instead of a person:
- Redefine D as organisational gravitational pull — what the institution moves toward when strategy is unavailable
- Redefine M as institutional meaning — what the organisation elaborates in its culture vs. what it compresses
- Redefine E as how the organisation presents itself externally vs. internally
- Redefine S as current activation state — stability, crisis, transition
- Adjust probe scenarios to surface institutional choices under pressure

The schema, the probe logic, the stopping criterion — unchanged.

The same extension applies to teams, products, or any system you can have a conversation with or about.

---

## What comes next

This workshop built the data collection layer — the system that reads the field and produces a primary configuration.

The Identity Navigation Stack continues:

| Workshop | Focus |
|----------|-------|
| **Workshop 1: Reading the Field** ← *you are here* | Primary configuration — mapping the topology |
| Workshop 2 *(forthcoming)* | Navigation design — building on the map |
| Workshop 3 *(forthcoming)* | Dynamic tracking — updating the map over time |

The map you built today is the foundation everything else is built on.

---

*Identity Navigation Stack · Workshop 1: Reading the Field*  
*Framework: Metastyling Framework, Alice Pau (2025) · DOI: 10.5281/zenodo.18081055*
