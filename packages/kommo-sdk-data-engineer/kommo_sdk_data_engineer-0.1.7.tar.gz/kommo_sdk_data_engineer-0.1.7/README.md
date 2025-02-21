# kommo SDK for Data Enginner

# Overview
kommo SDK for Data Enginner is a comprehensive Python SDK designed for data engineers working with the Kommo API. It simplifies API integration, data extraction, and transformation processes, making it easier to manage and analyze data efficiently.

# Installation
```bash
pip install kommo-sdk-data-engineer
```

# How to Use
```python
from kommo_sdk_data_engineer import KommoConfig, Leads

TOKEN_LONG_DURATION = '[TOKEN]'
URL_COMPANY = 'https://[YOUR_COMPANY].kommo.com'


config_kommo = KommoConfig(url_company=URL_COMPANY, token_long_duration=TOKEN_LONG_DURATION)
leads = Leads(config=config_kommo, output_verbose=True)
all_leads = leads.get_all_leads_list(with_params=['contacts', 'loss_reason'])

# To Dataframe
df_leads = leads.to_dataframe(leads.all_leads())
df_leads_custom_fields = leads.to_dataframe(leads.all_custom_field_values())
df_leads_contacts = leads.to_dataframe(leads.all_contacts())
df_leads_loss_reasons = leads.to_dataframe(leads.all_loss_reasons())
df_leads_tags = leads.to_dataframe(leads.all_tags())
```

# Contact
For any questions or support, please contact: mailson.nascin@gmail.com.
