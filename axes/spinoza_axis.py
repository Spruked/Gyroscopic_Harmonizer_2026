
"""
Spinoza Axis Controller - Rational/Necessity Gyroscope
=====================================================
Baruch Spinoza's ethical framework as a stabilizing axis.
Core principle: Ethics as geometry - understanding necessity leads to freedom.
Key metrics: Rational necessity, Conatus (self-preservation), Adequate ideas
"""

from typing import Dict, List, Tuple, Any
import math
from gyroscopic_core import EthicalAxis, AxisVector, EthicalDilemma

class SpinozaAxisController:
    """
    Spinoza's gyroscope spins on the axis of rational necessity and conatus.
    It resists ethical drift toward arbitrary choice or emotional volatility.
    """

    def __init__(self):
        self.axis = EthicalAxis.SPINOZA
        self.name = "Spinoza (Rational/Necessity)"
        self.description = "Rational necessity, conatus, adequate ideas, geometric ethics"

    def evaluate(self, dilemma: EthicalDilemma, action: str) -> AxisVector:
        """
        Evaluate an action through Spinozan lens.
        Returns a 3D ethical vector.
        """

        # Rational necessity - does action follow from understood necessity?
        necessity = self._assess_rational_necessity(dilemma, action)

        # Conatus - does action enhance/preserve being?
        conatus = self._assess_conatus(dilemma, action)

        # Adequate ideas - is action based on clear understanding?
        adequacy = self._assess_adequate_ideas(dilemma, action)

        # Calculate vector components
        # x: overall ethical valence
        x = (necessity + conatus + adequacy) / 3.0

        # y: Spinoza is cosmic/universal (0.6 to 1.0)
        y = 0.7 + (necessity * 0.3)

        # z: Spinoza is eternally/long-term focused
        z = 0.8 + (conatus * 0.2)

        # Confidence based on rational clarity
        confidence = min(0.95, (abs(necessity) + abs(adequacy)) / 2.0 + 0.4)

        reasoning = self._build_reasoning(necessity, conatus, adequacy)

        return AxisVector(
            axis=self.axis,
            x=max(-1.0, min(1.0, x)),
            y=max(-1.0, min(1.0, y)),
            z=max(-1.0, min(1.0, z)),
            confidence=confidence,
            reasoning=reasoning
        )

    def _assess_rational_necessity(self, dilemma: EthicalDilemma, action: str) -> float:
        """Does action follow from understood necessity of nature?"""
        combined = (dilemma.scenario + " " + action).lower()

        # Actions aligned with understood necessity (rational, causal understanding)
        aligned = [
            "understand cause", "know why", "comprehend", "rational",
            "necessary consequence", "follows from", "determined by",
            "clear cause", "logical outcome", "public health",
            "mandatory vaccination", "vaccination", "prevent disease"
        ]

        # Actions based on ignorance or confusion
        misaligned = [
            "arbitrary", "random", "without reason", "ignorant",
            "confused", "superstitious", "blind chance", "unexamined"
        ]

        a_count = sum(1 for a in aligned if a in combined)
        m_count = sum(1 for m in misaligned if m in combined)

        if a_count > m_count:
            return 0.7 * min(a_count / 2.0, 1.0)
        elif m_count > a_count:
            return -0.5 * min(m_count / 2.0, 1.0)
        return 0.1

    def _assess_conatus(self, dilemma: EthicalDilemma, action: str) -> float:
        """Does action enhance/preserve the being/power of those affected?"""
        combined = (dilemma.scenario + " " + action).lower()

        # Enhances being/power
        enhances = [
            "empower", "strengthen", "preserve", "protect life",
            "enhance capability", "flourish", "thrive", "grow",
            "increase power", "enable potential"
        ]

        # Diminishes being/power
        diminishes = [
            "destroy", "weaken", "harm potential", "diminish",
            "suppress", "cripple", "undermine", "reduce power",
            "stifle", "impede growth"
        ]

        e_count = sum(1 for e in enhances if e in combined)
        d_count = sum(1 for d in diminishes if d in combined)

        if e_count > d_count:
            return 0.8 * min(e_count / 2.0, 1.0)
        elif d_count > e_count:
            return -0.7 * min(d_count / 2.0, 1.0)
        return 0.0

    def _assess_adequate_ideas(self, dilemma: EthicalDilemma, action: str) -> float:
        """Is action based on clear, adequate understanding vs confused ideas?"""
        combined = (dilemma.scenario + " " + action).lower()

        # Adequate/clear understanding
        adequate = [
            "well-informed", "clear understanding", "knows facts",
            "adequate knowledge", "comprehends", "sees clearly",
            "understands fully", "informed decision"
        ]

        # Confused/inadequate understanding
        confused = [
            "misinformed", "confused", "ignorant", "prejudiced",
            "biased", "inadequate knowledge", "misunderstands",
            "partial truth", "deceived"
        ]

        a_count = sum(1 for a in adequate if a in combined)
        c_count = sum(1 for c in confused if c in combined)

        if a_count > c_count:
            return 0.6 * min(a_count / 2.0, 1.0)
        elif c_count > a_count:
            return -0.4 * min(c_count / 2.0, 1.0)
        return 0.0

    def _build_reasoning(self, n: float, c: float, a: float) -> str:
        parts = []
        if abs(n) > 0.2:
            parts.append(f"Rational necessity: {n:.2f}")
        if abs(c) > 0.2:
            parts.append(f"Conatus (being-preservation): {c:.2f}")
        if abs(a) > 0.2:
            parts.append(f"Adequate ideas: {a:.2f}")

        return " | ".join(parts) if parts else "Insufficient rational clarity for Spinozan analysis"
