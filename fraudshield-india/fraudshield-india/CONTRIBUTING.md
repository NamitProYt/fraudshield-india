# Contributing to FraudShield India

Scammers change phone numbers and UPI IDs within minutes, but their language stays the same. FraudShield works by learning that language, and anyone can help by proposing new rules.

## Report a new scam pattern

1. Fork this repository and create a branch, e.g. `add-courier-scam-rule`.
2. Edit `rules/scam_rules.json`:
   - add a phrase to the matching category under `categories`, or
   - add a new entry under `phrases` or `patterns` (with a `name`, `weight`, `label` and `terms` or `regex`).
3. Add one or more **synthetic** example messages to `data/sample_messages.csv` with the level they should get (`safe`, `caution` or `danger`).
4. Run the tests and make sure they pass:
   ```bash
   pip install -r requirements.txt
   python -m pytest
   ```
5. Open a pull request describing the scam and how it works.

## Ground rules

- **No real personal data.** Never paste real names, phone numbers, Aadhaar/PAN numbers, UPI IDs or real victims' messages. Write synthetic examples.
- Include at least one harmless message that must stay `safe`, so new rules do not cause false alarms.
- Keep rules specific. A phrase that appears in normal messages should have a low weight or be combined with others.

## Reporting a real scam

If you have been targeted, call **1930** or report at <https://cybercrime.gov.in> right away.
