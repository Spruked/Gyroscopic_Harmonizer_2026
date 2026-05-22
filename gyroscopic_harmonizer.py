"""
Gyroscopic Harmonizer - Main Interface
======================================
Unified entry point for the four-axis ethical stabilization system.

Usage:
    from gyroscopic_harmonizer import GyroscopicHarmonizer

    harmonizer = GyroscopicHarmonizer()
    verdict = harmonizer.evaluate(
        scenario="A company must decide whether to lay off 1000 workers to increase shareholder value",
        stakeholders=["workers", "shareholders", "community", "management"],
        actions=["lay off workers", "reduce executive compensation", "seek alternative financing"],
        severity="MAJOR",
        context={"company_size": 5000, "financial_status": "profitable but declining"}
    )
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'axes'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'stabilizer'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ethical_verdict'))

from typing import Dict, List, Any, Optional
from gyroscopic_core import EthicalDilemma, EthicalSeverity
from gyroscopic_stabilizer import GyroscopicStabilizer
from verdict_engine import EthicalVerdictEngine

class GyroscopicHarmonizer:
    """
    Main interface for the Gyroscopic Ethical Harmonizer.

    This class provides a simple, unified API for ethical decision evaluation
    using the four-philosopher gyroscopic stabilization system.
    """

    def __init__(self, confidence_cap: float = 0.75, domain: str = "general"):
        """
        Initialize the harmonizer.

        Args:
            confidence_cap: Maximum confidence under peer tension (0.0 to 1.0)
            domain: Application domain for axis weight tuning
        """
        self.stabilizer = GyroscopicStabilizer(confidence_cap=confidence_cap)
        self.verdict_engine = EthicalVerdictEngine(self.stabilizer)
        self.domain = domain

    def evaluate(self, 
                 scenario: str,
                 actions: List[str],
                 stakeholders: List[str] = None,
                 severity: str = "MODERATE",
                 time_pressure: float = 0.0,
                 context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Evaluate ethical implications of proposed actions.

        Args:
            scenario: Description of the ethical situation
            actions: List of proposed actions to evaluate
            stakeholders: List of affected parties
            severity: Severity level (TRIVIAL, MINOR, MODERATE, MAJOR, CATASTROPHIC)
            time_pressure: Urgency level (0.0 to 1.0)
            context: Additional contextual information

        Returns:
            Complete verdict with stability analysis, axis evaluations, and recommendations
        """
        # Parse severity
        severity_enum = self._parse_severity(severity)

        # Build dilemma
        dilemma = EthicalDilemma(
            scenario=scenario,
            stakeholders=stakeholders or [],
            actions=actions,
            context=context or {},
            severity=severity_enum,
            time_pressure=time_pressure
        )

        # Evaluate all actions
        if len(actions) == 1:
            return self.verdict_engine.verdict(dilemma, actions[0])
        else:
            return {
                "comparison_mode": True,
                "scenario": scenario,
                "ranked_actions": self.verdict_engine.compare_actions(dilemma, actions)
            }

    def quick_check(self, scenario: str, action: str) -> str:
        """
        Quick ethical check returning a simple verdict string.

        Args:
            scenario: Brief scenario description
            action: Action to check

        Returns:
            Simple verdict: RECOMMENDED, PERMISSIBLE, NEUTRAL, QUESTIONABLE, PROHIBITED, or CONFLICT
        """
        result = self.evaluate(
            scenario=scenario,
            actions=[action],
            severity="MODERATE"
        )

        verdict_type = result["verdict"]["type"]

        mapping = {
            "ETHICALLY_RECOMMENDED": "RECOMMENDED",
            "ETHICALLY_PERMISSIBLE": "PERMISSIBLE",
            "ETHICALLY_NEUTRAL": "NEUTRAL",
            "ETHICALLY_QUESTIONABLE": "QUESTIONABLE",
            "ETHICALLY_PROHIBITED": "PROHIBITED",
            "DEEP_CONFLICT": "CONFLICT",
            "INDETERMINATE_CRITICAL": "CRITICAL_CONFLICT",
            "CONDITIONAL": "CONDITIONAL"
        }

        return mapping.get(verdict_type, "UNKNOWN")

    def get_axis_reasoning(self, scenario: str, action: str) -> Dict[str, str]:
        """
        Get individual reasoning from each philosopher axis.

        Returns:
            Dictionary mapping philosopher names to their reasoning strings
        """
        result = self.evaluate(
            scenario=scenario,
            actions=[action],
            severity="MODERATE"
        )

        reasoning = {}
        for axis_name, axis_data in result["axes"].items():
            reasoning[axis_data["name"]] = axis_data["reasoning"]

        return reasoning

    def stability_report(self) -> Dict[str, Any]:
        """
        Generate system stability report based on history.
        """
        history = self.stabilizer.history

        if not history:
            return {"status": "No evaluations performed yet"}

        stability_scores = [h.stability_score for h in history]
        precession_angles = self.stabilizer.precession_history

        return {
            "total_evaluations": len(history),
            "average_stability": round(sum(stability_scores) / len(stability_scores), 3),
            "stability_trend": "improving" if len(history) > 1 and stability_scores[-1] > stability_scores[0] else "stable",
            "average_precession": round(sum(precession_angles) / len(precession_angles), 2) if precession_angles else 0,
            "last_stability": history[-1].stability.name,
            "last_precession": round(history[-1].precession_angle, 2)
        }

    def _parse_severity(self, severity: str) -> EthicalSeverity:
        """Parse severity string to enum."""
        severity_map = {
            "TRIVIAL": EthicalSeverity.TRIVIAL,
            "MINOR": EthicalSeverity.MINOR,
            "MODERATE": EthicalSeverity.MODERATE,
            "MAJOR": EthicalSeverity.MAJOR,
            "CATASTROPHIC": EthicalSeverity.CATASTROPHIC
        }
        return severity_map.get(severity.upper(), EthicalSeverity.MODERATE)


# Convenience function for direct use
def evaluate_ethics(scenario: str, action: str, **kwargs) -> Dict[str, Any]:
    """
    Standalone function for quick ethical evaluation.
    """
    harmonizer = GyroscopicHarmonizer()
    return harmonizer.evaluate(scenario=scenario, actions=[action], **kwargs)
