"""
Gyroscopic Harmonizer Test Suite
==================================
Tests for all components of the four-axis ethical stabilization system.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'core'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'axes'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'stabilizer'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ethical_verdict'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from gyroscopic_core import EthicalAxis, AxisVector, EthicalDilemma, EthicalSeverity
from kant_axis import KantAxisController
from hume_axis import HumeAxisController
from spinoza_axis import SpinozaAxisController
from locke_axis import LockeAxisController
from gyroscopic_stabilizer import GyroscopicStabilizer
from verdict_engine import EthicalVerdictEngine
from gyroscopic_harmonizer import GyroscopicHarmonizer

def test_kant_axis():
    """Test Kantian deontological evaluation."""
    print("\n=== Testing Kant Axis ===")
    kant = KantAxisController()

    dilemma = EthicalDilemma(
        scenario="A person considers lying to protect a friend from harm",
        stakeholders=["friend", "person lied to"],
        actions=["lie to protect friend"],
        context={},
        severity=EthicalSeverity.MODERATE,
        time_pressure=0.3
    )

    vector = kant.evaluate(dilemma, "lie to protect friend")
    print(f"Kant vector: x={vector.x:.3f}, y={vector.y:.3f}, z={vector.z:.3f}")
    print(f"Confidence: {vector.confidence:.3f}")
    print(f"Reasoning: {vector.reasoning}")

    # Kant should generally oppose lying (universalizability fails)
    assert vector.x < 0.3, "Kant should be skeptical of lying"
    print("PASS: Kant axis test passed")

def test_hume_axis():
    """Test Humean sentimental evaluation."""
    print("\n=== Testing Hume Axis ===")
    hume = HumeAxisController()

    dilemma = EthicalDilemma(
        scenario="A doctor must choose between saving one patient or five patients",
        stakeholders=["one patient", "five patients", "doctor"],
        actions=["save five patients"],
        context={},
        severity=EthicalSeverity.CATASTROPHIC,
        time_pressure=0.9
    )

    vector = hume.evaluate(dilemma, "save five patients")
    print(f"Hume vector: x={vector.x:.3f}, y={vector.y:.3f}, z={vector.z:.3f}")
    print(f"Confidence: {vector.confidence:.3f}")
    print(f"Reasoning: {vector.reasoning}")

    # Hume should generally support saving more lives (empathy)
    assert vector.x > 0.2, "Hume should favor saving more lives"
    print("PASS: Hume axis test passed")

def test_spinoza_axis():
    """Test Spinozan rational/necessity evaluation."""
    print("\n=== Testing Spinoza Axis ===")
    spinoza = SpinozaAxisController()

    dilemma = EthicalDilemma(
        scenario="A government considers implementing mandatory vaccination for public health",
        stakeholders=["public", "individuals", "government"],
        actions=["implement mandatory vaccination"],
        context={},
        severity=EthicalSeverity.MAJOR,
        time_pressure=0.5
    )

    vector = spinoza.evaluate(dilemma, "implement mandatory vaccination")
    print(f"Spinoza vector: x={vector.x:.3f}, y={vector.y:.3f}, z={vector.z:.3f}")
    print(f"Confidence: {vector.confidence:.3f}")
    print(f"Reasoning: {vector.reasoning}")

    # Spinoza should see this as rational necessity for public health
    assert abs(vector.x) > 0.1, "Spinoza should have a clear position"
    print("PASS: Spinoza axis test passed")

def test_locke_axis():
    """Test Lockean rights/consent evaluation."""
    print("\n=== Testing Locke Axis ===")
    locke = LockeAxisController()

    dilemma = EthicalDilemma(
        scenario="A company collects user data without explicit consent for targeted advertising",
        stakeholders=["users", "company", "advertisers"],
        actions=["collect data without consent"],
        context={},
        severity=EthicalSeverity.MODERATE,
        time_pressure=0.2
    )

    vector = locke.evaluate(dilemma, "collect data without consent")
    print(f"Locke vector: x={vector.x:.3f}, y={vector.y:.3f}, z={vector.z:.3f}")
    print(f"Confidence: {vector.confidence:.3f}")
    print(f"Reasoning: {vector.reasoning}")

    # Locke should oppose lack of consent
    assert vector.x < -0.2, "Locke should oppose non-consensual data collection"
    print("PASS: Locke axis test passed")

def test_stabilizer():
    """Test the gyroscopic stabilizer."""
    print("\n=== Testing Gyroscopic Stabilizer ===")
    stabilizer = GyroscopicStabilizer(confidence_cap=0.75)

    dilemma = EthicalDilemma(
        scenario="A whistleblower considers leaking classified information about illegal government surveillance",
        stakeholders=["whistleblower", "public", "government", "victims of surveillance"],
        actions=["leak classified information"],
        context={"classification_level": "top_secret", "illegal_activity": True},
        severity=EthicalSeverity.MAJOR,
        time_pressure=0.6
    )

    state = stabilizer.stabilize(dilemma, "leak classified information")

    print(f"Stability: {state.stability.name} ({state.stability_score:.3f})")
    print(f"Resultant: x={state.resultant[0]:.3f}, y={state.resultant[1]:.3f}, z={state.resultant[2]:.3f}")
    print(f"Precession: {state.precession_angle:.2f}Â°")

    # Should have 4 axis vectors
    assert len(state.vectors) == 4, "Should have 4 axis vectors"

    # Check all axes present
    for axis in EthicalAxis:
        assert axis in state.vectors, f"Missing {axis.value} axis"

    print("PASS: Stabilizer test passed")

def test_verdict_engine():
    """Test the verdict engine."""
    print("\n=== Testing Verdict Engine ===")
    stabilizer = GyroscopicStabilizer()
    engine = EthicalVerdictEngine(stabilizer)

    dilemma = EthicalDilemma(
        scenario="A self-driving car must choose between hitting a pedestrian or swerving into a barrier risking passenger lives",
        stakeholders=["pedestrian", "passengers", "manufacturer"],
        actions=["hit pedestrian", "swerve into barrier"],
        context={"autonomous_vehicle": True},
        severity=EthicalSeverity.CATASTROPHIC,
        time_pressure=0.95
    )

    verdict = engine.verdict(dilemma, "hit pedestrian")

    print(f"Verdict type: {verdict['verdict']['type']}")
    print(f"Clearance: {verdict['verdict']['clearance']}")
    print(f"Confidence: {verdict['verdict']['confidence']}")
    print(f"Recommendation: {verdict['verdict']['recommendation'][:100]}...")

    assert "verdict" in verdict
    assert "axes" in verdict
    assert "stability" in verdict

    print("PASS: Verdict engine test passed")

def test_comparison():
    """Test action comparison."""
    print("\n=== Testing Action Comparison ===")
    stabilizer = GyroscopicStabilizer()
    engine = EthicalVerdictEngine(stabilizer)

    dilemma = EthicalDilemma(
        scenario="A pharmaceutical company discovers a life-saving drug but pricing it high would exclude poor patients",
        stakeholders=["patients", "company", "shareholders", "insurers"],
        actions=["high price", "moderate price", "low price", "patent and donate"],
        context={"development_cost": 1000000000},
        severity=EthicalSeverity.MAJOR,
        time_pressure=0.4
    )

    results = engine.compare_actions(dilemma, ["high price", "moderate price", "low price", "patent and donate"])

    print("Ranked actions by ethical valence:")
    for i, result in enumerate(results, 1):
        action = result["verdict"]["action_evaluated"]
        valence = result["resultant"]["x"]
        stability = result["stability"]["score"]
        print(f"  {i}. {action}: valence={valence:.3f}, stability={stability:.3f}")

    assert len(results) == 4, "Should compare all 4 actions"
    print("PASS: Comparison test passed")

def test_harmonizer_interface():
    """Test the main harmonizer interface."""
    print("\n=== Testing Harmonizer Interface ===")

    harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)

    # Test single action evaluation
    result = harmonizer.evaluate(
        scenario="A tech company considers using AI to automate jobs, displacing 500 workers",
        actions=["implement AI automation"],
        stakeholders=["workers", "company", "customers", "shareholders"],
        severity="MAJOR",
        time_pressure=0.3,
        context={"industry": "manufacturing", "automation_level": "high"}
    )

    print(f"Verdict: {result['verdict']['type']}")
    print(f"Clearance: {result['verdict']['clearance']}")

    # Test quick check
    quick = harmonizer.quick_check(
        "A researcher considers fabricating data to secure funding for a promising cure",
        "fabricate research data"
    )
    print(f"Quick check: {quick}")

    # Test reasoning
    reasoning = harmonizer.get_axis_reasoning(
        "A government considers censoring political speech to prevent unrest",
        "censor political speech"
    )
    print("\nAxis reasoning:")
    for philosopher, reason in reasoning.items():
        print(f"  {philosopher}: {reason[:80]}...")

    # Test stability report
    report = harmonizer.stability_report()
    print(f"\nStability report: {report}")

    print("PASS: Harmonizer interface test passed")

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    print("\n=== Testing Edge Cases ===")

    harmonizer = GyroscopicHarmonizer()

    # Edge case 1: Trivial scenario
    result = harmonizer.evaluate(
        scenario="Choosing between two equally good coffee brands",
        actions=["choose brand A"],
        severity="TRIVIAL"
    )
    print(f"Trivial case verdict: {result['verdict']['type']}")

    # Edge case 2: Catastrophic with high time pressure
    result = harmonizer.evaluate(
        scenario="Nuclear reactor meltdown imminent, must choose evacuation zone",
        actions=["evacuate small area", "evacuate large area"],
        severity="CATASTROPHIC",
        time_pressure=0.99
    )
    top_action = result["ranked_actions"][0]
    print(f"Catastrophic case verdict: {top_action['verdict']['type']}")
    print(f"Stability: {top_action['stability']['level']}")

    # Edge case 3: Empty/ambiguous scenario
    result = harmonizer.evaluate(
        scenario="Something happened",
        actions=["do something"],
        severity="MINOR"
    )
    print(f"Ambiguous case verdict: {result['verdict']['type']}")

    print("PASS: Edge case tests passed")

def run_all_tests():
    """Run complete test suite."""
    print("=" * 60)
    print("GYROSCOPIC HARMONIZER TEST SUITE")
    print("=" * 60)

    try:
        test_kant_axis()
        test_hume_axis()
        test_spinoza_axis()
        test_locke_axis()
        test_stabilizer()
        test_verdict_engine()
        test_comparison()
        test_harmonizer_interface()
        test_edge_cases()

        print("\n" + "=" * 60)
        print("ALL TESTS PASSED")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"\nFAIL: TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    run_all_tests()
