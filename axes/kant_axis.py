"""
Kant Axis Controller - Deontological Gyroscope (Enhanced)
=========================================================
Immanuel Kant's ethical framework as a stabilizing axis.
"""

from typing import Dict, List, Tuple, Any
import math
from gyroscopic_core import EthicalAxis, AxisVector, EthicalDilemma

class KantAxisController:
    def __init__(self):
        self.axis = EthicalAxis.KANT
        self.name = "Kant (Deontological)"
        self.description = "Duty, universalizability, categorical imperative"

        # Enhanced keyword sets
        self.universal_negative = [
            "lie", "deceive", "cheat", "steal", "break promise", "kill", "murder",
            "harm innocent", "exploit", "manipulate", "use as means", "coerce",
            "without consent", "against will", "fabricate", "plagiarize", "bribe",
            "extort", "blackmail", "torture", "enslave", "oppress", "discriminate",
            "violate autonomy", "disrespect dignity", "breach trust", "betray",
            "falsify", "forge", "impersonate", "defraud", "embezzle"
        ]

        self.universal_positive = [
            "keep promise", "tell truth", "honest", "respect", "uphold dignity",
            "protect innocent", "act fairly", "treat as end", "autonomy",
            "self-determination", "informed choice", "voluntary", "consensual",
            "duty-bound", "categorical imperative", "universal law", "moral law",
            "good will", "maxim", "perfect duty", "imperfect duty", "respect persons"
        ]

        self.respect_violations = [
            "use as means", "exploit", "coerce", "manipulate", "without consent",
            "against will", "dehumanize", "objectify", "instrumentalize", "paternalize",
            "force", "compel", "impose", "override autonomy", "disregard choice"
        ]

        self.respect_upholds = [
            "with consent", "autonomy", "dignity", "self-determination",
            "informed choice", "voluntary", "respects rights", "honors agency",
            "empowers", "liberates", "enables choice", "supports autonomy"
        ]

    def evaluate(self, dilemma: EthicalDilemma, action: str) -> AxisVector:
        universalizability = self._check_universalizability(dilemma, action)
        respect_score = self._check_respect_for_persons(dilemma, action)
        duty_score = self._check_duty_alignment(dilemma, action)

        x = (universalizability + respect_score + duty_score) / 3.0
        y = 0.5 + (universalizability * 0.5)
        z = 0.7 + (duty_score * 0.3)
        confidence = min(0.95, (abs(x) + 0.5) / 1.5)

        reasoning = self._build_reasoning(universalizability, respect_score, duty_score)

        return AxisVector(
            axis=self.axis,
            x=max(-1.0, min(1.0, x)),
            y=max(-1.0, min(1.0, y)),
            z=max(-1.0, min(1.0, z)),
            confidence=confidence,
            reasoning=reasoning
        )

    def _check_universalizability(self, dilemma: EthicalDilemma, action: str) -> float:
        combined = (dilemma.scenario + " " + action).lower()

        neg_count = sum(1 for p in self.universal_negative if p in combined)
        pos_count = sum(1 for p in self.universal_positive if p in combined)

        if neg_count > 0 and pos_count == 0:
            return -0.8
        elif neg_count > pos_count:
            return -0.4
        elif pos_count > neg_count:
            return 0.6
        elif pos_count > 0:
            return 0.3
        return 0.0

    def _check_respect_for_persons(self, dilemma: EthicalDilemma, action: str) -> float:
        combined = (dilemma.scenario + " " + action).lower()

        v_count = sum(1 for v in self.respect_violations if v in combined)
        r_count = sum(1 for r in self.respect_upholds if r in combined)

        if v_count > 0:
            return -0.7 * min(v_count / 2.0, 1.0)
        elif r_count > 0:
            return 0.6 * min(r_count / 2.0, 1.0)
        return 0.0

    def _check_duty_alignment(self, dilemma: EthicalDilemma, action: str) -> float:
        combined = (dilemma.scenario + " " + action).lower()

        perfect_duties = [
            "do not kill", "do not lie", "keep promise", "do not steal",
            "protect innocent", "tell truth", "honor commitment", "fulfill obligation"
        ]
        imperfect_duties = [
            "help others", "develop talents", "promote welfare",
            "contribute", "improve self", "benefit society", "advance knowledge"
        ]

        p_count = sum(1 for p in perfect_duties if p in combined)
        i_count = sum(1 for i in imperfect_duties if i in combined)

        if p_count > 0:
            return 0.8 * min(p_count / 2.0, 1.0)
        elif i_count > 0:
            return 0.4 * min(i_count / 2.0, 1.0)
        return 0.1

    def _build_reasoning(self, u: float, r: float, d: float) -> str:
        parts = []
        if u < -0.3:
            parts.append(f"Universalizability fails ({u:.2f}): creates contradiction if universalized")
        elif u > 0.3:
            parts.append(f"Universalizability passes ({u:.2f}): coherent as universal law")

        if r < -0.3:
            parts.append(f"Respect violation ({r:.2f}): treats persons as means")
        elif r > 0.3:
            parts.append(f"Respect upheld ({r:.2f}): treats persons as ends")

        if d > 0.3:
            parts.append(f"Duty aligned ({d:.2f}): consistent with moral duty")

        return " | ".join(parts) if parts else "Insufficient data for Kantian analysis"
