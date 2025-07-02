# Ai-policy-gap-finder
🧠 AI Policy Gap Finder

A lightweight AI-powered tool to identify gaps between internal policies and ISO 27001:2022 controls using a **locally hosted Large Language Model (LLM)** via **LM Studio**.

This project was created as a personal learning initiative to explore the application of AI in **Governance, Risk & Compliance (GRC)** — especially in cybersecurity audit and policy evaluation contexts.

🎯 Project Purpose
To automate first-level policy reviews by simulating a cybersecurity auditor's assessment, helping GRC teams quickly identify where internal documentation aligns or falls short of ISO 27001 requirements. (This project uses synthetic and paraphrased ISO 27001:2022 control descriptions for demo purposes only.)

🔍 Output
`audit_results.txt` contains AI-generated evaluations of internal policy compliance against  synthetic data ISO 27001 controls.

🚀 How to Run
1. Prerequisites
- Python 3.7 or higher
- [LM Studio](https://lmstudio.ai/) with a supported model running (`meta-llama-3-8b-instruct`)

2. Install Dependencies
```bash
pip install -r requirements.txt


📁 Project Structure
├── data/
│   ├── iso-controls.json         //Synthetic ISO 27001 controls
│   ├── internal_policy.txt       //Sample internal policy statements
│   └── audit_results.txt         
├── policy-gap-finder.py          
├── requirements.txt              
└── README.md                    


✅ Features
Simulates AI-based GRC policy assessments
Works completely offline using local LLM
ISO 27001:2022-focused (synthetic data content)
Easy-to-understand output for GRC teams or auditors
