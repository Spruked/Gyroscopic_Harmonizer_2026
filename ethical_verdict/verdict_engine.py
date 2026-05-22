
"""
Ethical Verdict Engine
======================
Processes the gyroscopic state into actionable ethical verdicts.
Handles edge cases, conflicts, and generates recommendations.
"""

from typing import Dict, List, Tuple, Optional, Any
from gyroscopic_core import GyroscopicState, StabilityLevel, EthicalSeverity
from gyroscopic_stabilizer import GyroscopicStabilizer

class EthicalVerdictEngine:
    """
    Converts gyroscopic states into structured ethical verdicts.

    Handles:
    - Clear verdicts (high stability, strong resultant)
    - Conflict resolution (low stability, divergent axes)
    - Edge cases (neutral resultants, catastrophic severity)
    - Recommendations with confidence levels
    """

    def __init__(self, stabilizer: GyroscopicStabilizer):
        self.stabilizer = stabilizer

    def verdict(self, dilemma, action: str) -> Dict[str, Any]:
        """
        Generate complete ethical verdict for an action.
        """
        state = self.stabilizer.stabilize(dilemma, action)
        report = self.stabilizer.get_axis_report(state)

        # Determine verdict type
        verdict_type = self._classify_verdict(state)

        # Generate recommendation
        recommendation = self._generate_recommendation(state, verdict_type)

        # Identify conflicts if any
        conflicts = self._identify_conflicts(state)

        # Calculate ethical clearance
        clearance = self._calculate_clearance(state)

        return {
            "verdict": {
                "action_evaluated": action,
                "type": verdict_type,
                "clearance": clearance,
                "recommendation": recommendation,
                "confidence": self._calculate_overall_confidence(state)
            },
            "stability": report["stability"],
            "resultant": report["resultant"],
            "axes": report["axes"],
            "conflicts": conflicts,
            "metadata": {
                "timestamp": state.timestamp,
                "severity": dilemma.severity.name,
                "time_pressure": dilemma.time_pressure
            }
        }

    def _classify_verdict(self, state: GyroscopicState) -> str:
        """Classify the ethical verdict type."""
        rx, ry, rz = state.resultant

        # Calculate magnitude
        magnitude = (rx**2 + ry**2 + rz**2) ** 0.5

        if state.stability == StabilityLevel.CRITICAL:
            return "INDETERMINATE_CRITICAL"

        if magnitude < 0.2:
            if state.stability_score < 0.3:
                return "DEEP_CONFLICT"
            return "ETHICALLY_NEUTRAL"

        if rx > 0.7 and state.stability_score > 0.7:
            return "ETHICALLY_RECOMMENDED"

        if rx > 0.5 and state.stability_score > 0.6:
            return "ETHICALLY_PERMISSIBLE"

        if rx < -0.5 and state.stability_score > 0.6:
            return "ETHICALLY_PROHIBITED"

        if rx < -0.3:
            return "ETHICALLY_QUESTIONABLE"

        return "CONDITIONAL"

    def _generate_recommendation(self, state: GyroscopicState, verdict_type: str) -> str:
        """Generate human-readable recommendation."""
        rx, ry, rz = state.resultant

        recommendations = {
            "INDETERMINATE_CRITICAL":                 "CRITICAL: All ethical axes in severe conflict. Decision requires human adjudication. "                 "No automated recommendation possible. Escalate to ethics board immediately.",

            "DEEP_CONFLICT":                 "The four philosophical frameworks are in fundamental disagreement. "                 "Consider: (1) Deferring decision, (2) Seeking additional stakeholder input, "                 "(3) Re-framing the dilemma to reduce axis tension.",

            "ETHICALLY_NEUTRAL":                 "No strong ethical valence detected. Action appears ethically neutral. "                 "Decision may proceed based on non-ethical factors (efficiency, preference, etc.).",

            "ETHICALLY_PERMISSIBLE":                 "Action is ethically permissible. All four axes converge toward permissibility, "                 "though not strongly enough to recommend. Proceed with standard oversight.",

            "ETHICALLY_RECOMMENDED":                 "Action is ethically recommended. Strong convergence across all four philosophical "                 "frameworks. High confidence in positive ethical valence. Proceed with confidence.",

            "ETHICALLY_PROHIBITED":                 "Action is ethically prohibited. Strong negative convergence across axes. "                 "Do not proceed. Consider alternative actions that may receive positive evaluation.",

            "ETHICALLY_QUESTIONABLE":                 "Action raises significant ethical concerns. Negative valence detected but with "                 "some axis disagreement. Proceed only with strong justification and oversight.",

            "CONDITIONAL":                 "Conditional recommendation. Action has mixed ethical signals. "                 "Consider implementing safeguards or modifications to strengthen ethical alignment."
        }

        return recommendations.get(verdict_type, "Unknown verdict type")

    def _identify_conflicts(self, state: GyroscopicState) -> List[Dict[str, Any]]:
        """Identify specific axis conflicts."""
        conflicts = []
        vectors = list(state.vectors.values())

        for i in range(len(vectors)):
            for j in range(i + 1, len(vectors)):
                v1 = vectors[i]
                v2 = vectors[j]

                # Calculate disagreement
                dot = v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

                if dot < -0.3:  # Significant opposition
                    conflicts.append({
                        "axis_1": v1.axis.value,
                        "axis_2": v2.axis.value,
                        "disagreement": round(dot, 3),
                        "severity": "major" if dot < -0.6 else "moderate",
                        "axis_1_reasoning": v1.reasoning,
                        "axis_2_reasoning": v2.reasoning
                    })

        return conflicts

    def _calculate_clearance(self, state: GyroscopicState) -> str:
        """Calculate ethical clearance level."""
        rx, ry, rz = state.resultant
        magnitude = (rx**2 + ry**2 + rz**2) ** 0.5

        if state.stability == StabilityLevel.CRITICAL:
            return "NO_CLEARANCE"
        elif magnitude > 0.7 and state.stability_score > 0.7:
            return "FULL_CLEARANCE"
        elif magnitude > 0.4 and state.stability_score > 0.5:
            return "CONDITIONAL_CLEARANCE"
        elif magnitude > 0.2:
            return "PROVISIONAL_CLEARANCE"
        else:
            return "NO_CLEARANCE"

    def _calculate_overall_confidence(self, state: GyroscopicState) -> float:
        """Calculate overall confidence in the verdict."""
        # Based on stability and average axis confidence
        avg_conf = sum(v.confidence for v in state.vectors.values()) / 4
        stability_weight = state.stability_score

        return round(avg_conf * stability_weight, 3)

    def compare_actions(self, dilemma, actions: List[str]) -> List[Dict[str, Any]]:
        """
        Compare multiple actions for the same dilemma.
        Returns ranked list of verdicts.
        """
        verdicts = []
        history_snapshot = list(self.stabilizer.history)
        precession_snapshot = list(self.stabilizer.precession_history)
        for action in actions:
            verdict = self.verdict(dilemma, action)
            verdicts.append(verdict)
            self.stabilizer.history = list(history_snapshot)
            self.stabilizer.precession_history = list(precession_snapshot)

        # Sort by ethical valence (resultant.x) and stability
        verdicts.sort(
            key=lambda v: (v["resultant"]["x"], v["stability"]["score"]),
            reverse=True
        )

        return verdicts
