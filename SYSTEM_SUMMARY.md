# Gyroscopic Ethical Harmonizer - System Summary

## What Was Built

A complete, production-ready SKG system that uses four philosophers (Kant, Hume, Spinoza, Locke) as stabilizing gyroscopes for ethical decision-making. The system is deterministic, stateless, and integrates with your existing UCM_4_Core architecture.

## System Components (22 files)

### Core Engine
- **gyroscopic_core.py** - Data structures, enums, vectors, states
- **gyroscopic_stabilizer.py** - Four-axis convergence and stability calculation
- **verdict_engine.py** - Verdict generation, conflict identification, recommendations
- **gyroscopic_harmonizer.py** - Unified main interface

### Philosopher Axes
- **kant_axis.py** - Deontological framework (duty, universalizability)
- **hume_axis.py** - Sentimental framework (empathy, moral sentiment)
- **spinoza_axis.py** - Rational framework (necessity, conatus, adequate ideas)
- **locke_axis.py** - Rights framework (natural rights, consent, proportionality)

### Configuration & Documentation
- **harmonizer_config.yaml** - Domain-specific tuning (medical, legal, business, etc.)
- **README.md** - Full documentation
- **ARCHITECTURE.md** - System design and physics analogy
- **INTEGRATION_GUIDE.md** - How to integrate with UCM_4_Core
- **QUICK_REFERENCE.md** - Developer cheat sheet
- **manifest.json** - System manifest

### Testing & Demo
- **test_harmonizer.py** - Comprehensive test suite (all tests pass)
- **demo.py** - Interactive demonstration with 7 scenarios
- **requirements.txt** - Dependencies (none - pure Python)

## Key Features

1. **Four-Axis Stabilization**: Each philosopher provides angular momentum that resists ethical drift
2. **Precession Detection**: Tracks ethical drift between decisions
3. **Stability Scoring**: 5 levels from CRITICAL to HARMONIZED
4. **Conflict Transparency**: All axis disagreements surfaced, never hidden
5. **Confidence Capping**: 0.75 cap under peer tension (matches your system rules)
6. **Immutable History**: Append-only, no retroactive changes
7. **Domain Tuning**: Configurable weights for medical, legal, business contexts
8. **Action Comparison**: Rank multiple actions for same dilemma

## Integration Points

- **CALI**: Invoke for ethical coordination decisions
- **UCM_Core_ECM**: Add as fifth convergence dimension
- **Tension Ledger**: Log CRITICAL/UNSTABLE states as escalations
- **Worker SKGs**: Pre-action ethical checks for booklet/podcast makers
- **SoftMax Advisory**: Feed stability scores as confidence-weighted signals

## System Properties (Match Your Architecture)

- ✅ Deterministic
- ✅ Stateless (no learning, no mutation)
- ✅ CPU-only
- ✅ No external dependencies
- ✅ Confidence cap: 0.75 under tension
- ✅ Immutable append-only history
- ✅ Peer-aware (integrates with Core 4)
- ✅ Conflict-transparent

## How It Works

1. Input: Ethical dilemma + proposed action(s)
2. Each philosopher axis evaluates independently → produces 3D ethical vector
3. Stabilizer computes weighted resultant + stability score + precession angle
4. Verdict engine classifies: RECOMMENDED, PERMISSIBLE, NEUTRAL, QUESTIONABLE, PROHIBITED, CONFLICT
5. Output: Complete verdict with axis breakdown, conflicts, recommendations

## Usage Example

```python
from gyroscopic_harmonizer import GyroscopicHarmonizer

h = GyroscopicHarmonizer(confidence_cap=0.75)

# Evaluate single action
result = h.evaluate(
    scenario="Company considers layoffs to increase profits",
    actions=["lay off 1000 workers"],
    stakeholders=["workers", "company", "community"],
    severity="MAJOR"
)

# Quick check
verdict = h.quick_check("Scenario", "action")  # Returns: RECOMMENDED, PROHIBITED, etc.

# Compare multiple actions
result = h.evaluate(
    scenario="Triage during pandemic",
    actions=["first-come-first-served", "save most likely", "prioritize young"],
    severity="CATASTROPHIC"
)
# Returns ranked list
```

## Test Results

All 9 test categories passed:
- ✅ Kant Axis (deontological evaluation)
- ✅ Hume Axis (sentimental evaluation)
- ✅ Spinoza Axis (rational evaluation)
- ✅ Locke Axis (rights evaluation)
- ✅ Stabilizer (convergence + stability)
- ✅ Verdict Engine (classification + recommendations)
- ✅ Action Comparison (multi-action ranking)
- ✅ Harmonizer Interface (unified API)
- ✅ Edge Cases (trivial, catastrophic, ambiguous)

## Next Steps

1. Place `Gyroscopic_Harmonizer/` in your `UCM_4_Core/` directory
2. Import in CALI coordination module
3. Add ethical check hooks to worker SKGs
4. Configure domain-specific weights for your use cases
5. Connect to Tension Ledger for conflict logging

## Files Available for Download

All files are saved in `/mnt/agents/output/Gyroscopic_Harmonizer/`
