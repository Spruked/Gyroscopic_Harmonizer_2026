
"""
Gyroscopic Harmonizer Core
============================
Four-axis ethical stabilization system.
Each philosopher represents a stabilizing gyroscope that resists ethical drift.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any
from enum import Enum
import math
from datetime import datetime

class EthicalAxis(Enum):
    """The four philosophical gyroscopes"""
    KANT = "kant"           # Deontological axis - duty, universalizability
    HUME = "hume"           # Sentimental axis - empathy, moral sentiment
    SPINOZA = "spinoza"     # Rational axis - necessity, conatus, geometric ethics
    LOCKE = "locke"         # Rights axis - natural rights, consent, property

class StabilityLevel(Enum):
    """How well the gyroscopes are aligned"""
    CRITICAL = 0.0      # All axes in conflict - system unstable
    UNSTABLE = 0.25     # Major axis disagreement
    TURBULENT = 0.5     # Moderate disagreement, manageable
    STABLE = 0.75       # Good alignment
    HARMONIZED = 1.0    # All axes convergent - optimal ethical clarity

class EthicalSeverity(Enum):
    """Severity of the ethical decision"""
    TRIVIAL = 1
    MINOR = 2
    MODERATE = 3
    MAJOR = 4
    CATASTROPHIC = 5

@dataclass
class AxisVector:
    """A single philosopher's ethical vector"""
    axis: EthicalAxis
    x: float  # -1 to 1: negative to positive ethical valence
    y: float  # -1 to 1: individual vs collective
    z: float  # -1 to 1: immediate vs long-term
    confidence: float  # 0 to 1
    reasoning: str

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> 'AxisVector':
        mag = self.magnitude()
        if mag == 0:
            return self
        return AxisVector(
            axis=self.axis,
            x=self.x / mag,
            y=self.y / mag,
            z=self.z / mag,
            confidence=self.confidence,
            reasoning=self.reasoning
        )

@dataclass
class GyroscopicState:
    """Current state of the ethical gyroscope system"""
    timestamp: str
    vectors: Dict[EthicalAxis, AxisVector]
    resultant: Tuple[float, float, float]
    stability: StabilityLevel
    stability_score: float
    precession_angle: float  # How much the ethical frame has shifted

@dataclass
class EthicalDilemma:
    """Input to the harmonizer"""
    scenario: str
    stakeholders: List[str]
    actions: List[str]
    context: Dict[str, Any]
    severity: EthicalSeverity
    time_pressure: float  # 0 to 1
