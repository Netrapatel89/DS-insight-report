# Customer Churn Insights — Data Science Report & Presentation Plan

Week 4 capstone: a polished, executive-facing report that consolidates a hypothetical
churn-analysis project into clear findings, visualizations, and a communication plan
for non-technical stakeholders.

## Contents

- [`docs/Data_Science_Insights_Report.docx`](docs/Data_Science_Insights_Report.docx) — full report: executive summary, methodology, insights, presentation strategy, recommendations
- [`assets/`](assets) — the six mock-up visualizations used in the report (trend, feature importance, segment comparison, ROC curve, anomaly scatter, KPI scorecard)
- [`src/generate_charts.py`](src/generate_charts.py) — reproducible script that generates every chart in `assets/`
- [`slides/outline.md`](slides/outline.md) — slide-by-slide narrative outline for presenting these findings live

## Project structure

```
ds-insights-report/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── Data_Science_Insights_Report.docx
├── assets/
│   ├── 01_churn_trend.png
│   ├── 02_feature_importance.png
│   ├── 03_segment_comparison.png
│   ├── 04_roc_curve.png
│   ├── 05_anomaly_scatter.png
│   └── 06_kpi_scorecard.png
├── src/
│   └── generate_charts.py
└── slides/
    └── outline.md
```

## Report summary

1. **Executive summary** — churn fell from 9.6% to 5.6% after a retention program launch; model AUC of 0.84.
2. **Methodology** — data foundations, feature engineering, classification modeling, anomaly detection, and translation of model output into an operational risk tier.
3. **Insights & visualizations** — six purpose-built charts, each chosen to match the shape of the insight it conveys (trend, ranking, comparison, classifier quality, outliers, and an executive scorecard).
4. **Presentation strategy** — a narrative arc and storytelling techniques for communicating technical results to non-technical stakeholders.
5. **Recommendations** — immediate, medium-term, and longer-term next steps for the retention and analytics teams.

See `docs/Data_Science_Insights_Report.docx` for the complete write-up.

## Regenerating the charts

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_charts.py
```

## License

For coursework / educational use.
