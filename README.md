# Gyroscopic Ethical Harmonizer

## Four-Axis Philosophical Stabilization System for Ethical Decision-Making

### Overview

The Gyroscopic Harmonizer is a deterministic, stateless SKG system that uses four philosophical frameworks as stabilizing gyroscopes for ethical decision-making. Like a mechanical gyroscope resists changes in orientation, each philosopher axis resists ethical drift toward their opposing frameworks.

### The Four Axes

| Axis | Philosopher | Framework | Resists Drift Toward |
|------|-------------|-----------|---------------------|
| **Kant** | Immanuel Kant | Deontological (Duty, Universalizability) | Consequentialism, emotional bias |
| **Hume** | David Hume | Sentimental (Empathy, Moral Sentiment) | Cold rationalism, abstract universalism |
| **Spinoza** | Baruch Spinoza | Rational/Necessity (Conatus, Adequate Ideas) | Arbitrary choice, emotional volatility |
| **Locke** | John Locke | Rights/Consent (Natural Rights, Proportionality) | Tyranny, paternalism |

### Architecture

```
Gyroscopic_Harmonizer/
├── gyroscopic_harmonizer.py      # Main interface
├── demo.py                        # Interactive demo
├── core/
│   └── gyroscopic_core.py         # Data structures, enums, base classes
├── axes/
│   ├── kant_axis.py               # Deontological gyroscope
│   ├── hume_axis.py               # Sentimental gyroscope
│   ├── spinoza_axis.py            # Rational/necessity gyroscope
│   └── locke_axis.py              # Rights/consent gyroscope
├── stabilizer/
│   └── gyroscopic_stabilizer.py   # Four-axis convergence engine
├── ethical_verdict/
│   └── verdict_engine.py          # Verdict generation and conflict resolution
├── config/
│   └── harmonizer_config.yaml     # Domain-specific tuning
└── tests/
    └── test_harmonizer.py         # Comprehensive test suite
```

### Core Concepts

#### Gyroscopic Stabilization
Each philosopher axis produces a 3D ethical vector (x=valence, y=individual/collective, z=temporal). The stabilizer computes a weighted resultant vector and measures system stability based on axis alignment.

#### Precession
When axes conflict, the system experiences "precession" — ethical drift that must be actively corrected. High precession indicates fundamental philosophical disagreement about the dilemma.

#### Stability Levels
- **HARMONIZED** (0.85-1.0): All axes converge — high confidence verdict
- **STABLE** (0.65-0.85): Good alignment — proceed with standard oversight
- **TURBULENT** (0.45-0.65): Moderate disagreement — conditional recommendation
- **UNSTABLE** (0.25-0.45): Major conflict — requires human adjudication
- **CRITICAL** (0.0-0.25): Severe conflict — no automated decision possible

### Usage

#### Basic Evaluation
```python
from gyroscopic_harmonizer import GyroscopicHarmonizer

harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)

result = harmonizer.evaluate(
    scenario="A company must decide whether to use AI that displaces workers",
    actions=["implement AI", "keep human workers", "hybrid approach"],
    stakeholders=["workers", "company", "customers"],
    severity="MAJOR",
    time_pressure=0.3
)
```

#### Quick Check
```python
verdict = harmonizer.quick_check(
    "A researcher considers fabricating data",
    "fabricate research data"
)
# Returns: "PROHIBITED", "QUESTIONABLE", "NEUTRAL", "PERMISSIBLE", "RECOMMENDED", or "CONFLICT"
```

#### Get Individual Reasoning
```python
reasoning = harmonizer.get_axis_reasoning(
    "Government considers mass surveillance",
    "monitor all citizens"
)
# Returns: {"Kant (Deontological)": "...", "Hume (Sentimental)": "...", ...}
```

#### Compare Multiple Actions
```python
result = harmonizer.evaluate(
    scenario="Triage during pandemic",
    actions=["first-come-first-served", "save most likely to survive", "prioritize young"],
    severity="CATASTROPHIC"
)
# Returns ranked list of all actions with full analysis
```

### Domain-Specific Tuning

The system supports domain-specific axis weight tuning via configuration:

```yaml
domains:
  medical:
    axis_weights:
      kant: 1.2    # Duty stronger in medical contexts
      hume: 1.1    # Empathy important
      locke: 1.0
      spinoza: 0.9
```

### Verdict Types

| Type | Description | Action |
|------|-------------|--------|
| **ETHICALLY_RECOMMENDED** | Strong positive convergence | Proceed with confidence |
| **ETHICALLY_PERMISSIBLE** | Positive but not strong | Proceed with standard oversight |
| **ETHICALLY_NEUTRAL** | No strong valence | Decide on non-ethical factors |
| **CONDITIONAL** | Mixed signals | Implement safeguards |
| **ETHICALLY_QUESTIONABLE** | Negative but some disagreement | Proceed only with strong justification |
| **ETHICALLY_PROHIBITED** | Strong negative convergence | Do not proceed |
| **DEEP_CONFLICT** | Fundamental axis disagreement | Defer decision, seek input |
| **INDETERMINATE_CRITICAL** | Severe instability | Escalate to ethics board |

### System Properties

- **Deterministic**: Same input always produces same output
- **Stateless**: No learning or mutation (per your system rules)
- **Immutable**: History is append-only, no retroactive changes
- **Confidence-capped**: 0.75 cap under peer tension (high severity/time pressure)
- **Conflict-transparent**: All axis disagreements are surfaced, not hidden

### Integration with Core 4 Architecture

This harmonizer integrates with your existing UCM_4_Core architecture:
- Can be invoked by CALI for ethical coordination decisions
- Operates within the ECM (Epistemic Convergence Matrix) framework
- Follows the same deterministic, stateless principles as your other SKG components
- Supports the Tension Ledger pattern for tracking disagreements

### Running the Demo

```bash
cd Gyroscopic_Harmonizer
python demo.py
```

### Running Tests

```bash
python tests/test_harmonizer.py
```

### Version

**1.0.0** - Initial release with four-axis gyroscopic stabilization
