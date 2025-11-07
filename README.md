# Insight-Innovators-Group-12-

# 🫀 Heart Disease Prediction Analysis  
### *A Data-Driven Approach to Healthcare*

**Date:** November 8, 2025  
**Presented by:** *INSIGHT INNOVATORS (Group 12)*  

---

## 📌 Project Overview
The primary goal of this project is to **predict the presence or absence of heart disease** based on patient health attributes using **machine learning techniques**.

### 🎯 Objectives
- Identify key risk factors contributing to heart disease  
- Develop and evaluate predictive models  
- Support early diagnosis and prevention strategies  

---

## 🧾 Dataset Overview
| Detail | Description |
|--------|--------------|
| **Original Size** | 1025 rows × 14 columns |
| **After Cleaning** | 302 unique rows × 14 columns |
| **Duplicates Removed** | 723 |
| **Data Type** | Patient medical records |
| **Goal Variable** | Presence (1) or Absence (0) of heart disease |

### ⚙️ Data Cleaning
- **Duplicate Handling:** Removed 723 exact duplicates to prevent bias and data leakage.  
- **Outlier Management:** Applied logarithmic transformation on *trestbps* and *chol* to reduce skewness.  
- **Result:** Clean dataset of 302 unique records ready for analysis.

---

## 👥 Demographic Insights
- **Age:** Most heart disease cases occur in the **50–60** age group.  
- **Gender:**  
  - Males: 75% prevalence  
  - Females: 44.7% prevalence  
- **Insight:** Age and gender are major risk factors — older males show the highest susceptibility.

---

## 🧪 Clinical Factors
- **Chest Pain (cp):** cp = 1 or 2 strongly associated with heart disease.  
- **Major Vessels (ca):** ca = 0 → highest heart disease positivity rate.  
- **Thalassemia (thal):** thal = 2 → high correlation with heart disease.  

**Key Takeaway:** Clinical indicators such as **ca**, **cp**, and **thal** play crucial roles in diagnosis.

---

## 📊 Feature Correlation Analysis
| Feature | Correlation with Heart Disease | Interpretation |
|----------|-------------------------------|----------------|
| `cp` | +0.43 | Strong positive correlation |
| `thalach` | +0.42 | Higher max heart rate → higher risk |
| `exang` | -0.44 | Exercise-induced angina reduces likelihood |
| `oldpeak` | -0.43 | Lower ST depression → higher risk |
| `ca` | -0.39 | Fewer vessels colored → higher risk |

---

## 🤖 Model Selection
Four machine learning models were trained and evaluated:

| Model | Description |
|--------|-------------|
| **Logistic Regression** | Linear model for binary classification |
| **Decision Tree** | Rule-based non-linear model |
| **Random Forest** | Ensemble of multiple trees |
| **Gradient Boosting (XGBoost)** | Sequential ensemble learning model |

---

## 📈 Initial Model Performance (Before Tuning)
| Model | Accuracy (%) |
|--------|--------------|
| Logistic Regression | 86.1 |
| Decision Tree | 98.8 |
| Random Forest | 99.7 |
| XGBoost | 99.7 |

*Note:* Extremely high accuracies were observed due to duplicate data causing data leakage.

---

## 🧹 After Removing Duplicates (True Cross-Validation Results)
| Model | Mean Accuracy | Std. Deviation |
|--------|----------------|----------------|
| **Logistic Regression** | **0.8543** | 0.0520 |
| Random Forest | 0.8211 | 0.0756 |
| XGBoost | 0.8011 | 0.0441 |
| Decision Tree | 0.7416 | 0.0348 |

**Interpretation:**  
- Logistic Regression generalizes best on unique patient data.  
- Tree-based models dropped in accuracy after duplicates were removed, confirming prior overfitting.  
- Cross-validation gives a more honest, stable performance estimate than a single train/test split.

---

## 🧮 Model Evaluation (Random Forest Example)
**Performance Metrics**
| Metric | Score |
|--------|--------|
| Accuracy | 85% |
| Precision | 81% |
| Recall | 90% |

**Confusion Matrix Summary:**
- **True Positives:** 26  
- **True Negatives:** 26  
- **False Positives:** 6  
- **False Negatives:** 3  

---

## 🛠️ Hyperparameter Tuning (Random Forest)
**Tool Used:** `GridSearchCV`  

**Parameters Tuned:**
- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `max_features`

**Outcome:**
- Accuracy remained at 85%, but  
- **Precision (class 0)** improved from *0.90 → 0.93*  
- **Recall (class 1)** improved from *0.90 → 0.93*  
- Model became more balanced and reliable.

---

## 🧩 Key Insights
- **Removing duplicates** prevents inflated accuracy and ensures genuine model evaluation.  
- **Cross-validation** offers a better estimate of real-world performance.  
- **Logistic Regression** provides the best generalization on clean data.  
- **Random Forest**, while strong, may overfit small or redundant datasets.

---

## 🚀 Conclusion
- **Best Performing Model:** Random Forest (post-tuning)  
- **Best Generalizing Model:** Logistic Regression (based on CV)  
- **Accuracy Achieved:** ~85%  
- **Most Influential Features:** `cp`, `thalach`, `exang`, `oldpeak`, `ca`

---

## 🔭 Future Work
- Apply **advanced ensemble techniques** (Stacking, Voting Classifiers)  
- Integrate **larger and more diverse clinical datasets**  
- Use **explainable AI tools (SHAP, LIME)** for better interpretability  
- Develop a **real-time prediction dashboard** for healthcare use

---

## 🧑‍💻 Technologies Used
- **Python Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`  
- **Tools:** Jupyter Notebook, GridSearchCV, Cross-Validation  
- **Version Control:** GitHub  

---

## 📚 Acknowledgments
- *INSIGHT INNOVATORS (Group 12)*  
- TechCrush Community – Data Science Program 2025  

> “Data-driven healthcare empowers early intervention and saves lives.” ❤️

---
