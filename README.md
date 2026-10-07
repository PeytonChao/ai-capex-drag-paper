# Enterprise Software vs. Hardware Net Margin Sensitivity to AI CapEx (2024–2026)

## Overview
Replication pipeline and panel econometrics for research on firm-level operating margin sensitivity to AI capital expenditure across enterprise software vs. hardware sectors.

## Repository Structure
```
ai-capex-drag-paper/
├── data/
│   ├── raw_financials.csv
│   └── panel_dataset_clean.csv
├── scripts/
│   ├── 01_fetch_data.py
│   ├── 02_clean_panel.py
│   └── 03_run_regressions.py
├── outputs/
│   └── regression_results.txt
├── .gitignore
└── README.md
```

## Replication Instructions
1. Install dependencies:
   ```bash
   pip install pandas yfinance linearmodels statsmodels
   ```
2. Fetch financial data:
   ```bash
   python3 scripts/01_fetch_data.py
   ```
3. Clean panel dataset:
   ```bash
   python3 scripts/02_clean_panel.py
   ```
4. Run panel fixed effects regressions:
   ```bash
   python3 scripts/03_run_regressions.py
   ```

## Key Findings
- **Hardware Baseline CapEx Drag:** $\beta = -0.6204$ ( = 0.0320$), showing initial margin compression from hardware infrastructure builds.
- **Enterprise Software Moderation:** $\beta_{\text{interaction}} = +0.5194$ ( = 0.0952$), demonstrating significant margin insulation due to software scalability.
