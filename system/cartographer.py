"""
Identity Navigation Stack — Workshop 1: Reading the Field
cartographer.py — Anthropic API wrapper with dual-channel output

Usage:
    pip install anthropic
    export ANTHROPIC_API_KEY=your_key_here
    python cartographer.py

Output:
    Terminal left  — INNER_STATE (JSON, developer view)
    Terminal right — PROBE (text, user view)

Framework: Metastyling Framework (Alice Pau, 2025)
DOI: 10.5281/zenodo.18081055
"""

import os
import json
import re
import anthropic
from datetime import datetime

# ── Configuration ──────────────────────────────────────────────────────────────

MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 2000
SESSION_LOG = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

# Load system prompt from file
SYSTEM_PROMPT_PATH = os.path.join(os.path.dirname(__file__), "system_prompt.md")

def load_system_prompt() -> str:
    """Extract the prompt block from system_prompt.md."""
    with open(SYSTEM_PROMPT_PATH, "r") as f:
        content = f.read()
    # Extract content between the triple backticks
    match = re.search(r"```\n(.*?)```", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    raise ValueError("Could not find prompt block in system_prompt.md")


# ── Parsing ─────────────────────────────────────────────────────────────────────

def parse_response(raw: str) -> tuple[dict | None, str]:
    """
    Split model output into:
    - inner_state: parsed JSON from <INNER_STATE>...</INNER_STATE>
    - probe: plain text for the user
    """
    inner_state = None
    probe = raw.strip()

    match = re.search(r"<INNER_STATE>(.*?)</INNER_STATE>", raw, re.DOTALL)
    if match:
        json_str = match.group(1).strip()
        try:
            inner_state = json.loads(json_str)
        except json.JSONDecodeError as e:
            inner_state = {"parse_error": str(e), "raw": json_str}
        # Remove INNER_STATE block from user-facing text
        probe = raw.replace(match.group(0), "").strip()

    return inner_state, probe


# ── Completeness check ──────────────────────────────────────────────────────────

def is_map_ready(inner_state: dict | None) -> bool:
    """Check if stopping criterion is met."""
    if not inner_state:
        return False
    completeness = inner_state.get("completeness", {})
    return completeness.get("ready_to_map", False)


# ── Display ─────────────────────────────────────────────────────────────────────

def display_inner_state(inner_state: dict | None, turn: int):
    """Print formatted JSON state to terminal."""
    print("\n" + "═" * 60)
    print(f"  INNER STATE — Turn {turn}")
    print("═" * 60)
    if inner_state:
        # Completeness summary
        c = inner_state.get("completeness", {})
        print(f"  Block:  {inner_state.get('current_block', '—')}")
        print(f"  Mode:   {inner_state.get('interaction_mode', '—')}")
        xi = inner_state.get("field_state", {}).get("xi", "—")
        beta = inner_state.get("field_state", {}).get("beta", "—")
        print(f"  ξ: {xi}   β: {beta}")
        print()
        print("  DMES confidence:")
        dmes = inner_state.get("dmes", {})
        for v in ["direction", "meaning", "expression", "state"]:
            conf = dmes.get(v, {}).get("confidence", 0)
            hyp = dmes.get(v, {}).get("hypothesis", "—")
            bar = "█" * int(conf * 10) + "░" * (10 - int(conf * 10))
            print(f"  {v[0].upper()}  [{bar}] {conf:.1f}  {hyp or '—'}")
        print()
        faces = inner_state.get("faces", [])
        print(f"  Faces found: {len(faces)}")
        for face in faces:
            antipode = face.get("antipode_hypothesis") or "not yet localised"
            confirmed = face.get("confirmed_across_blocks", [])
            print(f"  └─ [{face.get('id')}] {face.get('label')}  β={face.get('depth_beta', '—')}")
            print(f"      confirmed in: {confirmed}")
            print(f"      antipode: {antipode}")
        print()
        uncharted = inner_state.get("uncharted_zones", [])
        if uncharted:
            print(f"  Uncharted zones:")
            for z in uncharted:
                print(f"  · {z}")
        print()
        print(f"  Completeness:")
        for k, v in c.items():
            mark = "✓" if v else "○"
            print(f"  {mark} {k}")
        print()
        print(f"  Next probe target: {inner_state.get('next_probe_target', '—')}")
    else:
        print("  [No inner state parsed]")
    print("═" * 60 + "\n")


def display_probe(probe: str):
    """Print user-facing text."""
    print("\n" + "─" * 60)
    print("  CARTOGRAPHER →")
    print("─" * 60)
    print()
    for line in probe.split("\n"):
        print(f"  {line}")
    print()
    print("─" * 60 + "\n")


# ── Session logging ─────────────────────────────────────────────────────────────

def save_session(log: list, path: str):
    """Save full session log to JSON file."""
    with open(path, "w") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


# ── Main loop ───────────────────────────────────────────────────────────────────

def run():
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    system_prompt = load_system_prompt()

    conversation_history = []
    session_log = []
    turn = 0

    print("\n" + "═" * 60)
    print("  IDENTITY NAVIGATION STACK")
    print("  Workshop 1: Reading the Field")
    print("  ─────────────────────────────")
    print("  Developer view active — INNER STATE visible in terminal")
    print("  Type 'quit' to end session")
    print("═" * 60 + "\n")

    # Opening move — cartographer initiates
    opening = (
        "I'm not going to ask you who you are. "
        "Tell me about something you've been working on lately — "
        "or something you've been thinking about. "
        "Wherever you want to start."
    )
    display_probe(opening)
    conversation_history.append({
        "role": "assistant",
        "content": opening
    })

    while True:
        # Get user input
        try:
            user_input = input("  YOU → ").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if user_input.lower() in ("quit", "exit", "q"):
            print("\n  Session ended.\n")
            break

        if not user_input:
            continue

        turn += 1
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Call API
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=system_prompt,
                messages=conversation_history
            )
            raw = response.content[0].text

        except Exception as e:
            print(f"\n  [API error: {e}]\n")
            continue

        # Parse dual-channel output
        inner_state, probe = parse_response(raw)

        # Display
        display_inner_state(inner_state, turn)
        display_probe(probe)

        # Log
        session_log.append({
            "turn": turn,
            "user": user_input,
            "inner_state": inner_state,
            "probe": probe
        })

        # Add assistant response to history (full raw — model needs its own JSON)
        conversation_history.append({
            "role": "assistant",
            "content": raw
        })

        # Check stopping criterion
        if is_map_ready(inner_state):
            print("\n  ── MAP READY ──")
            print("  Completeness criterion met.")
            print("  The cartographer's next move is the map presentation.")
            print("  Continue the conversation or type 'quit' to end.\n")

        # Save session after every turn
        save_session(session_log, SESSION_LOG)

    # Final save
    if session_log:
        save_session(session_log, SESSION_LOG)
        print(f"  Session saved → {SESSION_LOG}\n")


if __name__ == "__main__":
    run()
