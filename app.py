import streamlit as st
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Credit Card Fraud Detection using Machine Learning",
    page_icon="💳",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("💳 Credit Card Fraud Detection using Machine Learning")
st.subheader("An Interactive FinTech Demonstration")

st.markdown("""
This application explains **how Machine Learning (ML) is used to detect fraudulent credit card transactions**  
and prevent financial losses.
""")

st.divider()

# ======================================================
# 1. TOPIC EXPLANATION
# ======================================================
st.header("1️⃣ Topic Explanation – What is the Concept?")

st.markdown("""
Credit card fraud detection uses **Machine Learning (ML)** to identify whether a transaction is:

- ✅ Genuine  
- ❌ Fraudulent  

ML models analyze **transaction patterns** and detect unusual behaviour.

👉 If fraud is detected early, banks can **block transactions and prevent losses**.
""")

st.info("Key Idea: Unusual Pattern ➜ ML Detection ➜ Fraud Prevention")

# ======================================================
# 2. BASIC WORKING IDEA
# ======================================================
st.header("2️⃣ Basic Working Idea – How Does It Work?")

st.markdown("""
ML systems learn from **historical transaction data**:

1. Learn patterns of normal spending  
2. Identify unusual transactions  
3. Assign a **fraud probability score**  
4. Take action (approve / block / alert)

⚠️ ML does not “know fraud” — it detects **deviation from normal behaviour**.
""")

st.success("ML helps detect fraud in real-time.")

# ======================================================
# 3. FINANCIAL APPLICATION
# ======================================================
st.header("3️⃣ Financial Application")

st.markdown("""
**Used by:** Banks, payment gateways, credit card networks (Visa, Mastercard)

**Decision Supported:**
- Approve transaction  
- Block transaction  
- Flag for review  

**Objective:**
👉 Prevent financial loss and protect customers
""")

# ======================================================
# 4. INTERACTIVE DEMO
# ======================================================
st.header("4️⃣ Real-Life Fraud Detection Simulation")

st.markdown("""
Adjust the transaction details below to see how AI detects fraud.
""")

col1, col2, col3 = st.columns(3)

with col1:
    amount = st.slider("Transaction Amount (₹)", 100, 200000, 5000)

with col2:
    location_risk = st.selectbox(
        "Transaction Location",
        ["Same City", "Different City", "Different Country"]
    )

with col3:
    frequency = st.slider("Transactions in Last Hour", 1, 20, 3)

# -----------------------------
# SIMPLE AI LOGIC (Explainable)
# -----------------------------
risk_score = 0

# Amount risk
if amount > 50000:
    risk_score += 40
elif amount > 20000:
    risk_score += 25
else:
    risk_score += 10

# Location risk
if location_risk == "Different Country":
    risk_score += 40
elif location_risk == "Different City":
    risk_score += 20

# Frequency risk
if frequency > 10:
    risk_score += 30
elif frequency > 5:
    risk_score += 15

# Final probability
fraud_probability = min(risk_score, 100)

st.metric("AI Fraud Probability", f"{fraud_probability}%")

# Decision threshold
threshold = 60

if fraud_probability >= threshold:
    st.error("🚫 Transaction Blocked (Fraud Detected)")
    st.warning("Potential Financial Loss Prevented")
else:
    st.success("✅ Transaction Approved (Legitimate)")

# ======================================================
# 5. BENEFITS AND RISKS
# ======================================================
st.header("5️⃣ Benefits and Risks of ML in Fraud Detection")

col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Benefits")
    st.markdown("""
    - Real-time fraud detection  
    - Reduces financial losses  
    - Improves customer security  
    - Scalable across millions of transactions  
    """)

with col2:
    st.subheader("⚠️ Risks")
    st.markdown("""
    - False positives (blocking genuine users)  
    - False negatives (missing fraud cases)  
    - Model bias  
    - Dependence on data quality  
    """)

st.divider()

# ======================================================
# FINAL TAKEAWAY
# ======================================================
st.success("""
**Final Takeaway:**  
Machine Learning is a powerful tool for detecting fraud,  
but it must be carefully designed to balance **security and customer experience**.
""")

# ======================================================
# FOOTER
# ======================================================
st.markdown("""
<hr>
<div style="text-align:center; font-size:14px;">
<b>Student Name:</b> Sanjay Chidambaram<br>
<b>Course:</b> PGPISM 2025–26<br>
<b>Roll No.:</b> PGPISM02041<br><br>
</div>
""", unsafe_allow_html=True)
