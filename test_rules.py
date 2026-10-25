import csv
from pathlib import Path

import pytest

from engine.rules_engine import analyze
from engine.risk_score import to_level

DATA = Path(__file__).resolve().parent.parent / "data" / "sample_messages.csv"


def load_samples():
    with open(DATA, newline="", encoding="utf-8") as f:
        return [(row["message"], row["expected_level"]) for row in csv.DictReader(f)]


@pytest.mark.parametrize("message,expected", load_samples())
def test_sample_messages(message, expected):
    assert analyze(message)["level"] == expected


def test_flagship_example_is_danger():
    result = analyze("CBI Notice: Your Aadhaar is linked to money laundering. Call now or face arrest.")
    assert result["level"] == "danger"
    assert result["score"] >= 60
    assert any(r["rule"] == "authority" for r in result["reasons"])


def test_whole_word_matching():
    # 'fir' must not match inside 'confirm'
    result = analyze("Please confirm your booking.")
    assert result["score"] == 0


def test_thresholds():
    assert to_level(0) == "safe"
    assert to_level(30) == "caution"
    assert to_level(60) == "danger"
