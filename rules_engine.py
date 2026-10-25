"""Engine 1: instant rule and signature matching.

Usage (from the repository root):
    python -m engine.rules_engine "CBI Notice: Your Aadhaar is linked to money laundering."

Everything runs locally. Messages are never stored or sent anywhere.
"""
import json
import re
import sys
from pathlib import Path

from engine.risk_score import to_level

RULES_PATH = Path(__file__).resolve().parent.parent / "rules" / "scam_rules.json"


def load_rules(path: Path = RULES_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _normalize(text: str) -> str:
    text = text.lower().replace("\u2019", "'")
    return re.sub(r"\s+", " ", text).strip()


def _has_term(text: str, term: str) -> bool:
    # Whole-word match so that 'fir' does not fire inside 'confirm'.
    return re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", text) is not None


def analyze(message: str, rules: dict | None = None) -> dict:
    """Score one message. Returns level, score and the reasons behind it."""
    rules = rules or load_rules()
    text = _normalize(message)
    score = 0
    reasons = []

    for name, cat in rules["categories"].items():
        hits = [t for t in cat["terms"] if _has_term(text, t)]
        if hits:
            score += cat["weight"]
            reasons.append({"rule": name, "label": cat["label"], "matched": hits})

    for ph in rules.get("phrases", []):
        hits = [t for t in ph["terms"] if _has_term(text, t)]
        if hits:
            score += ph["weight"]
            reasons.append({"rule": ph["name"], "label": ph["label"], "matched": hits})

    for pat in rules.get("patterns", []):
        m = re.search(pat["regex"], text)
        if m:
            score += pat["weight"]
            reasons.append({"rule": pat["name"], "label": pat["label"], "matched": [m.group(0)]})

    score = min(score, 100)
    return {
        "level": to_level(score, rules.get("thresholds")),
        "score": score,
        "reasons": reasons,
    }


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python -m engine.rules_engine "<message text>"')
        sys.exit(1)
    result = analyze(" ".join(sys.argv[1:]))
    print(f"Verdict: {result['level'].upper()}  (risk score {result['score']}/100)")
    for r in result["reasons"]:
        print(f" - {r['label']}: {', '.join(r['matched'])}")


if __name__ == "__main__":
    main()
