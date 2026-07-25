"""
SINAP Model Calculator — v1.1 with Input Validation & Logging
==============================================================
Systems-based Interpersonal and Narrative Algorithmic Prediction

Author: Juan Andres Ubeda
Affiliation: Estudiante de Psicología, Universidad Maimónides (Argentina)
Year: 2026
License: MIT

Description:
    This module implements the core SINAP computational model for dynamic
    assessment of emotional dysregulation. It calculates the Tension Dynamics
    index (Td), the rate of change (Delta_Td), and the Critical Risk index (Rc).
    
    INPUT VALIDATION (v1.1):
    - All clinical variables [V, E, R1, R2, A] must be in [0-10]
    - Gamma (intrusion sensitivity) must be in [0.1-1.0]
    - Lambda (persistence) must be in [0.5-0.95]
    - Prior tension (Td_prev) must be in [0-10]
    - Raises ValueError if constraints violated

Usage:
    from sinap_calculator import calcular_sinap, SINAPInput
    result = calcular_sinap(SINAPInput(td_prev=4.0, V=6, E=5, R1=3, R2=4, gamma=0.5, A=2))
    print(result)
"""

from dataclasses import dataclass
from copy import copy
import logging
from typing import Tuple

# ==================== LOGGING SETUP ====================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - SINAP - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ==================== DATA CLASSES ====================

@dataclass(frozen=True)
class SINAPInput:
    """
    Input parameters for the SINAP model.
    
    All values are validated upon instantiation.
    Frozen to prevent accidental mutation.
    """
    td_prev: float          # T(d-1): Prior tension state [0-10]
    V: float                # Vulnerability (activated schemas) [0-10]
    E: float                # External stressors [0-10]
    R1: float               # Effective regulation [0-10]
    R2: float               # Intrusion / over-regulation [0-10]
    gamma: float            # Intrusion sensitivity [0.1-1.0]
    A: float                # Systemic asymmetry [0-10]
    lam: float = 0.8        # Lambda: persistence [0.5-0.95]
    
    def __post_init__(self):
        """Validate all inputs after instantiation."""
        _validate_sinap_input(self)


@dataclass(frozen=True)
class SINAPResult:
    """
    Output of the SINAP model calculation.
    Frozen to prevent accidental mutation.
    """
    Td: float
    Delta_Td: float
    Rc: float
    state: str
    state_emoji: str
    inputs: SINAPInput


# ==================== VALIDATION ====================

def _validate_sinap_input(inp: SINAPInput) -> None:
    """
    Validates all SINAP input parameters.
    
    Args:
        inp: SINAPInput instance to validate.
        
    Raises:
        ValueError: If any parameter violates clinical constraints.
    """
    errors = []
    
    # Validate [0-10] range variables
    range_vars = {
        'td_prev': inp.td_prev,
        'V': inp.V,
        'E': inp.E,
        'R1': inp.R1,
        'R2': inp.R2,
        'A': inp.A
    }
    
    for name, value in range_vars.items():
        if not (0 <= value <= 10):
            errors.append(f"{name}={value} must be in [0, 10]")
    
    # Validate gamma [0.1-1.0]
    if not (0.1 <= inp.gamma <= 1.0):
        errors.append(f"gamma={inp.gamma} must be in [0.1, 1.0]")
    
    # Validate lambda [0.5-0.95]
    if not (0.5 <= inp.lam <= 0.95):
        errors.append(f"lam={inp.lam} must be in [0.5, 0.95]")
    
    if errors:
        error_msg = "SINAP Input Validation Failed:\n  " + "\n  ".join(errors)
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    logger.debug(f"Input validation passed: Td_prev={inp.td_prev}, V={inp.V}, E={inp.E}, "
                f"R1={inp.R1}, R2={inp.R2}, γ={inp.gamma}, A={inp.A}, λ={inp.lam}")


# ==================== CORE FUNCTIONS ====================

def _clamp(value: float, min_val: float = 0.0, max_val: float = 10.0) -> float:
    """
    Bounds a value to the [min_val, max_val] interval.
    
    Ensures numerical stability of Td calculation.
    """
    return max(min_val, min(max_val, value))


def _classify_state(Td: float) -> Tuple[str, str]:
    """
    Classifies the system state based on the Td value.
    
    Args:
        Td: Tension Dynamics value [0-10].
        
    Returns:
        Tuple of (state_label, emoji_icon).
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
        inputs: A validated SINAPInput dataclass instance.

    Returns:
        A SINAPResult dataclass with calculated values and system classification.
        
    Raises:
        ValueError: If inputs do not pass validation.
    """
    # Validation is performed in SINAPInput.__post_init__
    
    # --- Equation 1: Tension Dynamics ---
    td_raw = (
        inputs.td_prev * inputs.lam
        + inputs.V
        + inputs.E
        - inputs.R1
        + inputs.gamma * (inputs.R2 ** 2)
    )
    Td = _clamp(td_raw)
    
    logger.debug(f"Tension calc: Td_raw={td_raw:.4f} → Td={Td:.4f}")

    # --- Equation 2: Delta (Rate of Change) ---
    Delta_Td = Td - inputs.td_prev
    
    # --- Equation 3: Critical Risk Index ---
    Rc = (Td / 10) * (1 + Delta_Td + inputs.E / 10 + inputs.A)
    
    state_label, state_emoji = _classify_state(Td)
    
    logger.info(f"SINAP Result: Td={Td:.4f} ({state_emoji} {state_label}), "
               f"ΔTd={Delta_Td:.4f}, Rc={Rc:.4f}")

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
    
    Identifies highest-leverage intervention points for therapeutic work.

    Scenarios:
        1. R2 + 2  (Increased intrusive regulation — escalation model)
        2. R1 + 2  (Improved coping resources — therapeutic progress model)
        3. E  - 2  (Reduced external stressors — environmental containment model)

    Args:
        inputs: Base validated SINAPInput parameters.

    Returns:
        A dict with results for each perturbation scenario.
        
    Raises:
        ValueError: If base inputs do not pass validation.
    """
    scenarios = {}
    
    logger.info(f"Running sensitivity analysis on baseline: Td_prev={inputs.td_prev}")

    # Scenario 1: Increased intrusive regulation
    p1_R2 = _clamp(inputs.R2 + 2)
    p1 = SINAPInput(
        td_prev=inputs.td_prev, V=inputs.V, E=inputs.E, R1=inputs.R1,
        R2=p1_R2, gamma=inputs.gamma, A=inputs.A, lam=inputs.lam
    )
    scenarios["R2_plus_2"] = calcular_sinap(p1)
    logger.debug(f"  [R2+2]: R2={inputs.R2}→{p1_R2}, Td={scenarios['R2_plus_2'].Td}")

    # Scenario 2: Improved effective regulation
    p2_R1 = _clamp(inputs.R1 + 2)
    p2 = SINAPInput(
        td_prev=inputs.td_prev, V=inputs.V, E=inputs.E, R1=p2_R1,
        R2=inputs.R2, gamma=inputs.gamma, A=inputs.A, lam=inputs.lam
    )
    scenarios["R1_plus_2"] = calcular_sinap(p2)
    logger.debug(f"  [R1+2]: R1={inputs.R1}→{p2_R1}, Td={scenarios['R1_plus_2'].Td}")

    # Scenario 3: Reduced external stressors
    p3_E = _clamp(inputs.E - 2)
    p3 = SINAPInput(
        td_prev=inputs.td_prev, V=inputs.V, E=p3_E, R1=inputs.R1,
        R2=inputs.R2, gamma=inputs.gamma, A=inputs.A, lam=inputs.lam
    )
    scenarios["E_minus_2"] = calcular_sinap(p3)
    logger.debug(f"  [E-2]: E={inputs.E}→{p3_E}, Td={scenarios['E_minus_2'].Td}")

    return scenarios


# ==================== CLI DEMO ====================

if __name__ == "__main__":
    print("=" * 70)
    print("SINAP Model Calculator — v1.1 (with Input Validation)")
    print("Author: Juan Andres Ubeda / Universidad Maimónides")
    print("=" * 70)

    try:
        # Example: High-conflict couple scenario
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
        print(f"  Td (Tension Dynamics):         {result.Td}")
        print(f"  ΔTd (Rate of change):          {result.Delta_Td}")
        print(f"  Rc (Critical Risk Index):      {result.Rc}")
        print(f"  State:                         {result.state_emoji} {result.state}")

        print(f"\n🔬 SENSITIVITY ANALYSIS")
        print(f"  (Identifies therapeutic leverage points)\n")
        scenarios = sensitivity_analysis(case)
        for label, s in scenarios.items():
            delta = s.Td - result.Td
            direction = "↑" if delta > 0 else "↓" if delta < 0 else "→"
            print(f"  [{label:12}] Td={s.Td} {direction} ({delta:+.4f}) | Rc={s.Rc} | {s.state_emoji} {s.state}")

        print("\n" + "=" * 70)
        print("✅ All validations passed. Model is stable.")
        print("=" * 70)
        
    except ValueError as e:
        print(f"\n❌ VALIDATION ERROR:\n{e}")
        print("\n" + "=" * 70)
