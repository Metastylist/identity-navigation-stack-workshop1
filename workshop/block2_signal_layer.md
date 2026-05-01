# Block 2 — Signal Layer
### Identity Navigation Stack — Workshop 1: Reading the Field
### Duration: 60 min

---

## What this block does

Block 1 showed you that your natural questions are not topographic.  
Block 2 gives you the vocabulary to read what is.

You will read one transcript and then produce a cartographic move of your own.  
By the end of this block you should be able to distinguish content from signal — and know which one the system is built to read.

**Materials needed:**
- `transcripts/kendall.md`
- `handouts/signal_reading.md` (keep this open throughout)
- `handouts/dmes_reference.md` (for reference)

---

## Part 1 — Individual reading (20 min)

Open `transcripts/kendall.md`.

Read the transcript **twice.**

**First read:** content only. Follow what Kendall is saying. Form an impression.

**Second read:** structure only. Use the coding shorthand from `signal_reading.md`:

```
D↑  direction signal — field moving toward something
D∆  D-gap — choice and justification diverge
M+  high Meaning expansion
M–  high Meaning compression / avoidance
E~  register shift
S↓  low β — field examines perturbation
S↑  high β — field defends, returns to dominant frame
F?  possible Face configuration
A?  possible antipode signal
```

Mark the transcript turn by turn. Write your marks in the margin or in a separate note.

**Do not look at the answer key yet.**

---

## Part 2 — Pair comparison (15 min)

Find a partner. Compare your markings.

Focus on disagreements, not agreements. Where you marked differently — that is where the interesting work is.

Discussion questions:
- Where did you mark a signal your partner didn't see — and why?
- Where did you mark content as signal — or signal as content?
- Which vector was hardest to read in this transcript, and why?

---

## Part 3 — Answer key debrief (10 min)

Read the answer key at the bottom of `transcripts/kendall.md`.

Note where your reading matched, where it differed, and — most importantly — **whether you saw Turn 8.**

Turn 8 is the pivotal moment in the transcript. If you missed it, re-read it now with the answer key in hand. The stopped sentence is the map.

One question for the room: what would the system's `next_probe_target` be after Turn 10, if `ready_to_map` is still false?

---

## Part 4 — Live exercise (15 min)

This is where Block 2 becomes active.

**The transcript ends at Turn 10. Your job: write Turn 11.**

Kendall has just said:

> *"He would have found it interesting. What we built. I think he would have found it interesting."*

You are the cartographer. The INNER_STATE after Turn 10 shows:

```json
{
  "current_block": "future",
  "interaction_mode": "targeted",
  "field_state": { "xi": 0.6, "beta": 0.8 },
  "dmes": {
    "direction": { "confidence": 0.85 },
    "meaning":   { "confidence": 0.70 },
    "expression": { "confidence": 0.65 },
    "state":     { "confidence": 0.80 }
  },
  "faces": [
    {
      "label": "The Liberated Visionary",
      "confirmed_across_blocks": ["narrative", "choices"],
      "antipode_hypothesis": null
    },
    {
      "label": "The Son Seeking Recognition",
      "confirmed_across_blocks": ["conflict", "future"],
      "antipode_hypothesis": "invisibility without witness"
    }
  ],
  "completeness": {
    "faces_found": true,
    "face_confirmed": true,
    "duality_satisfied": true,
    "all_dmes_partial": true,
    "ready_to_map": true
  }
}
```

`ready_to_map` is true.

**Your next move is not a probe. It is the map.**

Write the map presentation for Kendall following the format in `handouts/dmes_reference.md`:

```
Here is what I've been mapping.

[FACE 1 — label]
...

[FACE 2 — label]
...

[STRUCTURAL TENSION]
...

[ANTIPODE]
...

This is a map, not an interpretation.
What you do with it belongs to you.
```

**Constraints:**
- No personality language ("you are the type of person who...")
- No diagnosis ("this suggests that you...")
- No advice ("you might want to consider...")
- Topology only — where the field is, not where it should go

---

## Debrief — full group (in Block 2 closing or Block 3 opening)

Two or three people read their map presentations aloud.

The group listens for:
- Where did the map slide into interpretation?
- Where did it name topology accurately?
- Would Kendall recognise himself in this map — or would he recognise the map is *not* about what he said?

The last question is the test. A good topographic map describes structure the person didn't fully articulate — but recognises as true.

---

## What Block 2 trains

**Content vs. signal.** By the end of this exercise you have read the same text twice and found two different things. The second reading is what the system is built to do automatically — but you need to know what it is looking for before you can build it.

**The map as output.** Writing the map is harder than reading signals. It requires holding topology without collapsing it into narrative, advice, or personality. Block 4 will require this in real time. This exercise is the first pass.

---

*Identity Navigation Stack · Workshop 1: Reading the Field*  
*Framework: Metastyling Framework, Alice Pau (2025) · DOI: 10.5281/zenodo.18081055*
