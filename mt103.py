import math
import random
import uuid


def mt103(bank_bic, bank_names, company_d, company_names, country_list, val_weights, tag70_words, l_currency, w_currencies):
    l_52d_57d = country_list[:int(math.ceil(len(country_list) * 0.003))]
    l_52d = country_list[int(math.ceil(len(country_list) * 0.003)):int(math.ceil(len(country_list) * 0.006) + 1)]
    l_57d = country_list[int(math.ceil(len(country_list) * 0.006)) + 1:int(math.ceil(len(country_list) * 0.009)) + 1]
    l_52a = country_list[int(math.ceil(len(country_list) * 0.009)) + 1:int(math.ceil(len(country_list) * 0.1)) + 1]
    l_57a = country_list[int(math.ceil(len(country_list) * 0.1)) + 1:int(math.ceil(len(country_list) * 0.2)) + 1]
    l_52a_57a = country_list[int(math.ceil(len(country_list) * 0.2)) + 1:int(math.ceil(len(country_list) * 0.3)) + 1]
    l_basic = country_list[int(math.ceil(len(country_list) * 0.3)) + 1:]

    for c_code in l_52d_57d:
        if random.randint(0, 100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I103' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O1031454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        tag20 = "%0.6d" % random.randint(0, 999999)

        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)
        tag50k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50k_company = company1.iloc[0]['name'][:35]
        tag50k_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50k_companyaddress = ((tag50k_companyaddress_list[0].strip() + ',' + tag50k_companyaddress_list[1])[:35])[
                                :35] + \
                                '\n' + tag50k_companyaddress_list[2].strip()

        tag59k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59k_company = company2.iloc[0]['name'][:35]
        tag59k_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59k_companyaddress = ((tag59k_companyaddress_list[0].strip() + ',' + tag59k_companyaddress_list[1])[:35])[
                                :35] + \
                                '\n' + tag59k_companyaddress_list[2].strip()
        tag71a = random.choice(['SHA', 'OUR', 'BEN'])

        if random.randint(0, 100) < 3:
            tag70 = 'sample text ' + random.choice(tag70_words)
        else:
            tag70 = 'sample text '

        tag52d_account_number = "%0.10d" % random.randint(0, 9999999999)
        bank52d = bank_names.sample()[:35]
        bank52d_branch = bank52d.iloc[0]['name_branch'][:35]
        bank52d_country = bank52d.iloc[0]['Country']

        tag57d_account_number = "%0.10d" % random.randint(0, 9999999999)
        bank57d = bank_names.sample()[:35]
        bank57d_branch = bank57d.iloc[0]['name_branch'][:35]
        bank57d_country = bank57d.iloc[0]['Country']

        TB = '{4:\n:20:' + tag20 + '\n:23B:CRED\n:32A:' + '20' + "%0.2d" % random.randint(1,
                                                                                          6) + "%0.2d" % random.randint(
            1, 29) + currency + txn_val + '\n:50K:/' + tag50k_account_number + '\n' + tag50k_company \
             + '\n' + tag50k_companyaddress + '\n:59:/' + tag59k_account_number + '\n' + tag59k_company + '\n' + \
             tag59k_companyaddress + '\n:52D:/' + tag52d_account_number + '\n' + bank52d_branch + '\n' + bank52d_country \
             + '\n:57D:/' + tag57d_account_number + '\n' + bank57d_branch + '\n' + bank57d_country + '\n' + ':70:' + tag70 + '\n:71A:' + tag71a + '\n-}'

        content = BHB + AHB + UHB + TB

        message_file = open('C:\\Users\\semih\\PycharmProjects\\swift_sim\\messages\\' + (
                "%0.12d" % random.randint(0, 999999999999)) + '-103-52d-57d.txt', 'w')

        try:
            message_file.write(content)
            message_file.close()
        except:
            pass

    for c_code in l_52d:

        if random.randint(0, 100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I103' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O1031454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        tag20 = "%0.6d" % random.randint(0, 999999)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)

        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)

        tag50k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50k_company = company1.iloc[0]['name'][:35]
        tag50k_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50k_companyaddress = (tag50k_companyaddress_list[0].strip() + ',' + tag50k_companyaddress_list[1])[:35] + \
                                '\n' + tag50k_companyaddress_list[2].strip()

        tag59k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59k_company = company2.iloc[0]['name'][:35]
        tag59k_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59k_companyaddress = (tag59k_companyaddress_list[0].strip() + ',' + tag59k_companyaddress_list[1])[:35] + \
                                '\n' + tag59k_companyaddress_list[2].strip()
        tag71a = random.choice(['SHA', 'OUR', 'BEN'])

        if random.randint(0, 100) < 3:
            tag70 = 'sample text ' + random.choice(tag70_words)
        else:
            tag70 = 'sample text '

        tag52d_account_number = "%0.10d" % random.randint(0, 9999999999)
        bank52d = bank_names.sample()[:35]
        bank52d_branch = bank52d.iloc[0]['name_branch'][:35]
        bank52d_country = bank52d.iloc[0]['Country']

        TB = '{4:\n:20:' + tag20 + '\n:23B:CRED\n:32A:' + '20' + "%0.2d" % random.randint(1,
                                                                                          6) + "%0.2d" % random.randint(
            1, 29) + currency + txn_val + '\n:50K:/' + tag50k_account_number + '\n' + tag50k_company \
             + '\n' + tag50k_companyaddress + '\n:59:/' + tag59k_account_number + '\n' + tag59k_company + '\n' + \
             tag59k_companyaddress + '\n:52D:/' + tag52d_account_number + '\n' + bank52d_branch + '\n' + bank52d_country \
             + '\n' + ':70:' + tag70 + '\n:71A:' + tag71a + '\n-}'

        content = BHB + AHB + UHB + TB

        message_file = open('C:\\Users\\semih\\PycharmProjects\\swift_sim\\messages\\' + (
                "%0.12d" % random.randint(0, 999999999999)) + '-103-52d.txt', 'w')

        try:
            message_file.write(content)
            message_file.close()
        except:
            pass

    for c_code in l_57d:
        if random.randint(0, 100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I103' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O1031454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        tag20 = "%0.6d" % random.randint(0, 999999)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)

        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)

        tag50k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50k_company = company1.iloc[0]['name'][:35]
        tag50k_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50k_companyaddress = (tag50k_companyaddress_list[0].strip() + ',' + tag50k_companyaddress_list[1])[:35] + \
                                '\n' + tag50k_companyaddress_list[2].strip()

        tag59k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59k_company = company2.iloc[0]['name'][:35]
        tag59k_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59k_companyaddress = (tag59k_companyaddress_list[0].strip() + ',' + tag59k_companyaddress_list[1])[:35] + \
                                '\n' + tag59k_companyaddress_list[2].strip()
        tag71a = random.choice(['SHA', 'OUR', 'BEN'])

        if random.randint(0, 100) < 3:
            tag70 = 'sample text ' + random.choice(tag70_words)
        else:
            tag70 = 'sample text '

        tag57d_account_number = "%0.10d" % random.randint(0, 9999999999)
        bank57d = bank_names.sample()[:35]
        bank57d_branch = bank57d.iloc[0]['name_branch'][:35]
        bank57d_country = bank57d.iloc[0]['Country']

        TB = '{4:\n:20:' + tag20 + '\n:23B:CRED\n:32A:' + '20' + "%0.2d" % random.randint(1,
                                                                                          6) + "%0.2d" % random.randint(
            1, 29) + currency + txn_val + '\n:50K:/' + tag50k_account_number + '\n' + tag50k_company \
             + '\n' + tag50k_companyaddress + '\n:59:/' + tag59k_account_number + '\n' + tag59k_company + '\n' + \
             tag59k_companyaddress + '\n:57D:/' + tag57d_account_number + '\n' + bank57d_branch + '\n' + bank57d_country + \
             '\n' + ':70:' + tag70 + '\n:71A:' + tag71a + '\n-}'

        content = BHB + AHB + UHB + TB

        message_file = open('C:\\Users\\semih\\PycharmProjects\\swift_sim\\messages\\' + (
                "%0.12d" % random.randint(0, 999999999999)) + '-103-57d.txt', 'w')

        try:
            message_file.write(content)
            message_file.close()
        except:
            pass

    for c_code in l_52a_57a:
        if random.randint(0, 100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I103' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O1031454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        tag20 = "%0.6d" % random.randint(0, 999999)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)
        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)

        tag50k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50k_company = company1.iloc[0]['name'][:35]
        tag50k_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50k_companyaddress = (tag50k_companyaddress_list[0].strip() + ',' + tag50k_companyaddress_list[1])[:35] + \
                                '\n' + tag50k_companyaddress_list[2].strip()

        tag59k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59k_company = company2.iloc[0]['name'][:35]
        tag59k_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59k_companyaddress = (tag59k_companyaddress_list[0].strip() + ',' + tag59k_companyaddress_list[1])[:35] + \
                                '\n' + tag59k_companyaddress_list[2].strip()
        tag71a = random.choice(['SHA', 'OUR', 'BEN'])

        if random.randint(0, 100) < 3:
            tag70 = 'sample text ' + random.choice(tag70_words)
        else:
            tag70 = 'sample text '

        tag52a_bank = bank_bic.sample().iloc[0][0:4]
        tag52a_country = random.choice(country_list)

        tag57a_bank = bank_bic.sample().iloc[0][0:4]
        tag57a_country = random.choice(country_list)

        TB = '{4:\n:20:' + tag20 + '\n:23B:CRED\n:32A:' + '20' + "%0.2d" % random.randint(1,
                                                                                          6) + "%0.2d" % random.randint(
            1, 29) + currency + txn_val + '\n:50K:/' + tag50k_account_number + '\n' + tag50k_company \
             + '\n' + tag50k_companyaddress + '\n:59:/' + tag59k_account_number + '\n' + tag59k_company + '\n' + \
             tag59k_companyaddress + '\n:52A:' + tag52a_bank + tag52a_country + '2A' + '\n:57A:' + tag57a_bank + \
             tag57a_country + '22' + '\n' + ':70:' + tag70 + '\n:71A:' + tag71a + '\n-}'

        content = BHB + AHB + UHB + TB

        message_file = open('C:\\Users\\semih\\PycharmProjects\\swift_sim\\messages\\' + (
                "%0.12d" % random.randint(0, 999999999999)) + '-103-52a-57a.txt', 'w')

        try:
            message_file.write(content)
            message_file.close()
        except:
            pass

    for c_code in l_52a:
        if random.randint(0, 100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I103' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O1031454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        tag20 = "%0.6d" % random.randint(0, 999999)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)

        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)

        tag50k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50k_company = company1.iloc[0]['name'][:35]
        tag50k_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50k_companyaddress = (tag50k_companyaddress_list[0].strip() + ',' + tag50k_companyaddress_list[1])[:35] + \
                                '\n' + tag50k_companyaddress_list[2].strip()

        tag59k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59k_company = company2.iloc[0]['name'][:35]
        tag59k_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59k_companyaddress = (tag59k_companyaddress_list[0].strip() + ',' + tag59k_companyaddress_list[1])[:35] + \
                                '\n' + tag59k_companyaddress_list[2].strip()
        tag71a = random.choice(['SHA', 'OUR', 'BEN'])

        if random.randint(0, 100) < 3:
            tag70 = 'sample text ' + random.choice(tag70_words)
        else:
            tag70 = 'sample text '

        tag52a_bank = bank_bic.sample().iloc[0][0:4]
        tag52a_country = random.choice(country_list)

        TB = '{4:\n:20:' + tag20 + '\n:23B:CRED\n:32A:' + '20' + "%0.2d" % random.randint(1,
                                                                                          6) + "%0.2d" % random.randint(
            1, 29) + currency + txn_val + '\n:50K:/' + tag50k_account_number + '\n' + tag50k_company \
             + '\n' + tag50k_companyaddress + '\n:59:/' + tag59k_account_number + '\n' + tag59k_company + '\n' + \
             tag59k_companyaddress + '\n:52A:' + tag52a_bank + tag52a_country + '2A' + '\n' + ':70:' + tag70 + '\n:71A:' + tag71a + '\n-}'

        content = BHB + AHB + UHB + TB

        message_file = open('C:\\Users\\semih\\PycharmProjects\\swift_sim\\messages\\' + (
                "%0.12d" % random.randint(0, 999999999999)) + '-103-52a.txt', 'w')

        try:
            message_file.write(content)
            message_file.close()
        except:
            pass

    for c_code in l_57a:
        if random.randint(0, 100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I103' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O1031454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        tag20 = "%0.6d" % random.randint(0, 999999)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)

        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)

        tag50k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50k_company = company1.iloc[0]['name'][:35]
        tag50k_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50k_companyaddress = (tag50k_companyaddress_list[0].strip() + ',' + tag50k_companyaddress_list[1])[:35] + \
                                '\n' + tag50k_companyaddress_list[2].strip()

        tag59k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59k_company = company2.iloc[0]['name'][:35]
        tag59k_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59k_companyaddress = (tag59k_companyaddress_list[0].strip() + ',' + tag59k_companyaddress_list[1])[:35] + \
                                '\n' + tag59k_companyaddress_list[2].strip()
        tag71a = random.choice(['SHA', 'OUR', 'BEN'])

        if random.randint(0, 100) < 3:
            tag70 = 'sample text ' + random.choice(tag70_words)
        else:
            tag70 = 'sample text '

        tag57a_bank = bank_bic.sample().iloc[0][0:4]
        tag57a_country = random.choice(country_list)

        TB = '{4:\n:20:' + tag20 + '\n:23B:CRED\n:32A:' + '20' + "%0.2d" % random.randint(1,
                                                                                          6) + "%0.2d" % random.randint(
            1, 29) + currency + txn_val + '\n:50K:/' + tag50k_account_number + '\n' + tag50k_company \
             + '\n' + tag50k_companyaddress + '\n:59:/' + tag59k_account_number + '\n' + tag59k_company + '\n' + \
             tag59k_companyaddress + '\n:57A:' + tag57a_bank + tag57a_country + '22' + '\n:70:' + tag70 + '\n:71A:' + tag71a + '\n-}'

        content = BHB + AHB + UHB + TB

        message_file = open('C:\\Users\\semih\\PycharmProjects\\swift_sim\\messages\\' + (
                "%0.12d" % random.randint(0, 999999999999)) + '-103-57a.txt', 'w')

        try:
            message_file.write(content)
            message_file.close()
        except:
            pass

    for c_code in l_basic:
        if random.randint(0, 100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I103' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O1031454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{103:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        tag20 = "%0.6d" % random.randint(0, 999999)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)

        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)

        tag50k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50k_company = company1.iloc[0]['name'][:35]
        tag50k_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50k_companyaddress = (tag50k_companyaddress_list[0].strip() + ',' + tag50k_companyaddress_list[1])[:35] + \
                                '\n' + tag50k_companyaddress_list[2].strip()

        tag59k_account_number = "%0.10d" % random.randint(0, 9999999999)
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59k_company = company2.iloc[0]['name'][:35]
        tag59k_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59k_companyaddress = (tag59k_companyaddress_list[0].strip() + ',' + tag59k_companyaddress_list[1])[:35] + \
                                '\n' + tag59k_companyaddress_list[2].strip()
        tag71a = random.choice(['SHA', 'OUR', 'BEN'])

        if random.randint(0, 100) < 3:
            tag70 = 'sample text ' + random.choice(tag70_words)
        else:
            tag70 = 'sample text '

        TB = '{4:\n:20:' + tag20 + '\n:23B:CRED\n:32A:' + '20' + "%0.2d" % random.randint(1,
                                                                                          6) + "%0.2d" % random.randint(
            1, 29) + currency + txn_val + '\n:50K:/' + tag50k_account_number + '\n' + tag50k_company \
             + '\n' + tag50k_companyaddress + '\n:59:/' + tag59k_account_number + '\n' + tag59k_company + '\n' + \
             tag59k_companyaddress + '\n' + ':70:' + tag70 + '\n:71A:' + tag71a + '\n-}'

        content = BHB + AHB + UHB + TB

        message_file = open('C:\\Users\\semih\\PycharmProjects\\swift_sim\\messages\\' + (
                "%0.12d" % random.randint(0, 999999999999)) + '-103.txt', 'w')

        try:
            message_file.write(content)
            message_file.close()
        except:
            pass