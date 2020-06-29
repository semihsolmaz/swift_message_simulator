import pandas as pd
import random
from mt103 import mt103
from mt700 import mt700


message_type = int(input('Enter message type: '))
message_count = int(input('Enter message count: '))

countries = pd.read_csv('./data/country_data.csv')
companies = pd.read_csv('./data/companies_sorted.csv', nrows=20000)
company_names = companies[['name', 'locality']].dropna()
banks = pd.read_csv('./data/banks_bic_name.csv')
bank_names = banks[['name_branch', 'Country']]
bank_bic = banks['bic_branch']
val_weights = random.choices([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],
                             weights=[1, 5, 200, 210, 150, 50, 25, 10, 5, 1], k=1000)
words_tag70 = ['INVOICE', 'INV', 'GIFT', 'ITUNES', 'GIFT CARD', 'GOOGLE', 'AMAZON', 'INVESTMENT']
currency_l = pd.read_csv('./data/currency-codes.csv')
w_currencies = random.choices(currency_l['cur_code'], weights=currency_l['weight'], k=10000)

country_l = random.choices(countries['Code'], weights=countries['weight'], k=message_count)

if message_type == 103:
    mt103(bank_bic, bank_names, companies, company_names, country_l, val_weights, words_tag70, currency_l, w_currencies)
elif message_type == 700:
    mt700(bank_bic, companies, company_names, country_l, val_weights, currency_l, w_currencies)
else:
    print('undefined message type!!')

