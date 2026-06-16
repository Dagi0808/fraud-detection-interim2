# Fraud Detection System - Adey Innovations Inc.

## 📋 Project Overview

End-to-end **Machine Learning solution** for detecting fraudulent transactions in **e-commerce** and **bank credit card** data. 

The system effectively handles highly imbalanced data, engineers behavioral features, trains strong models, and provides **explainable** insights using SHAP to support business decisions.

---

## ✨ Key Features

### Task 1: Data Analysis & Preprocessing
- Data cleaning and type conversion
- Feature engineering: `time_since_signup`, `hour_of_day`, `day_of_week`
- High-cardinality columns dropped (`device_id`, `user_id`, `ip_address`)
- Categorical encoding for low-cardinality features
- SMOTE applied **only on training set**

### Task 2: Model Building & Training
- **Baseline**: Logistic Regression
- **Best Model**: XGBoost (with `scale_pos_weight` for imbalance)
- Evaluation using **AUC-PR** (primary metric), F1-Score, ROC-AUC, Confusion Matrix
- Models saved in `models/` folder

### Task 3: Model Explainability
- SHAP Global Summary Plots
- Individual Force Plots
- Actionable business recommendations derived from feature importance

---

## 🚀 Business Recommendations

1. **Signup Velocity Check**  
   Flag transactions occurring **within 4 hours of signup** for extra verification (2FA / manual review).

2. **High-Risk Traffic Monitoring**  
   Increase scrutiny on transactions from `"Ads"` source and suspicious browser combinations.

3. **Value + Timing Rules**  
   Trigger additional checks for high `purchase_value` transactions during unusual hours (e.g., 2–5 AM).

---

## 📁 Project Structure
fraud-detection/
├── data/raw/                  # Original datasets
├── notebooks/                 # EDA, Modeling, SHAP notebooks
├── src/                       # Data loading, preprocessing, feature engineering
├── models/                    # Trained model files (.pkl)
├── notebooks/shap_plots/      # SHAP visualizations
├── scripts/                   # Reproducible scripts
├── requirements.txt
└── README.md
text---

## 🛠️ How to Run

1. **Clone & Setup**
   ```bash
   git clone <your-repo-url>
   cd fraud-detection
   pip install -r requirements.txt

Run PipelineBashpython scripts/preprocess.py
python scripts/modeling.py
python scripts/shap_explain.py
Open notebooks for detailed exploration.


📊 Technologies

Core: Python, pandas, scikit-learn, XGBoost
Imbalance: imbalanced-learn (SMOTE)
Explainability: SHAP
Visualization: matplotlib, seaborn


Status: Complete (Task 1 + Task 2 + Task 3)
Branch: main (all tasks merged)
Submitted for Adey Innovations FinTech Challenge - June 16, 2026
text---

### **Update Command (Recommended)**

Run this to overwrite your README with the new content:

```bash
cat > README.md << 'EOF'
[PASTE THE ENTIRE MARKDOWN ABOVE HERE]
EOF