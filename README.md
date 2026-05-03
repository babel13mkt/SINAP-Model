# SINAP: Systems-based Interpersonal and Narrative Algorithmic Prediction

> A heuristic computational model for dynamic assessment of emotional dysregulation in clinical and forensic psychology contexts.

**Author:** Juan Andres Ubeda  
**Affiliation:** Estudiante de Psicología, Universidad Maimónides (Argentina)  
**Year:** 2026  
**License:** [MIT](LICENSE)

---

## 📐 The Equation

### Core Tension Oscillator

$$T_d = \text{clamp}\left( T_{d-1} \cdot \lambda + V + E - R_1 + \gamma \cdot R_2^2,\ 0,\ 10 \right)$$

### Delta (Rate of Change)

$$\Delta T_d = T_d - T_{d-1}$$

### Critical Risk Index

$$R_c = \frac{T_d}{10} \cdot \left(1 + \Delta T_d + \frac{E}{10} + A\right)$$

where $\text{clamp}(x, 0, 10)$ bounds the output to the $[0, 10]$ interval.

---

## 🔠 Variable Glossary

| Symbol | Name | Range | Description |
|---|---|---|---|
| $T_{d-1}$ | Prior Tension | 0–10 | Emotional tension level at the previous time step |
| $\lambda$ | Persistence | 0.5–0.95 | Rate at which prior tension carries over to the next state |
| $V$ | Vulnerability | 0–10 | Activation level of maladaptive schemas (CBT framework) |
| $E$ | External Stressors | 0–10 | Intensity of environmental stressors at time $d$ |
| $R_1$ | Effective Regulation | 0–10 | Functional coping and emotional regulation resources |
| $R_2$ | Intrusion / Over-regulation | 0–10 | Ineffective, intrusive, or coercive regulation attempts |
| $\gamma$ | Intrusion Sensitivity | 0.1–1.0 | Individual sensitivity coefficient to over-regulation |
| $A$ | Systemic Asymmetry | 0–10 | Power imbalance, invalidation, or social/relational pressure |

---

## 🏛️ The Five Pillars: S-I-N-A-P

### **S — Systems Theory**
Emotional dysregulation is modeled as a dynamic system, not a static trait. The model captures the **temporal evolution** of tension through recursive calculation ($T_d$ depends on $T_{d-1}$), drawing from General Systems Theory and cybernetic feedback loops.

### **I — Interpersonal Dynamics**
The variables $A$ (Systemic Asymmetry) and $R_2$ (Intrusion/Over-regulation) encode the relational context of the subject. Dysregulation is not purely intrapsychic — it is co-constructed within interpersonal fields, including coercive control, triangulation, and power differentials.

### **N — Narrative & Cognitive Schema Activation**
The variable $V$ (Vulnerability) operationalizes the activation of **cognitive schemas** (Young, 2003) and trauma-based narrative distortions. A subject's internal working models and narrative frameworks directly amplify or attenuate the tension state.

### **A — Algorithmic & Predictive**
The model generates concrete, time-windowed behavioral predictions (0–24h, 24–48h, 48–72h), classifying probable behavioral phases: Stonewalling, Baiting, Escalation, Discharge, or Re-engagement. This operationalizes clinical intuition into testable hypotheses.

### **P — Psychometric & Quantitative Foundation**
All variables are scored on a normalized $[0, 10]$ scale, enabling cross-case comparison, longitudinal tracking, and sensitivity analysis. The $\text{clamp}$ function ensures numerical stability. The model is compatible with standard psychometric frameworks (e.g., PTSD Checklist, Difficulties in Emotion Regulation Scale).

---

## 🚦 System State Classification

| $T_d$ Range | Status | Interpretation |
|---|---|---|
| $T_d < 3$ | 🟢 **Stable** | System in equilibrium |
| $3 \leq T_d \leq 6$ | 🟡 **Unstable** | Escalation risk, monitoring required |
| $6 < T_d \leq 8$ | 🟠 **Storm Forming** | Active baiting or provocation phase |
| $T_d > 8$ | 🔴 **Critical Event** | Imminent discharge or decompensation |

---

## ⚙️ Sensitivity Analysis Protocol

To assess model robustness, the following perturbations are evaluated for each case:

- What happens if $R_2$ increases by $+2$? *(More intrusive regulation)*
- What happens if $R_1$ increases by $+2$? *(Better coping resources)*
- What happens if $E$ decreases by $-2$? *(Stressor reduction)*

Each perturbation recalculates $T_d$ and $R_c$ to show directional sensitivity.

---

## 🔬 Intended Use

- **Clinical Supervision**: Structured case formulation and risk assessment.
- **Academic Research**: Computational modeling of affect regulation dynamics.
- **Forensic Psychology**: Threat assessment in high-conflict interpersonal contexts.

> ⚠️ **Disclaimer**: SINAP is a heuristic model. It organizes clinical variables and generates operational prognoses. It does **not** replace formal diagnosis or clinical judgment by a licensed professional.

---

## 📚 References

- Beck, A. T. (1979). *Cognitive therapy and the emotional disorders.*
- Young, J. E. (2003). *Schema therapy: A practitioner's guide.*
- Bertalanffy, L. von (1968). *General System Theory.*
- Linehan, M. M. (1993). *Cognitive-behavioral treatment of borderline personality disorder.*
- Gratz, K. L., & Roemer, L. (2004). Multidimensional assessment of emotion regulation and dysregulation. *Journal of Psychopathology and Behavioral Assessment, 26*(1), 41–54.

---

## 📄 Citation

See [CONTRIBUTING.md](CONTRIBUTING.md) for citation instructions.
