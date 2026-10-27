# AI-Accelerator Toolkit

A Streamlit app for planning an enterprise AI programme: how ready each business unit is, what a reference cloud architecture could look like, what the ROI case might be, and how to get started with MLOps and GenAI Ops.

I built it as a demo of the planning tools that help when an AI programme spans many teams and regions.

> **Demo data only.** Everything the app shows is synthetic. The 350 business units in `dummy_enterprise_data.csv` are generated with Faker by `generate_dummy_data.py`, and the GenAI playground and document Q&A return simulated answers instead of calling a model. None of the figures in the app are real results.

## What's in it

The landing page (`app.py`) lets you pick one of two editions.

**Enterprise Edition**

- **Change readiness:** a readiness heatmap by region, maturity-score distributions and key insights across business units
- **Blueprint generator:** reference architectures by industry and cloud (Azure, AWS or GCP), with MLOps pipeline templates and cost estimates
- **ROI estimator:** ROI by region and industry, plus a custom ROI calculator with 3-year projections
- **MLOps toolkit:** a starter project structure, best-practice guides and implementation checklists

**GenAI Edition**

- **AI playground:** try prompts with different models, temperature and token settings. Responses, token counts and costs are simulated.
- **Document Q&A:** a walkthrough of a document question-answering flow (simulated)
- **Analytics dashboard:** usage, latency and cost views on generated data
- **Blueprint generator and ROI calculator** extended for LLM use cases
- **MLOps and GenAI Ops toolkit:** setup, monitoring and troubleshooting guides

## Run it locally

Tested with Python 3.12.

```bash
git clone https://github.com/sumankrsh/ai-accelerator-toolkit.git
cd ai-accelerator-toolkit
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501.

The sample data file is already in the repo. Run `python generate_dummy_data.py` if you want a fresh synthetic set.

To open one edition directly:

```bash
streamlit run pages/1_Enterprise_Edition.py
streamlit run pages/2_GenAI_Edition.py
```

To host it for free, connect a fork to [Streamlit Community Cloud](https://share.streamlit.io) and set the main file to `app.py`.

## Project structure

```
ai-accelerator-toolkit/
├── app.py                        # Landing page: pick an edition
├── pages/
│   ├── 1_Enterprise_Edition.py   # Readiness, blueprints, ROI, MLOps
│   └── 2_GenAI_Edition.py        # Playground, document Q&A, analytics, GenAI Ops
├── main.py                       # Standalone copy of the Enterprise Edition
├── main_genai.py                 # Standalone copy of the GenAI Edition
├── generate_dummy_data.py        # Builds the synthetic dataset
├── dummy_enterprise_data.csv     # 350 synthetic business units
├── requirements.txt
└── .streamlit/config.toml        # Theme and server settings
```

## Sample data

Each synthetic business unit has a region, industry and cloud provider, maturity scores (data, MLOps, governance), budget and estimated ROI, models in production, time to market and an implementation date. Change `generate_dummy_data.py` to add your own use cases or fields.

## Built with

Streamlit, pandas, Plotly and Faker.

## Contact

Built by Suman Mukherjee. Questions or ideas: [contactme@mukherjeesuman.com](mailto:contactme@mukherjeesuman.com) · [mukherjeesuman.com](https://www.mukherjeesuman.com)

## License

MIT
