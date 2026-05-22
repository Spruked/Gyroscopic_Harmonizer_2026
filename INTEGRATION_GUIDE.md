# Integration Guide: Gyroscopic Harmonizer → UCM_4_Core

## Overview

This guide shows how to integrate the Gyroscopic Harmonizer into your existing UCM_4_Core architecture alongside CALI, Caleon Prime Legacy, KayGee 1.0, and UCM_Core_ECM.

## Folder Placement

```
UCM_4_Core/
├── CALI/
│   ├── cali_immutable_matrix/
│   │   └── system_memory.py
│   └── softmax_advisory.py          # Existing
├── Caleon_Prime_Legacy/
│   └── spacefield_cognition.py      # Existing
├── KayGee_1.0/
│   └── skg_engine.py                # Existing
├── UCM_Core_ECM/
│   └── convergence_matrix.py        # Existing
└── Gyroscopic_Harmonizer/           # ← NEW
    ├── gyroscopic_harmonizer.py     # Main interface
    ├── core/
    ├── axes/
    ├── stabilizer/
    ├── ethical_verdict/
    └── config/
```

## Integration Patterns

### Pattern 1: CALI Coordination Hook

Add to `UCM_4_Core/CALI/cali_coordination.py`:

```python
from Gyroscopic_Harmonizer.gyroscopic_harmonizer import GyroscopicHarmonizer

class CALIEthicalCoordination:
    def __init__(self):
        self.ethical_harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)
        self.tension_ledger = TensionLedger()  # Existing

    def evaluate_peer_decision(self, decision_context):
        """
        When Core 4 siblings disagree, use harmonizer to evaluate
        the ethical dimensions of each position.
        """
        # Extract ethical dimensions from sibling positions
        dilemma = self._build_dilemma_from_peers(decision_context)

        # Evaluate through four-philosopher framework
        verdict = self.ethical_harmonizer.evaluate(
            scenario=dilemma.scenario,
            actions=dilemma.actions,
            stakeholders=dilemma.stakeholders,
            severity=dilemma.severity,
            time_pressure=dilemma.time_pressure
        )

        # If stability is CRITICAL or UNSTABLE, log to Tension Ledger
        if verdict['stability']['score'] < 0.45:
            self.tension_ledger.log_escalation(
                source="gyroscopic_harmonizer",
                reason=f"Ethical instability: {verdict['stability']['level']}",
                conflicts=verdict['conflicts'],
                timestamp=verdict['metadata']['timestamp']
            )

        return verdict
```

### Pattern 2: ECM Convergence Integration

Add to `UCM_4_Core/UCM_Core_ECM/convergence_matrix.py`:

```python
from Gyroscopic_Harmonizer.gyroscopic_harmonizer import GyroscopicHarmonizer

class ECMWithEthicalLayer:
    """
    ECM now includes ethical convergence as a fifth dimension
    alongside Locke, Hume, Kant, Spinoza, and SoftMax.
    """

    def __init__(self):
        self.philosophical_skg = {
            'locke': LockeSKG(),
            'hume': HumeSKG(),
            'kant': KantSKG(),
            'spinoza': SpinozaSKG(),
            'softmax': SoftMaxSKG()
        }
        self.ethical_harmonizer = GyroscopicHarmonizer()

    def converge_with_ethics(self, query, context):
        """
        Standard ECM convergence now includes ethical stabilization.
        """
        # Get philosophical verdicts
        verdicts = {name: skg.evaluate(query) for name, skg in self.philosophical_skg.items()}

        # Get ethical harmonization
        ethical_state = self.ethical_harmonizer.evaluate(
            scenario=query,
            actions=[context.get('proposed_action', 'default')],
            severity=context.get('severity', 'MODERATE'),
            time_pressure=context.get('time_pressure', 0.0)
        )

        # Combine: standard ECM + ethical stability score
        convergence = self._compute_convergence(verdicts)
        ethical_weight = ethical_state['stability']['score']

        # Adjust confidence based on ethical stability
        adjusted_confidence = convergence['confidence'] * ethical_weight

        return {
            'convergence': convergence,
            'ethical_stability': ethical_state['stability'],
            'ethical_verdict': ethical_state['verdict'],
            'adjusted_confidence': adjusted_confidence,
            'requires_human_review': ethical_state['stability']['score'] < 0.45
        }
```

### Pattern 3: Worker SKG Integration

For product SKGs (booklet maker, podcast maker, etc.):

```python
# In your worker SKG ethical check hook
from Gyroscopic_Harmonizer.gyroscopic_harmonizer import GyroscopicHarmonizer

class EthicalWorkerMixin:
    def __init__(self):
        self.ethical_checker = GyroscopicHarmonizer(confidence_cap=0.75)

    def pre_action_ethical_check(self, action_description, affected_parties):
        """
        Before executing any significant action, check ethical implications.
        """
        result = self.ethical_checker.quick_check(
            scenario=action_description,
            action=action_description
        )

        if result in ['PROHIBITED', 'CRITICAL_CONFLICT']:
            raise EthicalViolationError(
                f"Action blocked by ethical check: {result}"
            )

        if result in ['QUESTIONABLE', 'CONFLICT']:
            self.log_warning(f"Ethical concern flagged: {result}")
            return False  # Require explicit override

        return True
```

### Pattern 4: Tension Ledger Integration

```python
# When harmonizer detects deep conflict, it becomes a tension entry

class TensionLedger:
    def log_gyroscopic_conflict(self, verdict):
        """
        Log gyroscopic ethical conflicts to the immutable tension ledger.
        """
        if verdict['verdict']['type'] in ['DEEP_CONFLICT', 'INDETERMINATE_CRITICAL']:
            entry = {
                'timestamp': verdict['metadata']['timestamp'],
                'type': 'ethical_gyroscopic_conflict',
                'severity': verdict['metadata']['severity'],
                'stability': verdict['stability']['level'],
                'stability_score': verdict['stability']['score'],
                'conflicts': [
                    {
                        'axis_1': c['axis_1'],
                        'axis_2': c['axis_2'],
                        'disagreement': c['disagreement'],
                        'severity': c['severity']
                    }
                    for c in verdict['conflicts']
                ],
                'resultant': verdict['resultant'],
                'requires_escalation': True,
                'immutable': True  # Never modified, only appended
            }
            self.append(entry)
```

## Configuration for Your System

### Domain-Specific Tuning

For your specific use cases (content creation, data processing, NFT minting):

```yaml
# config/harmonizer_config.yaml - Add these domains
domains:
  content_creation:
    axis_weights:
      kant: 1.0    # Originality, not plagiarism
      hume: 1.2    # Audience empathy
      spinoza: 1.0  # Logical coherence
      locke: 1.1    # IP rights, creator consent

  data_processing:
    axis_weights:
      kant: 1.1    # Duty to handle data responsibly
      hume: 0.9    # Less emotional, more procedural
      spinoza: 1.2  # Rational necessity of good data practices
      locke: 1.3    # Privacy rights, consent critical

  nft_minting:
    axis_weights:
      kant: 1.1    # Honest representation of assets
      hume: 0.8    # Less sentiment, more verification
      spinoza: 1.0  # Technical correctness
      locke: 1.3    # Property rights, ownership clarity
```

## API for Your Existing Components

### From CALI
```python
# CALI asks: "Should we proceed with this action?"
ethical_result = gyroscopic_harmonizer.evaluate(
    scenario=proposed_action.description,
    actions=[proposed_action.name],
    stakeholders=proposed_action.affected_parties,
    severity=proposed_action.risk_level,
    time_pressure=proposed_action.urgency
)

if ethical_result['verdict']['clearance'] == 'NO_CLEARANCE':
    cali.block_action(proposed_action, reason=ethical_result['verdict']['recommendation'])
else:
    cali.approve_action(proposed_action, ethical_clearance=ethical_result)
```

### From KayGee 1.0 (Content Generation)
```python
# Before generating content, check ethical implications
def generate_with_ethics(self, prompt, content_type):
    ethical_check = self.harmonizer.quick_check(
        scenario=f"Generate {content_type} about: {prompt}",
        action=f"generate {content_type}"
    )

    if ethical_check == 'PROHIBITED':
        return {"error": "Content generation blocked by ethical constraints", "verdict": ethical_check}

    # Proceed with generation
    return self.generate(prompt)
```

### From Caleon Prime Legacy (SpaceField Cognition)
```python
# EGF substrate can feed into ethical harmonizer
# When Caleon generates, she can check ethical field alignment

def generate_with_field_ethics(self, query):
    # Standard EGF generation
    field_state = self.spacefield.evaluate(query)

    # Ethical check on generated output
    ethical_verdict = self.harmonizer.evaluate(
        scenario=f"Generated output: {field_state.summary}",
        actions=["publish generated content"],
        severity="MODERATE"
    )

    # Caleon reports immutably to CALI
    self.report_to_cali({
        'generation': field_state,
        'ethical_verdict': ethical_verdict,
        'confidence': min(field_state.confidence, ethical_verdict['verdict']['confidence'])
    })
```

## Testing in Your Environment

```python
# Test integration with existing Core 4 components
def test_ethical_integration():
    harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)

    # Test 1: Data processing ethics
    result = harmonizer.evaluate(
        scenario="Process user data through AI without explicit consent for feature improvement",
        actions=["process without consent", "ask for consent first", "anonymize then process"],
        stakeholders=["users", "company", "regulators"],
        severity="MAJOR",
        context={"data_type": "personal", "purpose": "improvement"}
    )
    assert result['ranked_actions'][0]['verdict']['type'] == 'ETHICALLY_RECOMMENDED'

    # Test 2: Content creation ethics
    result = harmonizer.evaluate(
        scenario="Use AI to generate audiobook voices mimicking real celebrities without permission",
        actions=["mimic voices without permission", "use original voices", "license voices properly"],
        stakeholders=["celebrities", "listeners", "platform", "creators"],
        severity="MAJOR",
        context={"content_type": "audiobook", "voice_type": "mimic"}
    )
    assert result['ranked_actions'][0]['verdict']['clearance'] == 'FULL_CLEARANCE'
```

## Immutable Memory Integration

The harmonizer's history can be written to CALI's immutable matrix:

```python
# In CALI's immutable operational memory
cali_memory.write({
    'type': 'ethical_evaluation',
    'source': 'gyroscopic_harmonizer',
    'timestamp': verdict['metadata']['timestamp'],
    'verdict_type': verdict['verdict']['type'],
    'stability': verdict['stability']['level'],
    'resultant': verdict['resultant'],
    'immutable': True,
    'append_only': True
})
```

## Summary

The Gyroscopic Harmonizer adds a dedicated ethical stabilization layer to your Core 4 architecture without disrupting existing patterns:

1. **Deterministic**: Same inputs → same outputs (matches your system rules)
2. **Stateless**: No learning, no mutation (matches SKG principles)
3. **Immutable history**: Append-only (matches Tension Ledger pattern)
4. **Confidence-capped**: 0.75 under tension (matches your existing caps)
5. **Peer-aware**: Integrates with CALI coordination (matches Core 4 architecture)

The four philosophers provide ethical gyroscopic inertia — they resist drift toward any single ethical framework, forcing balanced consideration of duty, empathy, rational necessity, and rights.
