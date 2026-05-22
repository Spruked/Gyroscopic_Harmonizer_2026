# Gyroscopic Harmonizer Architecture

## System Diagram

```
                         Ethical Dilemma Input
                    (scenario, actions, stakeholders)
                                |
                                v
        +-----------------------+-----------------------+
        |           GYROSCOPIC STABILIZER               |
        |                                                 |
        |   +---------+  +---------+  +---------+      |
        |   |  KANT   |  |  HUME   |  | SPINOZA |      |
        |   |  Axis   |  |  Axis   |  |  Axis   |      |
        |   | (Duty)  |  | (Empathy)|  |(Reason) |      |
        |   +----+----+  +----+----+  +----+----+      |
        |        |            |            |            |
        |        v            v            v            |
        |   +----+------------+------------+----+      |
        |   |         LOCKE Axis              |        |
        |   |      (Rights/Consent)           |        |
        |   +----+------------+------------+----+      |
        |        |            |            |            |
        |        v            v            v            |
        |   +----+------------+------------+----+      |
        |   |      VECTOR CONVERGENCE ENGINE      |      |
        |   |  - Weighted resultant calculation    |      |
        |   |  - Stability scoring               |      |
        |   |  - Precession detection            |      |
        |   +----+------------+------------+----+      |
        |        |            |            |            |
        +--------|------------|------------|------------+
                 |            |            |
                 v            v            v
        +--------+------------+------------+--------+
        |         ETHICAL VERDICT ENGINE            |
        |                                           |
        |  - Verdict classification                 |
        |  - Conflict identification                |
        |  - Recommendation generation              |
        |  - Clearance calculation                  |
        |                                           |
        +--------+------------+------------+--------+
                 |            |            |
                 v            v            v
        +--------+------------+------------+--------+
        |              OUTPUT                             |
        |  - Verdict type (RECOMMENDED, PROHIBITED, etc) |
        |  - Stability report (HARMONIZED, TURBULENT, etc)|
        |  - Axis breakdown (each philosopher's view)     |
        |  - Conflicts (where axes disagree)              |
        |  - Recommendations (actionable guidance)        |
        +-------------------------------------------------+
```

## Gyroscope Physics Analogy

### Real Gyroscope Properties → Ethical System Properties

| Physical Property | Ethical Analog |
|-------------------|----------------|
| **Angular Momentum** | Philosophical conviction strength |
| **Precession** | Ethical drift when axes conflict |
| **Nutation** | Minor oscillations in ethical judgment |
| **Rigidity in Space** | Resistance to ethical drift |
| **Gimbal Lock** | Complete system failure (all axes aligned in conflict) |

### How Stabilization Works

1. **Individual Axis Spin**: Each philosopher evaluates the dilemma independently, producing an ethical vector with direction (valence) and magnitude (confidence)

2. **Vector Summation**: The stabilizer computes a weighted resultant vector. When axes align, vectors reinforce. When they conflict, they partially cancel.

3. **Stability Scoring**: The dot product between all axis pairs measures alignment. High average alignment = high stability.

4. **Precession Detection**: If the resultant shifts significantly from previous evaluations, the system detects ethical drift.

5. **Verdict Classification**: Based on resultant magnitude, direction, and stability, the system classifies the ethical verdict.

## Data Flow

```
Input Dilemma
    |
    ├──→ Kant Axis → Vector(x, y, z, confidence)
    ├──→ Hume Axis → Vector(x, y, z, confidence)
    ├──→ Spinoza Axis → Vector(x, y, z, confidence)
    └──→ Locke Axis → Vector(x, y, z, confidence)
              |
              v
    +-------------------+
    | Resultant = Σ(wᵢvᵢ) |
    +-------------------+
              |
              v
    +-------------------+
    | Stability = f(alignment, confidence) |
    +-------------------+
              |
              v
    +-------------------+
    | Precession = angle(resultantₜ, resultantₜ₋₁) |
    +-------------------+
              |
              v
    +-------------------+
    | Verdict = classify(resultant, stability) |
    +-------------------+
              |
              v
           Output
```

## Integration Points

### With CALI (Cognitively Aligned Linear Intelligence)
The harmonizer can be invoked by CALI when:
- Core 4 siblings disagree on ethical dimensions
- A decision requires explicit ethical clearance
- The Tension Ledger flags an ethical escalation

### With Tension Ledger
When stability is CRITICAL or UNSTABLE:
1. Verdict is logged to Tension Ledger
2. Disagreements between axes are recorded as escalation signals
3. No retroactive fixes — the conflict is preserved for analysis

### With SoftMax Advisory
The SoftMax component (from your existing system) can:
- Receive stability scores as confidence-weighted signals
- Detect when ethical verdicts are outliers
- Provide non-authoritative advisory to CALI

## State Management

### Immutable History
```python
self.history: List[GyroscopicState]  # Append-only
self.precession_history: List[float]  # Append-only
```

### No Mutation Rules
- Axis controllers are stateless
- Stabilizer history is append-only
- Verdict engine produces new outputs, never modifies inputs
- Confidence caps are applied at evaluation time, not stored

## Performance Characteristics

- **Evaluation Time**: O(1) per axis, O(n) for n actions
- **Memory**: O(h) where h = history limit (default 1000)
- **Determinism**: Fully deterministic for same inputs
- **Thread Safety**: Stateless design allows parallel evaluation

## Error Handling

| Condition | Response |
|-----------|----------|
| Empty scenario | Return NEUTRAL with low confidence |
| Unknown severity | Default to MODERATE |
| All axes neutral | Return ETHICALLY_NEUTRAL |
| Gimbal lock (all conflict) | Return INDETERMINATE_CRITICAL |
| Missing stakeholders | Evaluate with empty stakeholder list |
