# SINAP: Systems-based Interpersonal and Narrative Algorithmic Prediction

> A heuristic computational model for dynamic assessment of emotional dysregulation in clinical and forensic psychology contexts.

**Keywords / Palabras Clave:** Borderline Personality Disorder (BPD), Trastorno Límite de la Personalidad (TLP), Reactive Abuse, Abuso Reactivo, Intermittent Reinforcement, Refuerzo Intermitente, DARVO, Narcissistic Abuse, Abuso Narcisista, Trauma Bonding, Systems Theory, Emotion Regulation, Regulación Emocional, Dinámicas Vinculares, Psicología Clínica, Computational Psychology.

**Author:** Juan Andres Ubeda  
**Affiliation:** Juan Andres UBeda - Psicología - Universidad Maimónides (Argentina)  
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
All variables are scored on a normalized $[0, 10]$ scale, enabling cross-case comparison, longitudinal tracking, and sensitivity analysis. The $\text{clamp}$ function ensures numerical stability. The model is compatible with standard psychometric frameworks (e.g., PTSD Checklist, Difficulties in Emotion Regulation Scale — DERS).

---

## 🩺 Clinical Applications & Diagnostic Framework

> This section is intended for clinical psychologists working within CBT (Cognitive-Behavioral Therapy) and Systemic frameworks. Each SINAP variable is directly mapped to observable clinical phenomena, enabling the clinician to parameterize the model from session notes, behavioral observation, and standardized assessment instruments.

### 1. Personality Disorders — DSM-5 Alignment

The SINAP model demonstrates particular efficacy in the functional analysis of **Borderline Personality Disorder (BPD / TLP)**, as defined in the DSM-5 (APA, 2013). The model's variables directly operationalize three core diagnostic criteria:

| DSM-5 BPD Criterion | SINAP Variable(s) | Clinical Observation |
|---|---|---|
| **Criterion 1** — Frantic efforts to avoid real or imagined abandonment | $E$ (External Stressors) + $A$ (Asymmetry) | Separation cues or perceived rejection spikes $E$; perceived power imbalance elevates $A$, accelerating $T_d$ |
| **Criterion 2** — Unstable and intense interpersonal relationships | $R_2$ (Intrusion) + $\gamma$ (Sensitivity) | The subject oscillates between idealization and devaluation; intrusive relational attempts ($R_2$) are amplified quadratically by $\gamma$, generating rapid $T_d$ escalation |
| **Criterion 6** — Affective instability due to a marked reactivity of mood | $\lambda$ (Persistence) + $\Delta T_d$ | A high $\lambda$ value (e.g., 0.90) reflects the persistence of dysregulated mood states across days; a large $\Delta T_d$ captures sudden affective shifts — a direct correlate of emotional lability |

> **Clinical Note (CBT/DBT perspective):** In BPD cases, the clinician should pay special attention to the $\gamma \cdot R_2^2$ term. Because $R_2$ is squared, even moderate intrusive regulation attempts (e.g., repeated phone calls, guilt-inducing messages, triangulation via third parties) produce a disproportionate increase in $T_d$. This non-linearity models the BPD subject's extreme sensitivity to perceived control or abandonment threats. This aligns directly with Linehan's (1993) biosocial theory of BPD, in which emotional sensitivity + invalidating environment = dysregulation spiral.

---

### 2. Attachment Dynamics

The SINAP model provides a formal framework for analyzing attachment system collapse. The variables $\gamma$ and $R_2$ are the primary operationalizers of attachment dysregulation:

#### 🔴 Disorganized Attachment (Main & Hesse, 1990)
Characterized by the simultaneous activation of **approach** and **avoidance** behavioral systems. In SINAP terms:
- **$\gamma$ (Intrusion Sensitivity)** is maximally elevated (close to 1.0): any proximity attempt by the attachment figure simultaneously activates the fear system.
- **$R_2$ (Intrusion)** is high because the subject or the attachment figure uses paradoxical, coercive, or frightening strategies that function as regulation attempts but produce the opposite effect.
- **Systemic result:** The $\gamma \cdot R_2^2$ term becomes the dominant driver of $T_d$, collapsing the secure base and making stable $T_d$ values ($< 3$) functionally impossible without external containment.

#### 🟡 Anxious-Ambivalent Attachment (Ainsworth, 1978)
Characterized by hyperactivation of the attachment system and fear of abandonment:
- **$\lambda$** (Persistence) is elevated: relational anxiety from previous interactions persists into the current state.
- **$A$** (Asymmetry) is consistently high: the subject perceives a chronic power differential with the attachment figure, generating a self-reinforcing loop where $T_d$ rarely returns to baseline.
- **$R_1$** (Effective Regulation) is chronically low: the subject struggles to self-soothe in the absence of external reassurance from the attachment figure.

> **Clinical Note (Systemic framework):** For clinicians using structural or strategic family therapy models, $A$ (Systemic Asymmetry) maps directly to **coalitional patterns** and **boundary violations**. A persistently high $A$ indicates that the therapeutic focus must address the relational system before individual regulation is achievable.

---

### 3. Cluster B Dysregulation Spectrum

Beyond BPD, the SINAP model is applicable across the **Cluster B personality spectrum** where interpersonal conflict maintenance is a central feature:

#### Narcissistic Personality Disorder (NPD) — Devaluation Phase
During the devaluation phase (following idealization collapse), the NPD subject generates a relational context in which **the other person's** SINAP variables are severely impacted:
- The NPD subject's behaviors function as a constant $E$ (External Stressor) source for their interlocutor.
- **$A$ (Systemic Asymmetry)** is architecturally maintained by the NPD subject through mechanisms of contempt, gaslighting, and social invalidation — keeping the other party's $A$ chronically elevated.
- **Intervention implication:** Lowering $A$ is the primary clinical lever. This is achieved not through confronting the NPD subject directly, but by rebuilding the interlocutor's **identity resources** ($R_1$), reducing their schema activation ($V$), and creating external boundary structures that reduce $E$.

#### Histrionic & Antisocial Spectra
- **Histrionic:** High $E$ generation (dramatic, stimulus-seeking behaviors) combined with low $R_1$ produces rapid $T_d$ oscillation. The model can track the subject's own regulation trajectory across sessions.
- **Antisocial:** $\gamma$ is characteristically low in the subject itself (reduced emotional sensitivity), but the subject functions as a high-$E$ and high-$A$ agent in the relational system of others.

---

## 🧭 Clinical Usage Guide

### For CBT Clinicians

Map the following CBT constructs directly to SINAP variables during case formulation:

| CBT Construct | SINAP Variable | Assessment Source |
|---|---|---|
| Schema Activation (Young, 2003) | $V$ | YSQ-S3 (Young Schema Questionnaire) |
| Life Events / Stressors | $E$ | LES (Life Experiences Survey) or session observation |
| Coping Skills / Regulation Repertoire | $R_1$ | DERS (Difficulties in Emotion Regulation Scale) — inverted score |
| Reassurance-Seeking / Intrusive Behaviors | $R_2$ | Direct behavioral observation or collateral report |
| Emotional Sensitivity (baseline) | $\gamma$ | Clinical estimate; cross-validate with DERS Subscale 1 |
| Relational Power Differential | $A$ | IIP-32 (Inventory of Interpersonal Problems) |
| Baseline Affect / Mood Inertia | $\lambda$ | PANAS across multiple sessions; or MSSD (Mean Square Successive Difference) |

### For Systemic Clinicians

- Use $A$ (Systemic Asymmetry) as the entry point for **circular questioning**: "What would happen to the tension in the system if the power differential were reduced?"
- Map $R_2$ to **communication patterns**: intrusive or paradoxical communication acts as over-regulation, amplified by the other party's $\gamma$.
- Use $\Delta T_d$ to evaluate **homeostatic vs. morphogenetic** system trajectories across sessions: a positive $\Delta T_d$ trend over multiple sessions indicates a morphogenetic spiral (escalation); a negative trend suggests homeostatic stabilization.
- The recursive structure of the model ($T_d$ depends on $T_{d-1}$) aligns with **circular causality** principles in systemic epistemology.

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

- What happens if $R_2$ increases by $+2$? *(More intrusive regulation — models escalation of contact attempts)*
- What happens if $R_1$ increases by $+2$? *(Better coping resources — models therapeutic progress)*
- What happens if $E$ decreases by $-2$? *(Stressor reduction — models environmental containment)*

Each perturbation recalculates $T_d$ and $R_c$ to show directional sensitivity, enabling the clinician to identify the **highest-leverage intervention point** for a given case.

---

## 🤖 How to Test SINAP with AI: The Clinical Vignette Method

You don't need to be an expert in algebra or computational modeling to use SINAP. You can use any modern LLM (like ChatGPT, Claude, or Gemini) to simulate the equation for your clinical cases using conversational data (like WhatsApp exports).

**Instructions:**
1. Open your preferred AI chatbot.
2. Copy and paste the prompt below, which includes a real (anonymized) clinical vignette of a couple in high conflict.
3. Watch the AI extract the variables from the text, run the SINAP equation, and provide a systemic risk assessment.

### 🇪🇸 Prompt de Prueba en Español (Para copiar y pegar en la IA)

```text
Actúa como un simulador clínico del modelo SINAP (Predicción Algorítmica Narrativa e Interpersonal basada en Sistemas). 
A continuación, te presento una viñeta clínica basada en una transcripción de WhatsApp de una pareja (los llamaremos Sebastián y Mariela) que asiste a terapia de pareja y ha otorgado consentimiento para analizar su dinámica. 

Contexto clínico: 
- Sebastián: 49 años, abogado, con hijos de un matrimonio anterior. Presenta apego predominantemente seguro/estable.
- Mariela: 42 años, abogada, sin hijos. Presenta un esquema de trauma por abandono paterno severo y cuenta con un sistema familiar (clan) que refuerza activamente su desregulación y narrativas de victimización.
- Situación actual: Mariela está atravesando un día emocionalmente difícil. Sebastián intenta establecer un límite ante agresiones previas.

--- INICIO DE LA TRANSCRIPCIÓN ---
Sebastián: "reproches y echarme la culpa de que todos estos meses en los que estas alienada son culpa mia, cuando esto es algo que arrastras de años, bueno no. Perdon pero tengo que cuidar mi cabeza"
Mariela: "Ok"
Mariela: "Gracias por entender que es un día movilizante y empatizar"
Mariela: "Tu trato fue muy amable y contenedor"
Mariela: "Beso"
Sebastián: "ahhh ahora sacas esa carta?"
Sebastián: "hasta oré por tu viejo… te cagaste en todo eso y ya arrancaste con que 'veo que ahora me desbloqueaste' cuando anoche totalmente sacada no hacias otra cosa que agredirme"
Mariela: "Mientras q no hables mal de él es suficiente"
--- FIN DE LA TRANSCRIPCIÓN ---

Instrucciones para la IA:
1. Analiza el diálogo y el contexto sistémico. Extrae un valor estimado (de 0 a 10) para las variables del modelo SINAP aplicadas a Mariela en ese momento: 
   - V (Vulnerabilidad / Esquemas de abandono activos)
   - E (Estresores externos / Influencia del sistema familiar)
   - R1 (Regulación efectiva / Capacidad de auto-calmarse)
   - R2 (Regulación intrusiva/DARVO hacia Sebastián)
   - Gamma (Sensibilidad a la intrusión, de 0.1 a 1.0)
   - A (Asimetría sistémica / Invalidación)
2. Calcula la Tensión del día (Td) para Mariela usando la fórmula: Td = clamp( T(d-1)*Lambda + V + E - R1 + Gamma*(R2^2), 0, 10 ) 
   Asume que la tensión de ayer T(d-1) era 6 y la persistencia (Lambda) es 0.8.
3. Explícame el significado psicológico y sistémico de este estado. ¿Se observa un patrón de DARVO o Baiting? ¿El sistema está Estable, Inestable, Formando Tormenta o en un Evento Crítico?
```

### 🇬🇧 English Testing Prompt (To copy & paste into your AI)

```text
Act as a clinical simulator for the SINAP model (Systems-based Interpersonal and Narrative Algorithmic Prediction). 
Below is a clinical vignette based on a WhatsApp transcript from a couple in therapy (we will call them Sebastian and Mariela) who have granted consent for their dynamic to be analyzed.

Clinical Context:
- Sebastian: 49 years old, lawyer, has children from a previous marriage. Exhibits a predominantly secure/stable attachment style.
- Mariela: 42 years old, lawyer, no children. Exhibits a severe father-abandonment trauma schema, supported by an extended family system (clan) that actively reinforces her dysregulation and victim-narratives.
- Current situation: Mariela is having an emotionally difficult day. Sebastian is trying to set a boundary regarding previous aggressive behavior.

--- TRANSCRIPT START ---
Sebastian: "blaming me and reproaching me that all these months you've been alienated is my fault, when this is something you've been carrying for years, well no. I'm sorry but I have to protect my mental health."
Mariela: "Ok"
Mariela: "Thank you for understanding that it's an emotionally heavy day and for empathizing."
Mariela: "Your treatment was very kind and supportive."
Mariela: "Kiss"
Sebastian: "ahhh so now you pull that card?"
Sebastian: "I even prayed for your old man... you didn't care about any of that and started with 'I see you unblocked me now' when last night you were completely unhinged doing nothing but attacking me."
Mariela: "As long as you don't speak ill of him, that's enough."
--- TRANSCRIPT END ---

Instructions for the AI:
1. Analyze the dialogue and systemic context. Extract an estimated value (0 to 10) for Mariela's SINAP model variables at this moment:
   - V (Vulnerability / Active Abandonment Schemas)
   - E (External Stressors / Family system influence)
   - R1 (Effective Regulation / Ability to self-soothe)
   - R2 (Intrusive Regulation/DARVO towards Sebastian)
   - Gamma (Intrusion Sensitivity, 0.1 to 1.0)
   - A (Systemic Asymmetry / Invalidation)
2. Calculate the Tension of the day (Td) for Mariela using the formula: Td = clamp( T(d-1)*Lambda + V + E - R1 + Gamma*(R2^2), 0, 10 )
   Assume yesterday's tension T(d-1) was 6 and the persistence (Lambda) is 0.8.
3. Explain the systemic and psychological meaning of this state. Is there a pattern of DARVO or Baiting? Is the system Stable, Unstable, Forming a Storm, or in a Critical Event?
```

---

## 🔬 Intended Use

- **Clinical Supervision**: Structured case formulation and risk assessment.
- **Academic Research**: Computational modeling of affect regulation dynamics.
- **Forensic Psychology**: Threat assessment in high-conflict interpersonal contexts.
- **Teaching**: Operationalizing abstract DSM-5 criteria into quantifiable, trackable variables for psychology training programs.

> ⚠️ **Disclaimer**: SINAP is a heuristic model. It organizes clinical variables and generates operational prognoses. It does **not** replace formal diagnosis or clinical judgment by a licensed professional.

---

## 📚 References

- American Psychiatric Association. (2013). *Diagnostic and statistical manual of mental disorders* (5th ed.). APA Publishing.
- Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). *Patterns of attachment.* Erlbaum.
- Beck, A. T. (1979). *Cognitive therapy and the emotional disorders.* International Universities Press.
- Bertalanffy, L. von (1968). *General System Theory.* Braziller.
- Gratz, K. L., & Roemer, L. (2004). Multidimensional assessment of emotion regulation and dysregulation. *Journal of Psychopathology and Behavioral Assessment, 26*(1), 41–54.
- Linehan, M. M. (1993). *Cognitive-behavioral treatment of borderline personality disorder.* Guilford Press.
- Main, M., & Hesse, E. (1990). Parents' unresolved traumatic experiences are related to infant disorganized attachment status. In M. T. Greenberg, D. Cicchetti, & E. M. Cummings (Eds.), *Attachment in the preschool years* (pp. 161–182). University of Chicago Press.
- Young, J. E., Klosko, J. S., & Weishaar, M. E. (2003). *Schema therapy: A practitioner's guide.* Guilford Press.

---

## 📄 Citation

See [CONTRIBUTING.md](CONTRIBUTING.md) for citation instructions.