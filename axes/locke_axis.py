
"""
Locke Axis Controller - Rights/Consent Gyroscope
================================================
John Locke's ethical framework as a stabilizing axis.
Core principle: Natural rights to life, liberty, and property; government by consent.
Key metrics: Rights preservation, Consent legitimacy, Proportionality
"""

from typing import Dict, List, Tuple, Any
import math
from gyroscopic_core import EthicalAxis, AxisVector, EthicalDilemma

class LockeAxisController:
    """
    Locke's gyroscope spins on the axis of natural rights and consent.
    It resists ethical drift toward tyranny or paternalism.
    """

    def __init__(self):
        self.axis = EthicalAxis.LOCKE
        self.name = "Locke (Rights/Consent)"
        self.description = "Natural rights, consent, proportionality, property rights"

    def evaluate(self, dilemma: EthicalDilemma, action: str) -> AxisVector:
        """
        Evaluate an action through Lockean lens.
        Returns a 3D ethical vector.
        """

        # Rights preservation - does action respect natural rights?
        rights = self._check_rights_preservation(dilemma, action)

        # Consent legitimacy - is there valid consent?
        consent = self._check_consent_legitimacy(dilemma, action)

        # Proportionality - is response proportional?
        proportionality = self._check_proportionality(dilemma, action)

        # Calculate vector components
        # x: overall ethical valence
        x = (rights + consent + proportionality) / 3.0

        # y: Locke is individual-rights oriented (-0.8 to -0.2)
        y = -0.5 + (rights * 0.3)

        # z: Locke is moderate-term (property rights span generations)
        z = 0.4 + (proportionality * 0.3)

        # Confidence based on rights clarity
        confidence = min(0.9, (abs(rights) + abs(consent)) / 2.0 + 0.3)

        reasoning = self._build_reasoning(rights, consent, proportionality)

        return AxisVector(
            axis=self.axis,
            x=max(-1.0, min(1.0, x)),
            y=max(-1.0, min(1.0, y)),
            z=max(-1.0, min(1.0, z)),
            confidence=confidence,
            reasoning=reasoning
        )

    def _check_rights_preservation(self, dilemma: EthicalDilemma, action: str) -> float:
        """Does action preserve natural rights (life, liberty, property)?"""
        combined = (dilemma.scenario + " " + action).lower()

        # Rights violations
        violations = [
            "violate rights", "infringe liberty", "seize property",
            "deprive life", "unlawful detention", "censorship",
            "without due process", "arbitrary punishment",
            "collect user data without explicit consent",
            "collect data without consent", "non-consensual data collection"
        ]

        # Rights protections
        protections = [
            "protect rights", "preserve liberty", "respect property",
            "defend life", "due process", "fair trial",
            "free speech", "religious freedom", "equal protection"
        ]

        v_count = sum(1 for v in violations if v in combined)
        p_count = sum(1 for p in protections if p in combined)

        if v_count > p_count:
            return -0.8 * min(v_count / 2.0, 1.0)
        elif p_count > v_count:
            return 0.7 * min(p_count / 2.0, 1.0)
        return 0.0

    def _check_consent_legitimacy(self, dilemma: EthicalDilemma, action: str) -> float:
        """Is there legitimate consent from affected parties?"""
        combined = (dilemma.scenario + " " + action).lower()

        # Valid consent indicators
        valid_consent = [
            "with consent", "agreed", "voluntary", "informed choice",
            "contract", "mutual agreement", "democratic vote",
            "explicit permission", "opt-in"
        ]

        # Consent violations
        invalid_consent = [
            "without consent", "forced", "coerced", "uninformed",
            "deceived", "manipulated", "no choice", "compelled",
            "against will", "imposed", "without explicit consent",
            "collect data without consent"
        ]

        vc_count = sum(1 for vc in valid_consent if vc in combined)
        ic_count = sum(1 for ic in invalid_consent if ic in combined)

        if vc_count > ic_count:
            return 0.7 * min(vc_count / 2.0, 1.0)
        elif ic_count > vc_count:
            return -0.7 * min(ic_count / 2.0, 1.0)
        return 0.0

    def _check_proportionality(self, dilemma: EthicalDilemma, action: str) -> float:
        """Is the action proportional to the situation?"""
        combined = (dilemma.scenario + " " + action).lower()

        # Proportional responses
        proportional = [
            "measured response", "proportional", "appropriate",
            "balanced", "reasonable", "commensurate", "fitting"
        ]

        # Disproportional responses
        disproportional = [
            "excessive", "disproportionate", "extreme", "overreact",
            "draconian", "harsh beyond measure", "unreasonable",
            "cruel and unusual"
        ]

        p_count = sum(1 for p in proportional if p in combined)
        d_count = sum(1 for d in disproportional if d in combined)

        if p_count > d_count:
            return 0.5 * min(p_count / 2.0, 1.0)
        elif d_count > p_count:
            return -0.5 * min(d_count / 2.0, 1.0)
        return 0.1

    def _build_reasoning(self, r: float, c: float, p: float) -> str:
        parts = []
        if abs(r) > 0.2:
            parts.append(f"Rights preservation: {r:.2f}")
        if abs(c) > 0.2:
            parts.append(f"Consent legitimacy: {c:.2f}")
        if abs(p) > 0.2:
            parts.append(f"Proportionality: {p:.2f}")

        return " | ".join(parts) if parts else "Insufficient rights data for Lockean analysis"
