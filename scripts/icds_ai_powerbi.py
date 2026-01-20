import pandas as pd

# =====================================================
# ICDS AI TOOLKIT
# Explainable AI Logic for Child Risk & Dropout Prediction
# =====================================================

# STEP 1: READ ICDS DATA (EXCEL)
# -----------------------------------------------------
df = pd.read_excel(r"C:\Users\S M Shahrukh\OneDrive\Desktop\ICDS_AI_Toolkit\icds_data.xlsx")

# -----------------------------------------------------
# STEP 2: BASIC DATA CLEANING
# -----------------------------------------------------
df["Attendance"] = df["Attendance"].fillna(0)
df["Weight"] = df["Weight"].fillna(df["Weight"].mean())
df["MUAC"] = df["MUAC"].fillna(df["MUAC"].mean())

# -----------------------------------------------------
# STEP 3: NUTRITION RISK SCORING (EXPLAINABLE AI)
# -----------------------------------------------------
def calculate_risk(row):
    score = 0
    reasons = []

    if row["Weight"] < 12:
        score += 40
        reasons.append("Low weight")

    if row["MUAC"] < 13:
        score += 30
        reasons.append("Low MUAC")

    if row["Attendance"] < 60:
        score += 30
        reasons.append("Poor attendance")

    if score >= 70:
        risk_level = "Critical"
    elif score >= 40:
        risk_level = "Warning"
    else:
        risk_level = "Safe"

    reason_text = ", ".join(reasons) if reasons else "No risk factors"

    return pd.Series([risk_level, reason_text])

df[["Risk_Level", "Risk_Reason"]] = df.apply(calculate_risk, axis=1)

# -----------------------------------------------------
# STEP 4: DROPOUT RISK PREDICTION
# -----------------------------------------------------
def calculate_dropout(row):
    if row["Attendance"] < 60:
        return pd.Series(["High", "Attendance below 60%"])
    elif row["Attendance"] < 75:
        return pd.Series(["Medium", "Irregular attendance"])
    else:
        return pd.Series(["Low", "Regular attendance"])

df[["Dropout_Risk", "Dropout_Reason"]] = df.apply(calculate_dropout, axis=1)

# -----------------------------------------------------
# STEP 5: FINAL OUTPUT FOR POWER BI
# - The LAST LINE must return a DataFrame (Power BI rule)
# -----------------------------------------------------
df
