"""
SINAP Model Calculator
======================
Systems-based Interpersonal and Narrative Algorithmic Prediction

Author: Juan Andres Ubeda
Affiliation: Estudiante de Psicología, Universidad Maimónides (Argentina)
Year: 2026
License: MIT

Description:
    This module implements the core SINAP computational model for dynamic
    assessment of emotional dysregulation. It calculates the Tension Dynamics
    index (Td), the rate of change (Delta_Td), and the Critical Risk index (Rc).

Usage:
    from sinap_calculator import calcular_sinap, SINAPInput
    result = calcular_sinap(SINAPInput(td_prev=4.0, V=6, E=5, R1=3, R2=4, gamma=0.5, A=2))
    print(result)
"""

from dataclasses import dataclass
from copy import copy


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class SINAPInput:
    """Input parameters for the SINAP model."""
    td_prev: float          # T(d-1): Prior tension state [0-10]
    V: float                # Vulnerability (activated schemas) [0-10]
    E: float                # External stressors [0-10]
    R1: float               # Effective regulation [0-10]
    R2: float               # Intrusion / over-regulation [0-10]
    gamma: float            # Intrusion sensitivity [0.1-1.0]
    A: float                # Systemic asymmetry [0-10]
    lam: float = 0.8        # Lambda: persistence [0.5-0.95]


@dataclass
class SINAPResult:
    """Output of the SINAP model calculation."""
    Td: float
    Delta_Td: float
    Rc: float
    state: str
    state_emoji: str
    inputs: SINAPInput


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def _clamp(value: float, min_val: float = 0.0, max_val: float = 10.0) -> float:
    """Bounds a value to the [min_val, max_val] interval."""
    return max(min_val, min(max_val, value))


def _classify_state(Td: float) -> tuple:
    """
    Classifies the system state based on the Td value.
    Returns: (label, emoji)
    """
    if Td < 3:
        return "Stable", "🟢"
    elif Td <= 6:
        return "Unstable", "🟡"
    elif Td <= 8:
        return "Storm Forming", "🟠"
    else:
        return "Critical Event", "🔴"


def calcular_sinap(inputs: SINAPInput) -> SINAPResult:
    """
    Calculates the SINAP model for a given set of clinical parameters.

    Core equations:
        Td  = clamp( T(d-1) * λ + V + E - R1 + γ(R2²), 0, 10 )
        ΔTd = Td - T(d-1)
        Rc  = (Td / 10) * (1 + ΔTd + E/10 + A)

    Args:
        inputs: A SINAPInput dataclass instance with all model parameters.

    Returns:
        A SINAPResult dataclass with calculated values and system classification.
    """
    # --- Equation 1: Tension Dynamics ---
    td_raw = (
        inputs.td_prev * inputs.lam
        + inputs.V
        + inputs.E
        - inputs.R1
        + inputs.gamma * (inputs.R2 ** 2)
    )
    Td = _clamp(td_raw)

    # --- Equation 2: Delta (Rate of Change) ---
    Delta_Td = Td - inputs.td_prev

    # --- Equation 3: Critical Risk Index ---
    Rc = (Td / 10) * (1 + Delta_Td + inputs.E / 10 + inputs.A)

    state_label, state_emoji = _classify_state(Td)

    return SINAPResult(
        Td=round(Td, 4),
        Delta_Td=round(Delta_Td, 4),
        Rc=round(Rc, 4),
        state=state_label,
        state_emoji=state_emoji,
        inputs=inputs,
    )


def sensitivity_analysis(inputs: SINAPInput) -> dict:
    """
    Runs three standard perturbation scenarios to assess model sensitivity.

    Scenarios:
        1. R2 + 2  (Increased intrusive regulation)
        2. R1 + 2  (Improved coping resources)
        3. E  - 2  (Reduced external stressors)

    Args:
        inputs: Base SINAPInput parameters.

    Returns:
        A dict with results for each perturbation scenario.
    """
    scenarios = {}

    p1 = copy(inputs)
    p1.R2 = _clamp(inputs.R2 + 2)
    scenarios["R2_plus_2"] = calcular_sinap(p1)

    p2 = copy(inputs)
    p2.R1 = _clamp(inputs.R1 + 2)
    scenarios["R1_plus_2"] = calcular_sinap(p2)

    p3 = copy(inputs)
    p3.E = _clamp(inputs.E - 2)
    scenarios["E_minus_2"] = calcular_sinap(p3)

    return scenarios


# ---------------------------------------------------------------------------
# CLI Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("SINAP Model Calculator — v1.0")
    print("Author: Juan Andres Ubeda / Universidad Maimónides")
    print("=" * 60)

    case = SINAPInput(
        td_prev=4.0,
        V=6.0,
        E=5.0,
        R1=3.0,
        R2=4.0,
        gamma=0.5,
        A=2.0,
        lam=0.8,
    )

    result = calcular_sinap(case)

    print(f"\n📊 SINAP RESULT")
    print(f"  Td (Tension):         {result.Td}")
    print(f"  ΔTd (Rate of change): {result.Delta_Td}")
    print(f"  Rc (Critical Risk):   {result.Rc}")
    print(f"  State:                {result.state_emoji} {result.state}")

    print(f"\n🔬 SENSITIVITY ANALYSIS")
    scenarios = sensitivity_analysis(case)
    for label, s in scenarios.items():
        print(f"  [{label}] Td={s.Td} | Rc={s.Rc} | {s.state_emoji} {s.state}")

    print("\n" + "=" * 60)
