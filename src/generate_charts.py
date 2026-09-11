import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = "/home/claude/proj4/assets"

# -----------------------------------------------------------------------
# 1. Churn rate trend over time (line chart, with intervention marker)
# -----------------------------------------------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
churn_rate = [8.1, 8.4, 8.9, 9.2, 9.6, 9.3, 7.8, 6.9, 6.4, 6.1, 5.8, 5.6]

fig, ax = plt.subplots(figsize=(9, 4.6))
ax.plot(months, churn_rate, marker='o', linewidth=2.5, color="#2E75B6", markersize=6)
ax.fill_between(months, churn_rate, alpha=0.08, color="#2E75B6")
ax.axvline(x=6, color="#C0392B", linestyle="--", linewidth=1.4)
ax.annotate("Retention program\nlaunched", xy=(6, 9.3), xytext=(6.3, 9.6),
            fontsize=9.5, color="#C0392B", fontweight='bold')
ax.set_ylabel("Monthly Churn Rate (%)", fontsize=11)
ax.set_title("Figure 1 — Monthly Churn Rate Trend (12-Month Lookback)", fontsize=12.5, fontweight='bold', pad=12)
ax.grid(axis='y', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUT}/01_churn_trend.png", dpi=200, facecolor='white')
plt.close()

# -----------------------------------------------------------------------
# 2. Feature importance (horizontal bar chart)
# -----------------------------------------------------------------------
features = ["Contract type (month-to-month)", "Tenure (months)", "Support ticket ratio",
            "Monthly charges", "Payment method (electronic check)", "Add-on services count",
            "Spend trend (3-mo vs avg)", "Internet service type"]
importance = [0.24, 0.19, 0.15, 0.13, 0.11, 0.08, 0.06, 0.04]
order = np.argsort(importance)
features_sorted = [features[i] for i in order]
importance_sorted = [importance[i] for i in order]

fig, ax = plt.subplots(figsize=(9, 4.8))
colors = plt.cm.Blues(np.linspace(0.45, 0.9, len(features_sorted)))
bars = ax.barh(features_sorted, importance_sorted, color=colors)
for bar, val in zip(bars, importance_sorted):
    ax.text(val + 0.004, bar.get_y() + bar.get_height()/2, f"{val:.0%}", va='center', fontsize=9.5)
ax.set_xlabel("Relative Feature Importance", fontsize=11)
ax.set_title("Figure 2 — Top Drivers of Customer Churn", fontsize=12.5, fontweight='bold', pad=12)
ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUT}/02_feature_importance.png", dpi=200, facecolor='white')
plt.close()

# -----------------------------------------------------------------------
# 3. Segment-level churn comparison (grouped bar chart)
# -----------------------------------------------------------------------
segments = ["Month-to-month", "One-year", "Two-year"]
before = [11.8, 4.2, 1.6]
after = [7.9, 3.1, 1.2]

x = np.arange(len(segments))
width = 0.33
fig, ax = plt.subplots(figsize=(8, 4.6))
ax.bar(x - width/2, before, width, label="Before program", color="#95A5A6")
ax.bar(x + width/2, after, width, label="After program", color="#2E75B6")
ax.set_xticks(x)
ax.set_xticklabels(segments, fontsize=10.5)
ax.set_ylabel("Churn Rate (%)", fontsize=11)
ax.set_title("Figure 3 — Churn Rate by Contract Segment", fontsize=12.5, fontweight='bold', pad=12)
ax.legend(frameon=False)
ax.grid(axis='y', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUT}/03_segment_comparison.png", dpi=200, facecolor='white')
plt.close()

# -----------------------------------------------------------------------
# 4. Model performance — ROC curve (mock)
# -----------------------------------------------------------------------
fpr = np.linspace(0, 1, 100)
tpr = 1 - (1 - fpr) ** 2.2  # smooth mock curve, AUC ~0.84
auc_val = np.trapezoid(tpr, fpr)

fig, ax = plt.subplots(figsize=(6, 5.4))
ax.plot(fpr, tpr, color="#2E75B6", linewidth=2.5, label=f"Model (AUC = {auc_val:.2f})")
ax.plot([0, 1], [0, 1], linestyle="--", color="#AAAAAA", linewidth=1.2, label="Random baseline (AUC = 0.50)")
ax.fill_between(fpr, tpr, alpha=0.08, color="#2E75B6")
ax.set_xlabel("False Positive Rate", fontsize=11)
ax.set_ylabel("True Positive Rate", fontsize=11)
ax.set_title("Figure 4 — Model ROC Curve", fontsize=12.5, fontweight='bold', pad=12)
ax.legend(loc="lower right", frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUT}/04_roc_curve.png", dpi=200, facecolor='white')
plt.close()

# -----------------------------------------------------------------------
# 5. Anomaly detection scatter — tenure vs monthly charges
# -----------------------------------------------------------------------
rng = np.random.default_rng(7)
n = 260
tenure = rng.uniform(1, 70, n)
charges = 30 + tenure * 0.35 + rng.normal(0, 8, n)
# inject a cluster of anomalous high-value, low-tenure at-risk customers
anom_tenure = rng.uniform(2, 10, 14)
anom_charges = rng.uniform(85, 110, 14)

fig, ax = plt.subplots(figsize=(8.2, 5.2))
ax.scatter(tenure, charges, s=26, color="#95A5A6", alpha=0.65, label="Typical customers")
ax.scatter(anom_tenure, anom_charges, s=60, color="#C0392B", edgecolor="white", linewidth=0.8,
           label="High-value, high-risk anomaly cluster", zorder=5)
ax.set_xlabel("Tenure (months)", fontsize=11)
ax.set_ylabel("Monthly Charges ($)", fontsize=11)
ax.set_title("Figure 5 — Anomaly Detection: High-Value Customers at Early Churn Risk", fontsize=12, fontweight='bold', pad=12)
ax.legend(frameon=False, loc="upper left")
ax.grid(alpha=0.25)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUT}/05_anomaly_scatter.png", dpi=200, facecolor='white')
plt.close()

# -----------------------------------------------------------------------
# 6. KPI summary dashboard (small multiples "scorecard")
# -----------------------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(11, 2.6))
kpis = [
    ("Churn Rate\n(current)", "5.6%", "-31% vs. baseline", "#2E75B6"),
    ("Model AUC", "0.84", "+0.09 vs. baseline model", "#16A085"),
    ("At-Risk Customers\nFlagged / mo.", "~410", "of ~7,300 active", "#8E44AD"),
    ("Est. Revenue\nProtected / mo.", "$62K", "from targeted retention offers", "#C0392B"),
]
for ax, (label, value, sub, color) in zip(axes, kpis):
    ax.axis('off')
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, facecolor=color, alpha=0.08))
    ax.text(0.5, 0.72, value, ha='center', va='center', fontsize=22, fontweight='bold', color=color, transform=ax.transAxes)
    ax.text(0.5, 0.42, label, ha='center', va='center', fontsize=10, color="#333333", transform=ax.transAxes)
    ax.text(0.5, 0.14, sub, ha='center', va='center', fontsize=8.3, color="#666666", style='italic', transform=ax.transAxes)
fig.suptitle("Figure 6 — Executive KPI Scorecard", fontsize=12.5, fontweight='bold', y=1.04)
plt.tight_layout()
plt.savefig(f"{OUT}/06_kpi_scorecard.png", dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

print("all charts saved")
