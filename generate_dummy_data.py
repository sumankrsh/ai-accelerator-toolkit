from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
rows = []

industries = ['Insurance', 'Healthcare', 'Retail', 'Banking', 'Manufacturing', 'Technology', 'Energy', 'Telecommunications']
regions = ['US-East', 'US-West', 'EMEA', 'APAC', 'LATAM', 'Canada', 'MEA']
cloud_providers = ['Azure', 'AWS', 'GCP', 'Multi-Cloud']
ai_use_cases = ['Customer Churn Prediction', 'Fraud Detection', 'Demand Forecasting', 'Personalization', 
                 'Predictive Maintenance', 'Document Processing', 'Risk Assessment', 'Quality Control']

for i in range(350):
    industry = random.choice(industries)
    region = random.choice(regions)
    cloud_ready = random.random() > 0.3
    data_maturity = random.randint(1, 10)
    mlops_maturity = random.randint(1, 10)
    
    # More realistic ROI based on maturity scores
    base_roi = (data_maturity + mlops_maturity) / 2
    roi_multiplier = 1.5 if cloud_ready else 1.0
    roi = round(base_roi * roi_multiplier * random.uniform(0.8, 1.2), 2)
    
    # Additional metrics
    data_volume_tb = round(random.uniform(0.5, 500), 1)
    models_in_production = int(mlops_maturity * random.uniform(0.5, 3))
    time_to_market_days = int(180 / (mlops_maturity / 2))
    
    rows.append({
        'Business_Unit': fake.company(),
        'Region': region,
        'Industry': industry,
        'Cloud_Provider': random.choice(cloud_providers),
        'Cloud_Ready': cloud_ready,
        'Data_Maturity_Score': data_maturity,
        'ML_Ops_Maturity_Score': mlops_maturity,
        'Data_Volume_TB': data_volume_tb,
        'Models_In_Production': models_in_production,
        'Time_To_Market_Days': time_to_market_days,
        'Primary_AI_Use_Case': random.choice(ai_use_cases),
        'Annual_IT_Budget_Million': round(random.uniform(5, 100), 1),
        'AI_Investment_Percentage': round(random.uniform(5, 25), 1),
        'Estimated_AI_ROI_MillionUSD': roi,
        'Implementation_Date': fake.date_between(start_date='-2y', end_date='today'),
        'Technical_Debt_Score': random.randint(1, 10),
        'Data_Governance_Score': random.randint(1, 10),
        'Team_Size': random.randint(5, 150),
        'AI_Skilled_Resources': int(random.randint(5, 150) * mlops_maturity / 10)
    })

df = pd.DataFrame(rows)

# Calculate additional derived metrics
df['Overall_Readiness_Score'] = (df['Data_Maturity_Score'] + df['ML_Ops_Maturity_Score'] + 
                                  df['Data_Governance_Score']) / 3
df['ROI_Potential'] = df['Estimated_AI_ROI_MillionUSD'] / df['Annual_IT_Budget_Million'] * 100

# Save to CSV
df.to_csv('dummy_enterprise_data.csv', index=False)

print(f"Generated {len(df)} rows of dummy enterprise data")
print(f"Columns: {list(df.columns)}")
print(f"\nSample data:")
print(df.head())