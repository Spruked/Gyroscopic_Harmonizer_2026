"""
Tkinter live visualization for the Gyroscopic Harmonizer.

Run:
    python gyroscope_visualizer.py
"""

import math
import tkinter as tk
from tkinter import ttk
from typing import Any, Dict

from gyroscopic_harmonizer import GyroscopicHarmonizer


AXIS_COLORS = {
    "kant": "#2563eb",
    "hume": "#dc2626",
    "spinoza": "#16a34a",
    "locke": "#9333ea",
}


class GyroscopeVisualizer(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Gyroscopic Ethical Harmonizer")
        self.geometry("980x680")
        self.minsize(860, 600)

        self.harmonizer = GyroscopicHarmonizer()
        self.last_result: Dict[str, Any] = {}

        self._build_ui()
        self._load_sample()
        self.evaluate()

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        panel = ttk.Frame(self, padding=12)
        panel.grid(row=0, column=0, sticky="ns")

        ttk.Label(panel, text="Scenario").grid(row=0, column=0, sticky="w")
        self.scenario = tk.Text(panel, width=38, height=7, wrap="word")
        self.scenario.grid(row=1, column=0, sticky="ew", pady=(4, 10))

        ttk.Label(panel, text="Action").grid(row=2, column=0, sticky="w")
        self.action = ttk.Entry(panel, width=42)
        self.action.grid(row=3, column=0, sticky="ew", pady=(4, 10))

        ttk.Label(panel, text="Stakeholders, comma-separated").grid(row=4, column=0, sticky="w")
        self.stakeholders = ttk.Entry(panel, width=42)
        self.stakeholders.grid(row=5, column=0, sticky="ew", pady=(4, 10))

        ttk.Label(panel, text="Severity").grid(row=6, column=0, sticky="w")
        self.severity = ttk.Combobox(
            panel,
            values=["TRIVIAL", "MINOR", "MODERATE", "MAJOR", "CATASTROPHIC"],
            state="readonly",
        )
        self.severity.grid(row=7, column=0, sticky="ew", pady=(4, 10))
        self.severity.set("MODERATE")

        ttk.Label(panel, text="Time Pressure").grid(row=8, column=0, sticky="w")
        self.time_pressure = ttk.Scale(panel, from_=0.0, to=1.0, orient="horizontal")
        self.time_pressure.grid(row=9, column=0, sticky="ew", pady=(4, 10))

        ttk.Button(panel, text="Evaluate", command=self.evaluate).grid(row=10, column=0, sticky="ew")

        self.summary = tk.Text(panel, width=38, height=14, wrap="word", state="disabled")
        self.summary.grid(row=11, column=0, sticky="nsew", pady=(12, 0))
        panel.rowconfigure(11, weight=1)

        right = ttk.Frame(self, padding=(0, 12, 12, 12))
        right.grid(row=0, column=1, sticky="nsew")
        right.rowconfigure(0, weight=1)
        right.columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(right, bg="#f8fafc", highlightthickness=1, highlightbackground="#cbd5e1")
        self.canvas.grid(row=0, column=0, sticky="nsew")

    def _load_sample(self) -> None:
        self.scenario.insert(
            "1.0",
            "A company collects user data without explicit consent for targeted advertising.",
        )
        self.action.insert(0, "collect data without consent")
        self.stakeholders.insert(0, "users, company, advertisers")

    def evaluate(self) -> None:
        stakeholders = [
            item.strip()
            for item in self.stakeholders.get().split(",")
            if item.strip()
        ]
        result = self.harmonizer.evaluate(
            scenario=self.scenario.get("1.0", "end").strip(),
            actions=[self.action.get().strip()],
            stakeholders=stakeholders,
            severity=self.severity.get(),
            time_pressure=float(self.time_pressure.get()),
        )
        self.last_result = result
        self._draw(result)
        self._write_summary(result)

    def _draw(self, result: Dict[str, Any]) -> None:
        self.canvas.delete("all")
        width = max(self.canvas.winfo_width(), 640)
        height = max(self.canvas.winfo_height(), 520)
        cx = width // 2
        cy = height // 2
        radius = min(width, height) * 0.34

        self.canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline="#94a3b8", width=2)
        self.canvas.create_line(cx - radius - 28, cy, cx + radius + 28, cy, fill="#cbd5e1")
        self.canvas.create_line(cx, cy - radius - 28, cx, cy + radius + 28, fill="#cbd5e1")
        self.canvas.create_text(cx, cy - radius - 42, text="Ethical Gyroscope", font=("Segoe UI", 16, "bold"), fill="#0f172a")

        for axis_id, axis_data in result["axes"].items():
            vector = axis_data["vector"]
            confidence = axis_data["confidence"]
            color = AXIS_COLORS.get(axis_id, "#334155")
            end_x = cx + vector["x"] * radius
            end_y = cy - vector["y"] * radius
            width_px = max(2, int(confidence * 6))
            self._arrow(cx, cy, end_x, end_y, color, width_px)
            self.canvas.create_text(end_x, end_y - 14, text=axis_id.upper(), fill=color, font=("Segoe UI", 10, "bold"))

        resultant = result["resultant"]
        end_x = cx + resultant["x"] * radius
        end_y = cy - resultant["y"] * radius
        self._arrow(cx, cy, end_x, end_y, "#020617", 7)
        self.canvas.create_text(end_x, end_y + 20, text="RESULTANT", fill="#020617", font=("Segoe UI", 10, "bold"))

        stability = result["stability"]
        verdict = result["verdict"]
        footer = f"{verdict['type']} | {verdict['clearance']} | Stability {stability['level']} {stability['score']}"
        self.canvas.create_text(cx, height - 32, text=footer, fill="#0f172a", font=("Segoe UI", 12))

    def _arrow(self, start_x: float, start_y: float, end_x: float, end_y: float, color: str, width: int) -> None:
        self.canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=width, arrow=tk.LAST, arrowshape=(16, 18, 6))

    def _write_summary(self, result: Dict[str, Any]) -> None:
        verdict = result["verdict"]
        stability = result["stability"]
        lines = [
            f"Verdict: {verdict['type']}",
            f"Clearance: {verdict['clearance']}",
            f"Confidence: {verdict['confidence']}",
            f"Stability: {stability['level']} ({stability['score']})",
            f"Precession: {stability['precession']} degrees",
            "",
            verdict["recommendation"],
            "",
            "Axes:",
        ]
        for axis_id, axis_data in result["axes"].items():
            lines.append(f"- {axis_data['name']}: x={axis_data['vector']['x']}, conf={axis_data['confidence']}")

        self.summary.configure(state="normal")
        self.summary.delete("1.0", "end")
        self.summary.insert("1.0", "\n".join(lines))
        self.summary.configure(state="disabled")


if __name__ == "__main__":
    GyroscopeVisualizer().mainloop()
