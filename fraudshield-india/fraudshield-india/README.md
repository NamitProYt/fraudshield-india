# 🛡️ FraudShield India

**An open-source AI guardian that spots "digital arrest" and UPI scams on your phone, before you pay.**

> *"CBI Notice: Your Aadhaar is linked to money laundering. Call now or face arrest."*
> FraudShield is designed to catch messages like this before the victim replies or pays.

Built by **Team Quad Core** for **Hack the Circle 2026** (MAIT Delhi, Open Circle).
**Track:** AI/ML & Cybersecurity · **License:** MIT

📄 Presentation: [`docs/FraudShield-India-presentation.pdf`](docs/FraudShield-India-presentation.pdf)

---

## The problem

- About **₹4,057 crore** was lost to "digital arrest" scams from 2022 to May 2026, across roughly 2.98 lakh complaints.
- "Digital arrest" **does not exist in Indian law**. No agency can arrest anyone over a call or video call.
- About 1 in 5 UPI-user families faced fraud in three years, and 51% of victims never reported it.

*Sources: I4C data reported by News18 (Jul 2026); Cybersecify (yearly losses); LocalCircles survey via Business Standard.*

Scammers change numbers and UPI IDs within minutes, so blacklists and file scanners miss them. What stays the same is the **language of fear and urgency**, so FraudShield reads the language.

## How it works

Two engines produce one verdict:

| Engine | What it does |
|---|---|
| **Engine 1: Rule & signature engine** | Instant matching of scam phrases, patterns and unverified `.apk` links. |
| **Engine 2: Urgency & coercion AI** | A compact quantized DistilBERT model that reads tone (authority, threats, artificial urgency) even when no keyword matches. |

Both feed a single **risk score** → **Safe** (passes quietly), **Caution** (yellow nudge) or **Danger** (red alert plus a one-tap draft report for **1930** / cybercrime.gov.in).

**Privacy by design:** everything is meant to run on the device. No messages stored, no telemetry.

## Project status (transparent progress)

| Component | Status |
|---|---|
| Rule & signature engine (Engine 1) | ✅ Working prototype in this repo |
| Scam rule set, sample data and tests | ✅ Included |
| Urgency & coercion AI (quantized DistilBERT, ONNX Runtime) | 🚧 Planned for the Round 2 build |
| FastAPI backend and Redis caching | 🚧 Planned for the Round 2 build |
| Chrome extension (Manifest V3) and Next.js UI | 🚧 Planned for the Round 2 build |
| 1930 / cybercrime.gov.in report drafter | 🚧 Planned for the Round 2 build |
| Python SDK (`pip install fraudshield`) | 📅 Roadmap, not yet published |

Performance figures in the presentation (for example under 45 ms API latency) are **design targets**, not measured results yet.

## Try the prototype

Requires Python 3.10+.

```bash
git clone https://github.com/NamitProYt/fraudshield-india.git
cd fraudshield-india
pip install -r requirements.txt

# Analyse a message
python -m engine.rules_engine "CBI Notice: Your Aadhaar is linked to money laundering. Call now or face arrest."

# Run the tests
python -m pytest
```

Example output:

```
Verdict: DANGER  (risk score 85/100)
 - Claims to be from a government agency or police: cbi
 - Mentions your ID, SIM or a parcel as the hook: aadhaar
 - Uses threats of arrest or legal action: arrest, money laundering
 - Creates artificial urgency or secrecy: call now
```

## Repository layout

```
engine/       rule engine and risk scoring (Engine 1)
rules/        scam_rules.json, the community-maintained rule set
data/         synthetic sample messages used by the tests
tests/        automated tests
docs/         presentation and diagrams
extension/    Chrome extension (planned)
```

## Contributing

Every new scam we learn protects everyone. Rules are proposed in public through pull requests and checked by automated tests. See [CONTRIBUTING.md](CONTRIBUTING.md). Please use **synthetic examples only**, never real personal data.

## Team Quad Core

- Namit Bisht (Team Leader)
- Shreya Gupta
- Tanish Paraswal
- Sakshi Parihar

## If you are targeted by a scam

Call **1930** or report at <https://cybercrime.gov.in> immediately. Police never arrest anyone over a video call.

## License

Released under the [MIT License](LICENSE).
