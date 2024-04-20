from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
from openai import OpenAI
import random

client = OpenAI()
# Function to generate the email thread
def generate_email_thread(customer_name, customer_role, customer_company, customer_industry, sdr_name, account_manager_name):
    prompt = f"""
    You are an AI assistant tasked with simulating a realistic email conversation between the Monday.com sales team and a potential customer ({customer_company}, a {customer_industry} company) interested in their work management platform. The goal is to emulate a typical B2B sales cycle involving multiple stakeholders on the customer side.

    The initial inquiry should come from {customer_name}, the {customer_role} at {customer_company}, looking for a better work management solution for their team and outlining their specific pain points and requirements.

    {sdr_name}, a Sales Development Representative (SDR) from the Monday.com sales team, should respond by providing an initial overview of the Monday.com platform's key features and capabilities relevant to the customer's needs, while also discussing the implementation and onboarding approach.

    Other relevant stakeholders from {customer_company} should get looped in, such as project managers, department heads, or IT personnel, each with their own specific questions and concerns.

    {account_manager_name}, an Account Manager at Monday.com, should then aim to address all questions in more detail, and set up a call/demo to thoroughly evaluate how the platform can be tailored to the customer's unique workflows and requirements.

    The conversation flow and email cadence should accurately reflect the back-and-forth interactions that typically occur during a B2B sales process with multiple decision makers involved.

    Generate the entire email thread without any additional explanation/text, covering the sequence from initial inquiry through the pre-demo/evaluation stages. Focus on demonstrating realistic dialog, capturing different stakeholder perspectives, requirement gathering, and choreographing the appropriate resources from the Monday.com team to progress the opportunity.
    """

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].message.content


# Example usage
customer_name = "Sarah Johnson"
customer_role = "Operations Manager"
customer_company = "ABC Company"
customer_industry = "Marketing Agency"
sdr_name = "Mike Wilson"
account_manager_name = "Jane Doe"

email_thread = generate_email_thread(customer_name, customer_role, customer_company, customer_industry, sdr_name, account_manager_name)
print(email_thread)

#  Function to generate data for a given country. Here 100 companies with 10 contacts, deals, tickets for each company
def generate_data(country, company_rows=1, contacts_per_company=1, deals_per_company=10, products_per_deal=10 ):
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
        "conversation_thread": [],
        "proponent_recommendation": [],
        # "product_name": [],
        # "product_price": [],
        # "product_description": [],
        # "product_sku": [],
        # "product_quantity": [],
    }

    # Loop to generate data for each company
    for _ in range(company_rows ):
        company_name = faker.company()
        company_domain = faker.domain_name()
        company_industry = faker.random_element(["Technology", "Healthcare", "Finance", "Real Estate", "Retail"])
        company_address = faker.address().replace('\n', ', ')
        company_country = country

        # Loop to generate data for each contact
        for _ in range(contacts_per_company ):
            contact_firstname = faker.first_name()
            contact_lastname = faker.last_name()
            contact_email = faker.email()
            contact_phone = faker.phone_number()
            contact_address = faker.address().replace('\n', ', ')
            contact_country = country
            contact_department = faker.random_element(["Sales", "Marketing", "Human Resources", "Engineering"])
            # generate contact function based on department
            if contact_department == "Sales":
                contact_function = faker.random_element(["Sales Manager", "Account Executive", "Business Development Representative"])
            elif contact_department == "Marketing":
                contact_function = faker.random_element(["Marketing Manager", "Marketing Specialist", "Content Writer"])
            elif contact_department == "Human Resources":
                contact_function = faker.random_element(["HR Manager", "Recruiter", "Training Specialist"])
            else:
                contact_function = faker.random_element(["Software Engineer", "Product Manager", "Data Scientist"])

            conversation_thread = generate_email_thread(contact_firstname + " " + contact_lastname, contact_function, company_name, company_industry, "Mike Wilson", "Sarah Powers")

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
            data["deal_amount"].append(faker.random_int(min=1000, max=50000, step=3000))
            data["deal_type"].append(faker.random_element(["New Business", "Existing Business"]))
            data["deal_source"].append(faker.random_element(["Direct Traffic", "Organic Search", "Paid Search", "Social Media"]))
            data["close_date"].append((datetime.today() + timedelta(days=faker.random_int(min=1, max=90))).date())

            # # Generate product data
            # data["product_name"].append(f'Product-{faker.uuid4()}')
            # data["product_price"].append(faker.random_int(min=10, max=1000))
            # data["product_description"].append(faker.catch_phrase())
            # data["product_sku"].append(faker.random_int(min=10000, max=99999))
            # data["product_quantity"].append(faker.random_int(min=1, max=100))

            # Generate ticket data
            data["ticket_title"].append(f'Ticket-{faker.uuid4()}')
            data["ticket_status"].append(faker.random_element(["New", "Waiting on contact", "Waiting on us", "On hold"]))
            data["ticket_priority"].append(faker.random_element(["Low", "Medium", "High"]))

            # Append the conversation thread to the list
            data["conversation_thread"].append(conversation_thread)

            # Generate the proponent recommendation: generate a list of 7 numbers, each between 1 and 18
            proponent_recommendation = [random.randint(1, 18) for _ in range(7)]
            data["proponent_recommendation"].append(proponent_recommendation)

        # Success message
        print(f"Data generated for {company_name} in {country}.")
    
    # Convert the data dictionary to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

# # Generate data for the United States
# result = generate_data("United States",company_rows=10)

# # Write the generated data to a csv file
# result.to_csv("hubspot_data.csv", index=False)