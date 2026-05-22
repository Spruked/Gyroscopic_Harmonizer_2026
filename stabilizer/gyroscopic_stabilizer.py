
"""
Gyroscopic Stabilizer
=====================
The central harmonizer that combines four philosophical axes into a stable ethical frame.
Uses gyroscopic physics principles: precession, nutation, and angular momentum conservation.
"""

from typing import Dict, List, Tuple, Optional, Any
import math
from datetime import datetime
from gyroscopic_core import (
    EthicalAxis, AxisVector, GyroscopicState, 
    EthicalDilemma, StabilityLevel
)
from kant_axis import KantAxisController
from hume_axis import HumeAxisController
from spinoza_axis import SpinozaAxisController
from locke_axis import LockeAxisController

class GyroscopicStabilizer:
    """
    Four-axis gyroscopic stabilizer for ethical decision-making.

    Like a mechanical gyroscope, each philosopher provides angular momentum
    that resists ethical drift. When axes align, the system is stable.
    When they conflict, the system experiences precession (ethical drift)
    that must be actively corrected.
    """

    def __init__(self, confidence_cap: float = 0.75):
        self.axes = {
            EthicalAxis.KANT: KantAxisController(),
            EthicalAxis.HUME: HumeAxisController(),
            EthicalAxis.SPINOZA: SpinozaAxisController(),
            EthicalAxis.LOCKE: LockeAxisController()
        }
        self.confidence_cap = confidence_cap
        self.history: List[GyroscopicState] = []
        self.precession_history: List[float] = []

    def stabilize(self, dilemma: EthicalDilemma, action: str) -> GyroscopicState:
        """
        Run all four axes and compute the stabilized ethical verdict.

        Args:
            dilemma: The ethical situation
            action: The proposed action to evaluate

        Returns:
            GyroscopicState containing all axis vectors, resultant, and stability
        """
        # Evaluate through all four philosophical lenses
        vectors = {}
        for axis_enum, controller in self.axes.items():
            vector = controller.evaluate(dilemma, action)
            # Apply confidence cap under tension (per your system rules)
            if self._detect_peer_tension(dilemma):
                vector.confidence = min(vector.confidence, self.confidence_cap)
            vectors[axis_enum] = vector

        # Compute resultant vector (weighted by confidence)
        resultant = self._compute_resultant(vectors)

        # Calculate stability metrics
        stability_score = self._calculate_stability(vectors)
        stability_level = self._classify_stability(stability_score)

        # Calculate precession (how much ethical frame has shifted from previous)
        precession = self._calculate_precession(resultant)

        state = GyroscopicState(
            timestamp=datetime.utcnow().isoformat(),
            vectors=vectors,
            resultant=resultant,
            stability=stability_level,
            stability_score=stability_score,
            precession_angle=precession
        )

        self.history.append(state)
        self.precession_history.append(precession)

        return state

    def _detect_peer_tension(self, dilemma: EthicalDilemma) -> bool:
        """Detect if there is peer tension requiring confidence cap."""
        # Tension detected for high-severity dilemmas or time pressure
        return (dilemma.severity.value >= 4 or dilemma.time_pressure > 0.7)

    def _compute_resultant(self, vectors: Dict[EthicalAxis, AxisVector]) -> Tuple[float, float, float]:
        """
        Compute the equal-weight resultant vector.
        Each philosopher axis contributes exactly 25% of the final direction.
        """
        if not vectors:
            return (0.0, 0.0, 0.0)

        rx, ry, rz = 0.0, 0.0, 0.0

        for vector in vectors.values():
            rx += vector.x
            ry += vector.y
            rz += vector.z

        axis_count = len(vectors)
        return (
            rx / axis_count,
            ry / axis_count,
            rz / axis_count
        )

    def _calculate_stability(self, vectors: Dict[EthicalAxis, AxisVector]) -> float:
        """
        Calculate stability score (0 to 1).

        Stability is high when:
        1. All axes point in similar directions (low angular dispersion)
        2. All axes have reasonable confidence
        3. No axis is in strong opposition to the resultant
        """
        axis_values = list(vectors.values())
        if len(axis_values) < 2:
            return 0.25

        # Ethical agreement should be driven primarily by valence. The y/z
        # coordinates describe orientation, but their defaults can otherwise
        # make unrelated low-evidence inputs look artificially stable.
        valences = [v.x for v in axis_values]
        avg_confidence = sum(v.confidence for v in axis_values) / len(axis_values)
        avg_evidence = sum(abs(v.x) for v in axis_values) / len(axis_values)

        pair_scores = []
        for i in range(len(valences)):
            for j in range(i + 1, len(valences)):
                distance = abs(valences[i] - valences[j])
                pair_scores.append(1.0 - min(distance / 2.0, 1.0))

        valence_alignment = sum(pair_scores) / len(pair_scores) if pair_scores else 0.0

        has_positive = any(v > 0.2 for v in valences)
        has_negative = any(v < -0.2 for v in valences)
        conflict_penalty = 0.25 if has_positive and has_negative else 0.0

        evidence_factor = min(1.0, avg_evidence * 2.5)
        if evidence_factor < 0.25:
            # Low-information inputs should remain indeterminate/turbulent,
            # not become stable just because every axis stayed near default.
            return max(0.2, min(0.44, 0.25 + avg_confidence * 0.25))

        stability = (
            valence_alignment * 0.45 +
            avg_confidence * 0.30 +
            evidence_factor * 0.25 -
            conflict_penalty
        )

        return max(0.0, min(1.0, stability))

    def _classify_stability(self, score: float) -> StabilityLevel:
        """Classify stability score into level."""
        if score >= 0.85:
            return StabilityLevel.HARMONIZED
        elif score >= 0.65:
            return StabilityLevel.STABLE
        elif score >= 0.45:
            return StabilityLevel.TURBULENT
        elif score >= 0.25:
            return StabilityLevel.UNSTABLE
        else:
            return StabilityLevel.CRITICAL

    def _calculate_precession(self, resultant: Tuple[float, float, float]) -> float:
        """
        Calculate precession angle from previous state.
        Precession indicates ethical drift between decisions.
        """
        if not self.history:
            return 0.0

        prev = self.history[-1].resultant

        # Calculate angle between current and previous resultant
        dot = (resultant[0] * prev[0] + resultant[1] * prev[1] + resultant[2] * prev[2])

        mag_curr = math.sqrt(resultant[0]**2 + resultant[1]**2 + resultant[2]**2)
        mag_prev = math.sqrt(prev[0]**2 + prev[1]**2 + prev[2]**2)

        if mag_curr == 0 or mag_prev == 0:
            return 0.0

        cos_angle = dot / (mag_curr * mag_prev)
        cos_angle = max(-1.0, min(1.0, cos_angle))

        angle = math.acos(cos_angle)
        return math.degrees(angle)

    def get_axis_report(self, state: GyroscopicState) -> Dict[str, Any]:
        """Generate human-readable report of axis evaluations."""
        report = {
            "timestamp": state.timestamp,
            "stability": {
                "level": state.stability.name,
                "score": round(state.stability_score, 3),
                "precession": round(state.precession_angle, 2)
            },
            "resultant": {
                "x": round(state.resultant[0], 3),
                "y": round(state.resultant[1], 3),
                "z": round(state.resultant[2], 3)
            },
            "axes": {}
        }

        for axis_enum, vector in state.vectors.items():
            report["axes"][axis_enum.value] = {
                "name": self.axes[axis_enum].name,
                "vector": {
                    "x": round(vector.x, 3),
                    "y": round(vector.y, 3),
                    "z": round(vector.z, 3)
                },
                "confidence": round(vector.confidence, 3),
                "reasoning": vector.reasoning
            }

        return report
