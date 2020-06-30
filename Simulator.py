import pandas as pd
import random
from mt103 import mt103
from mt700 import mt700
import stomp
import time
import sys
from datetime import datetime, timedelta

sim_mode = input('1-init:\n2-prod:\n')
if sim_mode == '2':
    conn_type = input('Choose connection type:\n1: jms\n2: file\n ')
    date_list = [datetime.today().strftime('%Y%m%d')[2:], (datetime.today() + timedelta(days=1)).strftime('%Y%m%d')[2:],
                 (datetime.today() + timedelta(days=2)).strftime('%Y%m%d')[2:]]
    period = int(input('enter period for messages to be create in sec: '))
else:
    conn_type = '2'
    back_days = int(input('Enter back days: '))
    date_list = []
    while back_days >= 0:
        date_list.append((datetime.today() - timedelta(days=back_days)).strftime('%Y%m%d')[2:])
        back_days = back_days - 1

message_type = input('Enter message type: ')


message_count = int(input('Enter message count: '))

print(date_list)
# conn = stomp.Connection([('13.95.109.53', 61613)])
# conn.connect('admin', 'admin', wait=True)
# conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')
# time.sleep(2)
# conn.disconnect()


#todo: Add JMS and postgress out path.
out_path = 'C:\\Users\\semih\\PycharmProjects\\swift_message_simulator\\messages\\'


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

if message_type == '103':
    mt103(bank_bic, bank_names, companies, company_names, country_l, val_weights, words_tag70, currency_l, w_currencies,out_path, date_list, period)
elif message_type == '700':
    mt700(bank_bic, companies, company_names, country_l, val_weights, currency_l, w_currencies, out_path, date_list)
else:
    print('undefined message type!!')

