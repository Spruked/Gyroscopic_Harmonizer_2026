# Gyroscopic Harmonizer - Quick Reference Card

## One-Line Usage

```python
from gyroscopic_harmonizer import GyroscopicHarmonizer

h = GyroscopicHarmonizer()
result = h.evaluate(scenario="...", actions=["action1", "action2"])
```

## Verdict Types (Fast Lookup)

| Code | Meaning | Do This |
|------|---------|---------|
| `RECOMMENDED` | All axes agree positive | Proceed with confidence |
| `PERMISSIBLE` | Generally positive | Proceed with oversight |
| `NEUTRAL` | No strong signal | Use non-ethical criteria |
| `CONDITIONAL` | Mixed signals | Add safeguards |
| `QUESTIONABLE` | Some negative | Need strong justification |
| `PROHIBITED` | All axes agree negative | Do NOT proceed |
| `CONFLICT` | Axes fundamentally disagree | Escalate to human |
| `CRITICAL_CONFLICT` | System unstable | Emergency escalation |

## Stability Levels

```
HARMONIZED (0.85-1.0)  ████████████████████  All axes aligned
STABLE (0.65-0.85)       ████████████████░░░░  Good alignment
TURBULENT (0.45-0.65)    ███████████░░░░░░░░░  Moderate conflict
UNSTABLE (0.25-0.45)     ██████░░░░░░░░░░░░░░  Major conflict
CRITICAL (0.0-0.25)      ██░░░░░░░░░░░░░░░░░░  System failure
```

## Axis Quick Reference

```
KANT (Duty)        → "Can this be universal law?"
HUME (Empathy)     → "What do moral sentiments say?"
SPINOZA (Reason)   → "Does this follow rational necessity?"
LOCKE (Rights)     → "Are rights and consent respected?"
```

## Common Patterns

### Pattern: Block Prohibited Actions
```python
if h.quick_check(scenario, action) == 'PROHIBITED':
    raise ActionBlockedError()
```

### Pattern: Require Human Review for Conflicts
```python
result = h.evaluate(scenario, [action])
if result['stability']['level'] in ['UNSTABLE', 'CRITICAL']:
    send_to_human_review(result)
```

### Pattern: Log All Evaluations
```python
result = h.evaluate(scenario, [action])
logger.info(f"Ethical verdict: {result['verdict']['type']} "
            f"(stability: {result['stability']['score']})")
```

### Pattern: Compare Alternatives
```python
result = h.evaluate(scenario, ["option_a", "option_b", "option_c"])
best = result['ranked_actions'][0]
print(f"Best option: {best['verdict']['action_evaluated']}")
```

## Severity Levels

```
TRIVIAL    → Minor inconvenience
MINOR      → Small impact
MODERATE   → Noticeable impact
MAJOR      → Significant consequences
CATASTROPHIC → Life/death or systemic risk
```

## Integration Checklist

- [ ] Place `Gyroscopic_Harmonizer/` in `UCM_4_Core/`
- [ ] Import in CALI coordination module
- [ ] Add ethical check hooks to worker SKGs
- [ ] Configure domain-specific weights
- [ ] Set up Tension Ledger logging for conflicts
- [ ] Test with your specific use cases
- [ ] Document escalation procedures for CRITICAL stability

## Confidence Cap Rules

```
Normal conditions:     confidence = calculated_value
High severity (≥MAJOR): confidence = min(calculated, 0.75)
High time pressure (>0.7): confidence = min(calculated, 0.75)
Both conditions:       confidence = min(calculated, 0.75)
```

## Error Codes

| Condition | System Response |
|-----------|----------------|
| Empty scenario | NEUTRAL, low confidence |
| Missing severity | Defaults to MODERATE |
| No stakeholders | Evaluates with empty list |
| All axes neutral | ETHICALLY_NEUTRAL |
| Gimbal lock | INDETERMINATE_CRITICAL |

## Performance

- Single evaluation: ~1-5ms (CPU-only)
- Action comparison (4 actions): ~4-20ms
- Memory per evaluation: ~2KB
- History limit: 1000 entries (configurable)

## File Locations

```
Main interface:     gyroscopic_harmonizer.py
Core structures:    core/gyroscopic_core.py
Philosopher axes:   axes/{kant,hume,spinoza,locke}_axis.py
Stabilizer engine:  stabilizer/gyroscopic_stabilizer.py
Verdict engine:     ethical_verdict/verdict_engine.py
Configuration:      config/harmonizer_config.yaml
Tests:              tests/test_harmonizer.py
Demo:               demo.py
```

## Support

- Architecture details: See ARCHITECTURE.md
- Integration guide: See INTEGRATION_GUIDE.md
- Full documentation: See README.md
- Run tests: `python tests/test_harmonizer.py`
- Run demo: `python demo.py`
