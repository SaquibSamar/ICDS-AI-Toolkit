# AI Logic – ICDS AI Toolkit

This folder contains the core **Python-based Explainable AI logic** used in the ICDS AI Toolkit.

The scripts here are responsible for transforming raw ICDS child data into **actionable, explainable risk and dropout predictions** that are visualised in Power BI.

---

## File Overview

### 'icds_ai_powerbi.py'
This is the **main AI logic file** of the project.

It performs the following functions:
- Reads ICDS child-level data from an Excel source
- Cleans and validates nutrition and attendance fields
- Applies explainable, rule-based AI logic to:
  - Classify **nutrition risk** (Safe / Warning / Critical)
  - Predict **dropout risk** (Low / Medium / High)
- Generates **human-readable reasons** for every prediction
- Outputs a final processed DataFrame compatible with Power BI

The same script is used for:
- **Direct execution inside Power BI** using the Python Script connector
- **Standalone execution** for CSV-based workflows or testing

This ensures a **single, consistent AI logic layer** across deployment modes.

---

## Explainable AI Approach

The AI logic is intentionally designed to be **transparent and interpretable**.

Instead of using black-box machine learning models, the system relies on:
- Clear nutrition and attendance thresholds
- Weighted rule-based scoring
- Explicit reason generation for each alert

This approach aligns with the requirements of **government and social welfare systems**, where trust and accountability are critical.

---

## Data Note

For the hackathon prototype, the script is tested using **synthetic ICDS-like data** to ensure privacy and responsible AI usage.

The logic is **fully compatible with authorised real ICDS datasets** and does not require any modification when deployed with real data.

---

## Usage Notes

- When used inside Power BI, the **last line of the script must output a DataFrame** (e.g., `df`)
- File paths to the Excel data source should be updated based on the local environment
- No additional machine learning libraries are required

---

## Key Takeaway

> This folder represents the intelligence layer of the ICDS AI Toolkit, enabling early, explainable, and actionable decision support for child welfare interventions.
