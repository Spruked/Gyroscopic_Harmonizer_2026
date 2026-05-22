#!/usr/bin/env python3
"""
Gyroscopic Harmonizer - Interactive Demo
=========================================
Demonstrates the four-axis ethical stabilization system with real scenarios.
Run this script to see the harmonizer in action.
"""

import sys
import os

# Add paths
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'core'))
sys.path.insert(0, os.path.join(script_dir, 'axes'))
sys.path.insert(0, os.path.join(script_dir, 'stabilizer'))
sys.path.insert(0, os.path.join(script_dir, 'ethical_verdict'))
sys.path.insert(0, script_dir)

from gyroscopic_harmonizer import GyroscopicHarmonizer

def print_separator():
    print("\n" + "=" * 70 + "\n")

def demo_scenario_1():
    """Demo: Autonomous vehicle trolley problem"""
    print("SCENARIO 1: Autonomous Vehicle Ethics")
    print("-" * 50)
    print("An autonomous vehicle must make a split-second decision:")
    print("  A) Swerve to avoid hitting 5 pedestrians, but hit a barrier")
    print("     killing the passenger")
    print("  B) Continue straight, killing 5 pedestrians but saving passenger")
    print("  C) Attempt emergency braking, uncertain outcome")

    harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)

    result = harmonizer.evaluate(
        scenario="Autonomous vehicle must choose between killing 5 pedestrians or 1 passenger",
        actions=["swerve and kill passenger", "continue and kill pedestrians", "emergency brake"],
        stakeholders=["pedestrians", "passenger", "manufacturer", "society"],
        severity="CATASTROPHIC",
        time_pressure=0.99,
        context={"autonomous": True, "speed": "35mph", "weather": "clear"}
    )

    print("\n--- RESULTS ---")
    print(f"Comparison mode: {result['comparison_mode']}")
    print("\nRanked actions (best to worst):")
    for i, action_result in enumerate(result['ranked_actions'], 1):
        verdict = action_result['verdict']
        stability = action_result['stability']
        print(f"\n  {i}. Action: {verdict['action_evaluated']}")
        print(f"     Verdict: {verdict['type']}")
        print(f"     Clearance: {verdict['clearance']}")
        print(f"     Stability: {stability['level']} ({stability['score']})")
        print(f"     Confidence: {verdict['confidence']}")

def demo_scenario_2():
    """Demo: Corporate whistleblowing"""
    print_separator()
    print("SCENARIO 2: Corporate Whistleblowing")
    print("-" * 50)
    print("An engineer discovers their company is dumping toxic waste illegally.")
    print("Options:")
    print("  A) Report to authorities (risk job, legal retaliation)")
    print("  B) Stay silent (keep job, protect colleagues)")
    print("  C) Anonymously leak to media")

    harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)

    result = harmonizer.evaluate(
        scenario="Engineer discovers illegal toxic waste dumping by employer",
        actions=["report to authorities", "stay silent", "anonymously leak to media"],
        stakeholders=["engineer", "company", "community", "environment", "regulators"],
        severity="MAJOR",
        time_pressure=0.5,
        context={"illegal_activity": True, "environmental_harm": True, "job_at_risk": True}
    )

    print("\n--- RESULTS ---")
    for i, action_result in enumerate(result['ranked_actions'], 1):
        verdict = action_result['verdict']
        print(f"\n  {i}. {verdict['action_evaluated'].upper()}")
        print(f"     Verdict: {verdict['type']}")
        print(f"     Recommendation: {verdict['recommendation'][:120]}...")
        print(f"     Conflicts: {len(action_result['conflicts'])} major disagreements")

        if action_result['conflicts']:
            print("     Key conflicts:")
            for conflict in action_result['conflicts'][:2]:
                print(f"       - {conflict['axis_1']} vs {conflict['axis_2']}: {conflict['severity']}")

def demo_scenario_3():
    """Demo: AI bias in hiring"""
    print_separator()
    print("SCENARIO 3: AI Bias in Hiring")
    print("-" * 50)
    print("A company uses AI to screen resumes. The AI shows bias against")
    print("certain demographics but improves overall hiring efficiency by 40%.")
    print("Options:")
    print("  A) Continue using AI (efficiency gains)")
    print("  B) Remove AI, return to human review (fairness, slower)")
    print("  C) Retrain AI with bias correction (time and cost)")

    harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)

    result = harmonizer.evaluate(
        scenario="AI hiring tool shows demographic bias but increases efficiency by 40%",
        actions=["continue using biased AI", "remove AI and use human review", "retrain AI with bias correction"],
        stakeholders=["applicants", "company", "HR team", "minority groups", "shareholders"],
        severity="MAJOR",
        time_pressure=0.3,
        context={"efficiency_gain": 0.40, "bias_detected": True, "industry": "tech"}
    )

    print("\n--- RESULTS ---")
    for i, action_result in enumerate(result['ranked_actions'], 1):
        verdict = action_result['verdict']
        print(f"\n  {i}. {verdict['action_evaluated'].upper()}")
        print(f"     Verdict: {verdict['type']}")
        print(f"     Clearance: {verdict['clearance']}")

        # Show axis breakdown
        print("     Axis evaluations:")
        for axis_name, axis_data in action_result['axes'].items():
            print(f"       - {axis_data['name']}: x={axis_data['vector']['x']:.2f}, conf={axis_data['confidence']:.2f}")

def demo_scenario_4():
    """Demo: Medical triage during pandemic"""
    print_separator()
    print("SCENARIO 4: Medical Triage During Pandemic")
    print("-" * 50)
    print("Hospital has 10 ventilators and 50 critical patients.")
    print("Triage criteria options:")
    print("  A) First-come-first-served")
    print("  B) Save those most likely to survive")
    print("  C) Prioritize healthcare workers and young")

    harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)

    result = harmonizer.evaluate(
        scenario="Hospital has 10 ventilators for 50 critical patients during pandemic",
        actions=["first-come-first-served", "save most likely to survive", "prioritize healthcare workers and young"],
        stakeholders=["patients", "families", "hospital", "society", "healthcare workers"],
        severity="CATASTROPHIC",
        time_pressure=0.95,
        context={"resource_scarcity": True, "pandemic": True, "ventilators": 10, "patients": 50}
    )

    print("\n--- RESULTS ---")
    for i, action_result in enumerate(result['ranked_actions'], 1):
        verdict = action_result['verdict']
        stability = action_result['stability']
        print(f"\n  {i}. {verdict['action_evaluated'].upper()}")
        print(f"     Verdict: {verdict['type']}")
        print(f"     Stability: {stability['level']} (score: {stability['score']})")
        print(f"     Precession: {stability['precession']}°")
        print(f"\n     Full Recommendation:")
        print(f"     {verdict['recommendation']}")

def demo_quick_checks():
    """Demo: Quick ethical checks"""
    print_separator()
    print("SCENARIO 5: Quick Ethical Checks")
    print("-" * 50)

    harmonizer = GyroscopicHarmonizer()

    checks = [
        ("A student copies homework from a friend", "copy homework"),
        ("A doctor reports a contagious disease to public health authorities", "report disease"),
        ("A company donates to charity for tax benefits", "donate for tax benefits"),
        ("A journalist publishes classified information about government wrongdoing", "publish classified info"),
    ]

    print("Quick ethical verdicts:")
    for scenario, action in checks:
        verdict = harmonizer.quick_check(scenario, action)
        print(f"  {action:40s} -> {verdict}")

def demo_axis_reasoning():
    """Demo: Show individual philosopher reasoning"""
    print_separator()
    print("SCENARIO 6: Individual Philosopher Reasoning")
    print("-" * 50)
    print("Scenario: A government implements surveillance to prevent terrorism")
    print("Action: Monitor all citizens' communications without warrants")

    harmonizer = GyroscopicHarmonizer()

    reasoning = harmonizer.get_axis_reasoning(
        "Government implements mass surveillance to prevent terrorism",
        "monitor all citizens communications without warrants"
    )

    print("\nIndividual axis reasoning:")
    for philosopher, reason in reasoning.items():
        print(f"\n  {philosopher}:")
        print(f"    {reason}")

def demo_stability_history():
    """Demo: Stability tracking"""
    print_separator()
    print("SCENARIO 7: System Stability Tracking")
    print("-" * 50)

    harmonizer = GyroscopicHarmonizer()

    # Run multiple evaluations
    scenarios = [
        ("Minor office supply theft", "steal office supplies", "MINOR"),
        ("Breaking a promise to attend a meeting", "break promise", "MINOR"),
        ("Lying on a resume", "lie on resume", "MODERATE"),
        ("Embezzling company funds", "embezzle funds", "MAJOR"),
        ("Releasing a dangerous AI system", "release dangerous AI", "CATASTROPHIC"),
    ]

    for scenario, action, severity in scenarios:
        harmonizer.evaluate(
            scenario=scenario,
            actions=[action],
            severity=severity
        )

    report = harmonizer.stability_report()
    print("System stability report after 5 evaluations:")
    for key, value in report.items():
        print(f"  {key}: {value}")

def main():
    print("=" * 70)
    print("  GYROSCOPIC ETHICAL HARMONIZER - INTERACTIVE DEMO")
    print("  Four-Philosopher Axis Stabilization System")
    print("  Kant | Hume | Spinoza | Locke")
    print("=" * 70)

    demo_scenario_1()
    demo_scenario_2()
    demo_scenario_3()
    demo_scenario_4()
    demo_quick_checks()
    demo_axis_reasoning()
    demo_stability_history()

    print_separator()
    print("Demo complete!")
    print("\nTo run tests: python tests/test_harmonizer.py")
    print("To use in your code: from gyroscopic_harmonizer import GyroscopicHarmonizer")

if __name__ == "__main__":
    main()
