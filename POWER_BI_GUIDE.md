# Power BI Integration Guide – ICDS AI Toolkit

## 1. Overview
This document explains how the ICDS AI Toolkit integrates Python-based explainable AI logic directly into Power BI to analyse child nutrition and dropout risk data collected under ICDS.

The dashboard enables Anganwadi workers and officials to identify at-risk children, understand the reasons behind each alert, and monitor trends at village and Anganwadi levels.

---

## 2. Power BI + Python Integration
The solution uses Power BI’s native Python scripting connector.

Workflow:
- Power BI runs a Python script during data refresh
- The script reads ICDS data from an Excel file
- AI logic is executed inside Power BI
- The final processed DataFrame is loaded directly into the Power BI dataset

No external servers or APIs are required.

---

## 3. AI Logic Execution in Power BI
The Python script performs the following steps:
- Data cleaning and validation
- Nutrition risk scoring (Safe / Warning / Critical)
- Dropout risk prediction (Low / Medium / High)
- Generation of human-readable reasons for each prediction

The final line of the script outputs a DataFrame (`df`), which Power BI automatically ingests.

---

## 4. Dashboard Visuals
The Power BI dashboard includes:
- Donut chart showing overall nutrition risk distribution
- Dropout risk overview chart
- Child-level table with risk and dropout reasons
- Village and Anganwadi-level comparison matrix
- Interactive slicers for Village, Gender, and Risk Level

All visuals are fully interactive and update dynamically based on filters.

---

## 5. Data Refresh & Deployment Modes

### Case A: CSV-Based Workflow
- Python script generates an output CSV
- CSV is manually uploaded into Power BI
- Suitable for offline or pilot environments

### Case B: Direct Power BI Integration (Recommended)
- Python script runs inside Power BI
- No manual file uploads
- Refresh button re-runs AI logic automatically
- Suitable for district and state-level dashboards

---

## 6. Why Power BI
Power BI was chosen because it is:
- Already used in government systems
- Easy to adopt without retraining
- Scalable from village to national level
- Capable of running Python-based AI logic securely

---

## 7. Key Takeaway
The ICDS AI Toolkit demonstrates how explainable AI can be seamlessly embedded into existing government analytics tools to enable early, transparent, and actionable decision-making.
