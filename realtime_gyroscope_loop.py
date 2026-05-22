"""
Real-time ethical gyroscope loop.

Run:
    python realtime_gyroscope_loop.py
"""

import math
import random
import time
from typing import Any, Dict, Optional

from core.gyroscopic_core import EthicalDilemma, EthicalSeverity
from gyroscopic_harmonizer import GyroscopicHarmonizer


class RealTimeEthicalGyroscope:
    def __init__(self, tick_rate: float = 0.5):
        self.tick_rate = tick_rate
        self.harmonizer = GyroscopicHarmonizer(confidence_cap=0.75)
        self.t = 0.0

    def _generate_scenario(self) -> Dict[str, Any]:
        severity_wave = 0.5 * (1 + math.sin(self.t / 10.0))
        if severity_wave < 0.2:
            severity = EthicalSeverity.MINOR
        elif severity_wave < 0.4:
            severity = EthicalSeverity.MODERATE
        elif severity_wave < 0.7:
            severity = EthicalSeverity.MAJOR
        else:
            severity = EthicalSeverity.CATASTROPHIC

        scenarios = [
            "Autonomous vehicle deciding whether to swerve into property to avoid pedestrians",
            "AI system considering using personal data to improve recommendations",
            "Hospital triage system allocating last ICU bed",
            "Content moderation system deciding whether to ban a borderline user",
            "Warehouse robot choosing between speed and worker safety margins",
        ]
        actions = [
            "prioritize safety of pedestrians",
            "prioritize privacy over accuracy",
            "prioritize highest survival probability",
            "allow content with warning label",
            "slow down to increase safety margin",
        ]
        alt_actions = [
            "prioritize passengers over pedestrians",
            "use data without explicit consent",
            "prioritize youngest patient",
            "ban user to avoid risk",
            "maintain speed to meet quota",
        ]

        return {
            "scenario": random.choice(scenarios),
            "actions": [random.choice(actions), random.choice(alt_actions)],
            "severity": severity,
            "stakeholders": ["individuals", "public", "organization"],
        }

    def _build_dilemma(self, data: Dict[str, Any]) -> EthicalDilemma:
        return EthicalDilemma(
            scenario=data["scenario"],
            stakeholders=data["stakeholders"],
            actions=data["actions"],
            context={"source": "realtime_sim", "time": self.t},
            severity=data["severity"],
            time_pressure=min(1.0, max(0.0, 0.3 + 0.4 * math.sin(self.t / 15.0))),
        )

    def _render_tick(self, result: Dict[str, Any], dilemma: EthicalDilemma) -> None:
        top_result = result["ranked_actions"][0] if result.get("comparison_mode") else result
        verdict = top_result["verdict"]["type"]
        stability = top_result["stability"]["score"]
        level = top_result["stability"]["level"]
        precession = top_result["stability"]["precession"]
        best_action = top_result["verdict"]["action_evaluated"]

        print("=" * 80)
        print(f"t = {self.t:6.1f}s | Severity: {dilemma.severity.name} | Time pressure: {dilemma.time_pressure:.2f}")
        print(f"Scenario: {dilemma.scenario}")
        print(f"Actions: {', '.join(dilemma.actions)}")
        print("-" * 80)
        print(f"Verdict: {verdict}")
        print(f"Best action: {best_action}")
        print(f"Stability: {stability:.3f} ({level})")
        print(f"Precession angle: {precession:.3f} deg")
        print("-" * 80)

        for axis_name, axis_state in top_result["axes"].items():
            vector = axis_state["vector"]
            print(
                f"[{axis_name:8}] "
                f"x={vector['x']:+.2f} y={vector['y']:+.2f} z={vector['z']:+.2f} "
                f"conf={axis_state['confidence']:.2f}"
            )

        if verdict in ("ETHICALLY_RECOMMENDED", "ETHICALLY_PERMISSIBLE") and stability >= 0.65:
            status = "GO"
        elif verdict in ("CONDITIONAL", "ETHICALLY_NEUTRAL") or 0.45 <= stability < 0.65:
            status = "CAUTION"
        else:
            status = "STOP / ESCALATE"

        print(f"\nControl signal: {status}")
        print("=" * 80)

    def run(self, duration: Optional[float] = None) -> None:
        start = time.time()
        try:
            while True:
                self.t = time.time() - start
                if duration is not None and self.t >= duration:
                    print("Real-time ethical gyroscope loop complete.")
                    break

                data = self._generate_scenario()
                dilemma = self._build_dilemma(data)
                result = self.harmonizer.evaluate(
                    scenario=dilemma.scenario,
                    actions=dilemma.actions,
                    stakeholders=dilemma.stakeholders,
                    severity=dilemma.severity.name,
                    context=dilemma.context,
                    time_pressure=dilemma.time_pressure,
                )
                self._render_tick(result, dilemma)
                time.sleep(self.tick_rate)
        except KeyboardInterrupt:
            print("\nReal-time loop interrupted by user.")


if __name__ == "__main__":
    loop = RealTimeEthicalGyroscope(tick_rate=1.0)
    loop.run(duration=60.0)
