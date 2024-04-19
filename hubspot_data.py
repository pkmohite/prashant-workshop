# This code has been created by Michael Kupermann (michael.kupermann@codersunlimited.com or michael@kupermann.com)
# The purpose of this code is to generate dummy data that simulates a realistic dataset for HubSpot CRM.
# This data can then be used for demonstrations, testing, or other purposes that require a representative dataset.
# You need to amend the HubSpot Sales and Service Pipelines before you import the data.
#
# Required Packages:
# 1. Faker: This package is used to generate the fake data for our dataset.
# 2. Pandas: This package is used to handle the data in a tabular format and to write the data to an Excel file.
# 3. DateTime: This package is used to generate realistic date data for the 'close_date' field.
#
# To install the necessary packages, you can use pip, the Python package installer.
# Open your terminal (or command prompt on Windows), and enter the following commands:
# pip install faker
# pip install pandas
# pip install datetime
#
# If you're using a Jupyter notebook, you can prefix these commands with an exclamation mark:
# !pip install faker
# !pip install pandas
# !pip install datetime

from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

#  Function to generate data for a given country. Here 100 companies with 10 contacts, deals, tickets for each company
def generate_data(country, company_rows=100, contacts_per_company=10, deals_per_company=10, products_per_deal=10 )
    # Set the locale for Faker based on the country
    if country == "Germany":
        faker = Faker("de_DE")
    elif country == "United States":
        faker = Faker("en_US")
    elif country == "France":
        faker = Faker("fr_FR")
    elif country == "Italy":
        faker = Faker("it_IT")
    elif country == "Japan":
        faker = Faker("ja_JP")
    elif country == "United Kingdom":
        faker = Faker("en_GB")
    elif country == "Canada":
        faker = Faker("en_CA")
    elif country == "Austria":
        faker = Faker("de_AT")
    elif country == "Switzerland":
        faker = Faker("de_CH")

    # Create a dictionary to hold the data
    data = {
        "company_name": [],
        "company_domain": [],
        "company_industry": [],
        "company_address": [],
        "company_country": [],
        "contact_firstname": [],
        "contact_lastname": [],
        "contact_email": [],
        "contact_phone": [],
        "contact_address": [],
        "contact_country": [],
        "contact_function": [],
        "contact_department": [],
        "deal_name": [],
        "deal_stage": [],
        "deal_amount": [],
        "deal_type": [],
        "deal_source": [],
        "close_date": [],
        "ticket_title": [],
        "ticket_status": [],
        "ticket_priority": [],
        "product_name": [],
        "product_price": [],
        "product_description": [],
        "product_sku": [],
        "product_quantity": [],
    }

    # Loop to generate data for each company
    for _ in range(company_rows )
        company_name = faker.company()
        company_domain = faker.domain_name()
        company_industry = faker.random_element(["Technology", "Healthcare", "Finance", "Real Estate"])
        company_address = faker.address().replace('\n', ', ')
        company_country = country

        # Loop to generate data for each contact
        for _ in range(contacts_per_company )
            contact_firstname = faker.first_name()
            contact_lastname = faker.last_name()
            contact_email = faker.email()
            contact_phone = faker.phone_number()
            contact_address = faker.address().replace('\n', ', ')
            contact_country = country
            contact_function = faker.job()
            contact_department = faker.random_element(["Sales", "Marketing", "Human Resources", "Engineering"])

            # Append generated company and contact data to the lists in the dictionary
            data["company_name"].append(company_name)
            data["company_domain"].append(company_domain)
            data["company_industry"].append(company_industry)
            data["company_address"].append(company_address)
            data["company_country"].append(company_country)
           
            data["contact_firstname"].append(contact_firstname)
            data["contact_lastname"].append(contact_lastname)
            data["contact_email"].append(contact_email)
            data["contact_phone"].append(contact_phone)
            data["contact_address"].append(contact_address)
            data["contact_country"].append(contact_country)
            data["contact_function"].append(contact_function)
            data["contact_department"].append(contact_department)

            # Generate deal and product data
            data["deal_name"].append(f'Deal-{faker.uuid4()}')
            data["deal_stage"].append(faker.random_element(["Appointment Scheduled", "Qualified To Buy", "Presentation Scheduled", "Decision Maker Brought-In"]))
            data["deal_amount"].append(faker.random_int(min=1000, max=50000))
            data["deal_type"].append(faker.random_element(["New Business", "Existing Business"]))
            data["deal_source"].append(faker.random_element(["Direct Traffic", "Organic Search", "Paid Search", "Social Media"]))
            data["close_date"].append((datetime.today() + timedelta(days=faker.random_int(min=1, max=90))).date())

            # Generate product data
            data["product_name"].append(f'Product-{faker.uuid4()}')
            data["product_price"].append(faker.random_int(min=10, max=1000))
            data["product_description"].append(faker.catch_phrase())
            data["product_sku"].append(faker.random_int(min=10000, max=99999))
            data["product_quantity"].append(faker.random_int(min=1, max=100))

            # Generate ticket data
            data["ticket_title"].append(f'Ticket-{faker.uuid4()}')
            data["ticket_status"].append(faker.random_element(["New", "Waiting on contact", "Waiting on us", "Closed"]))
            data["ticket_priority"].append(faker.random_element(["Low", "Medium", "High"]))

    # Convert the data dictionary to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

# Define the list of countries for which we want to generate data
g7_countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States", "Austria", "Switzerland"]

# Create an empty DataFrame to hold the generated data
result = pd.DataFrame()
for country in g7_countries:
    df = generate_data(country)
    # Append the data for each country to the result DataFrame
    result = result.append(df)

# Write the generated data to an Excel file
result.to_excel(r"C:\~\~\~\hubspot_dummy_data.xlsx", index=False)