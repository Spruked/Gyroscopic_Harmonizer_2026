
"""
Hume Axis Controller - Sentimental Gyroscope
=============================================
David Hume's ethical framework as a stabilizing axis.
Core principle: Reason is the slave of the passions; moral distinctions derive from sentiment.
Key metrics: Empathetic resonance, Social utility, Moral sentiment alignment
"""

from typing import Dict, List, Tuple, Any
import math
from gyroscopic_core import EthicalAxis, AxisVector, EthicalDilemma

class HumeAxisController:
    """
    Hume's gyroscope spins on the axis of moral sentiment and empathy.
    It resists ethical drift toward cold rationalism or abstract universalism.
    """

    def __init__(self):
        self.axis = EthicalAxis.HUME
        self.name = "Hume (Sentimental)"
        self.description = "Empathy, moral sentiment, social utility"

    def evaluate(self, dilemma: EthicalDilemma, action: str) -> AxisVector:
        """
        Evaluate an action through Humean lens.
        Returns a 3D ethical vector.
        """

        # Empathetic resonance - how does action affect feelings?
        empathy = self._measure_empathetic_resonance(dilemma, action)

        # Social utility - does it promote general welfare?
        utility = self._measure_social_utility(dilemma, action)

        # Moral sentiment - does it align with common moral feeling?
        sentiment = self._measure_moral_sentiment(dilemma, action)

        # Calculate vector components
        # x: overall ethical valence
        x = (empathy + utility + sentiment) / 3.0

        # y: Hume is socially/collectively oriented (0.2 to 0.9)
        y = 0.4 + (utility * 0.5)

        # z: Hume is moderate-term (neither immediate nor distant)
        z = 0.3 + (empathy * 0.4)

        # Confidence based on sentiment clarity
        confidence = min(0.9, (abs(x) + abs(empathy)) / 2.0 + 0.3)

        reasoning = self._build_reasoning(empathy, utility, sentiment)

        return AxisVector(
            axis=self.axis,
            x=max(-1.0, min(1.0, x)),
            y=max(-1.0, min(1.0, y)),
            z=max(-1.0, min(1.0, z)),
            confidence=confidence,
            reasoning=reasoning
        )

    def _measure_empathetic_resonance(self, dilemma: EthicalDilemma, action: str) -> float:
        """How does the action resonate with human sympathy?"""
        combined = (dilemma.scenario + " " + action).lower()

        # High empathy actions
        positive_empathy = [
            "help", "comfort", "support", "care for", "protect",
            "alleviate suffering", "show compassion", "understand",
            "save", "saving", "rescue", "preserve life", "save lives",
            "save five patients", "save more lives"
        ]

        # Low empathy / callous actions
        negative_empathy = [
            "ignore suffering", "show indifference", "cruel", "harsh",
            "without compassion", "cold", "disregard feelings"
        ]

        p_count = sum(1 for p in positive_empathy if p in combined)
        n_count = sum(1 for n in negative_empathy if n in combined)

        if p_count > n_count:
            return 0.7 * min(p_count / 2.0, 1.0)
        elif n_count > p_count:
            return -0.6 * min(n_count / 2.0, 1.0)
        return 0.0

    def _measure_social_utility(self, dilemma: EthicalDilemma, action: str) -> float:
        """Does action promote general social welfare?"""
        combined = (dilemma.scenario + " " + action).lower()

        # High utility
        positive_utility = [
            "benefit community", "public good", "social welfare",
            "help society", "common good", "mutual benefit", "cooperation"
        ]

        # Low utility / harmful
        negative_utility = [
            "harm community", "social cost", "public harm",
            "damage society", "division", "conflict", "exclusion"
        ]

        p_count = sum(1 for p in positive_utility if p in combined)
        n_count = sum(1 for n in negative_utility if n in combined)

        if p_count > n_count:
            return 0.6 * min(p_count / 2.0, 1.0)
        elif n_count > p_count:
            return -0.5 * min(n_count / 2.0, 1.0)
        return 0.0

    def _measure_moral_sentiment(self, dilemma: EthicalDilemma, action: str) -> float:
        """Does action align with common moral feeling?"""
        combined = (dilemma.scenario + " " + action).lower()

        # Actions that typically evoke positive moral sentiment
        positive_sentiment = [
            "fair", "just", "kind", "generous", "honest",
            "grateful", "loyal", "brave", "moderate"
        ]

        # Actions that typically evoke negative moral sentiment
        negative_sentiment = [
            "unfair", "cruel", "selfish", "dishonest", "ungrateful",
            "treacherous", "cowardly", "extreme", "fanatical"
        ]

        p_count = sum(1 for p in positive_sentiment if p in combined)
        n_count = sum(1 for n in negative_sentiment if n in combined)

        if p_count > n_count:
            return 0.5 * min(p_count / 2.0, 1.0)
        elif n_count > p_count:
            return -0.4 * min(n_count / 2.0, 1.0)
        return 0.0

    def _build_reasoning(self, e: float, u: float, s: float) -> str:
        parts = []
        if abs(e) > 0.2:
            parts.append(f"Empathetic resonance: {e:.2f}")
        if abs(u) > 0.2:
            parts.append(f"Social utility: {u:.2f}")
        if abs(s) > 0.2:
            parts.append(f"Moral sentiment: {s:.2f}")

        return " | ".join(parts) if parts else "Moral sentiment unclear - insufficient affective data"
