"""Turns a numeric risk score into a Safe / Caution / Danger verdict."""

DEFAULT_THRESHOLDS = {"caution": 30, "danger": 60}


def to_level(score: int, thresholds: dict | None = None) -> str:
    """Map a 0-100 score to 'safe', 'caution' or 'danger'."""
    t = thresholds or DEFAULT_THRESHOLDS
    if score >= t["danger"]:
        return "danger"
    if score >= t["caution"]:
        return "caution"
    return "safe"
