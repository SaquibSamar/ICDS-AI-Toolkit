# ICDS-AI-Toolkit
Explainable AI-powered dashboard for ICDS child nutrition &amp; dropout risk analysis
---

## Problem Statement

India’s Integrated Child Development Services (ICDS) collects large amounts of data related to child nutrition, attendance, and growth through Anganwadi centres. However, this data is often **fragmented, under-utilised, and analysed too late**, making early intervention difficult.

Anganwadi workers and ICDS officials currently lack:
- A unified view of child nutrition and attendance data  
- Early warning signals for malnutrition and dropout risk  
- Clear, explainable insights they can trust and act upon  

As a result, children at risk are often identified only after the situation becomes severe.

---

## Proposed Solution

The **ICDS AI Toolkit** is an **explainable AI-powered decision support system** that converts raw ICDS data into **actionable insights** using lightweight AI logic embedded directly into **Power BI**.

The toolkit:
- Flags **nutrition risk** among children using growth and attendance indicators  
- Predicts **dropout risk** before children disengage completely  
- Clearly explains **why** a child is flagged (no black-box AI)  
- Summarises trends at **village and Anganwadi levels**  

The solution is designed to align with **real ICDS workflows** and uses tools already familiar to government stakeholders.

---

## Where AI Is Used

This project uses **explainable, rule-based AI**, prioritising transparency and trust.

### 1.Nutrition Risk Scoring
Each child receives a **Risk Score (0–100)** based on:
- Weight
- MUAC
- Attendance percentage
- Age factor  

Risk Levels:
- **Safe**
- **Warning**
- **Critical**

---

### 2.Dropout Risk Prediction
Dropout risk is predicted using:
- Attendance patterns  
- Nutrition risk score  
- Age-related transition risk  

Output:
- **Low**
- **Medium**
- **High**

---

### 3.Explainability Layer
For every flagged child, the system generates a **human-readable reason**, such as:
- “Low attendance, Poor nutrition”
- “Low MUAC”
- “Older age, declining attendance”

This ensures that **every AI decision is understandable and actionable**.

---

## 📊 Power BI Integration

The AI logic is integrated directly into **Power BI using Python scripts**, enabling:

- No external servers  
- Automated refresh  
- Easy adoption within government systems  

### Supported Deployment Modes:
- **CSV-based prototype** (offline / pilot use)
- **Direct Python integration in Power BI** (recommended, no manual uploads)

---

## 🔐 Data Note

Due to the **sensitive nature of ICDS child data**, this prototype has been developed using **synthetic (dummy) data** that closely mirrors real ICDS indicators.

✔ Data structure is fully compatible with authorised ICDS datasets  
✔ No changes are required when switching to real data  
✔ Ensures privacy, ethics, and responsible AI usage  

---

## Social Impact

### Primary Beneficiaries:
- Anganwadi workers  
- ICDS supervisors and district officials  
- Children aged 3–6 years  

### Impact Created:
- Early identification of malnutrition and dropout risk  
- Timely, targeted interventions  
- Improved nutrition and education outcomes  
- Better use of existing ICDS data  

---

## Scalability & Future Scope

- Integration with health and education datasets  
- Role-based dashboards (worker, supervisor, district)  
- District → State → National scale deployment  
- Potential listing on public platforms such as **AIKosh**

---

## Tech Stack

- **Python** (AI logic)
- **Power BI** (dashboard & visualisation)
- **Pandas** (data processing)

---

## 📂 Repository Structure
ICDS-AI-Toolkit/
│
├── README.md
├── LICENSE
├── POWER_BI_GUIDE.md
├── data/
│ └── sample_icds_data.xlsx
├── scripts/
│ └── icds_ai_powerbi.py
├── reports/
│ └── ICDS_AI_Toolkit_Report.pdf
└── screenshots/
└── dashboard_view.png
