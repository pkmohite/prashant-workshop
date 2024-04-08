import pandas as pd
import thepassiveinvestor as pi

class ETFData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = pi.collect_data(symbol)

    def display_summary(self):
        summary = f'{self.data["summary"]}'
        return summary

    def display_sector_holdings(self):
        sector_holdings = self.data['sector_holdings']
        sector_holdings_table = pd.DataFrame(sector_holdings.items(), columns=['Sector', 'Percentage'])
        return sector_holdings_table

    def display_company_holdings(self):
        company_holdings = self.data['company_holdings']
        company_holdings_table = pd.DataFrame(company_holdings.items(), columns=['Company', 'Percentage'])
        return company_holdings_table

    def display_annual_returns(self):
        annual_returns = self.data['annual_returns']
        annual_returns_table = pd.DataFrame(annual_returns.items(), columns=['Year', 'Percentage'])
        return annual_returns_table

    def display_risk_data(self):
        risk_data_table = pd.DataFrame(self.data['risk_data'])
        return risk_data_table

    def display_key_characteristics(self):
        key_characteristics = self.data['key_characteristics']
        key_characteristics_table = pd.DataFrame(key_characteristics.items(), columns=['Characteristic', 'Value'])
        return key_characteristics_table

# Usage example
etf = ETFData('SPY')
# summary = etf.display_summary()
# sector_holdings = etf.display_sector_holdings()
# company_holdings = etf.display_company_holdings()
# annual_returns = etf.display_annual_returns()
risk_data = etf.display_risk_data()
# key_characteristics = etf.display_key_characteristics()

# print(summary)
# print(sector_holdings)
# print(company_holdings)
# print(annual_returns)
# print(risk_data)
print(risk_data['5y']['sharpeRatio'])
# print(key_characteristics)