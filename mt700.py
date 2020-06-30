import random
import uuid


def mt700(bank_bic, company_d, company_names, country_list, val_weights, l_currency, w_currencies, out_path, date_list):
    for c_code in country_list:
        if random.randint(0,100) > 50:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'BJAXXX0000000000}'
            AHB = '{2:I700' + bank2 + country2 + '2LXXXXN}'
            UHB = '{3:{700:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'
        else:
            bank1 = 'AAAA'
            bank2 = bank_bic.sample().iloc[0][0:4]
            country1 = random.choices(['GB', 'DE', 'RU', 'AE', 'US', ], weights=[85, 3, 5, 2, 5], k=1)[0]
            country2 = c_code
            BHB = '{1:F01' + bank1 + country1 + 'B0AXXX0377002089}'
            AHB = '{2:O7001454110804' + bank2 + country2 + 'XXXXX100009037121108041654N}'
            UHB = '{3:{700:TGT}{108:OPTUSERREF16CHAR}{121:' + str(uuid.uuid1()) + '}}'

        val_date = random.choice(date_list)
        tag20 = "%0.6d" % random.randint(0, 999999)
        # tag27 = '1/1'
        tag40a = 'IRREVOCABLE'
        tag44c = random.choice(date_list)


    
        if (random.randint(0, 100) < 15) and (c_code in l_currency.values):
            currency = l_currency.loc[l_currency['co_code'] == c_code]['cur_code'].values[0]
        else:
            currency = random.choice(w_currencies)
        txn_val = str(round(random.choice(val_weights) * random.random())) + ',' + "%0.2d" % random.randint(1, 99)
    
        company1 = company_names.sample(weights=company_d['current employee estimate'])
        tag50_company = company1.iloc[0]['name'][:35]
        tag50_companyaddress_list = company1.iloc[0]['locality'].split(',')
        tag50_companyaddress = tag50_companyaddress_list[0].strip()[:35] + '\n' + tag50_companyaddress_list[1].strip()[:35] + \
                                '\n' + tag50_companyaddress_list[2].strip()[:35]
    
        company2 = company_names.sample(weights=company_d['current employee estimate'])
        tag59_company = company2.iloc[0]['name'][:35]
        tag59_companyaddress_list = company2.iloc[0]['locality'].split(',')
        tag59_companyaddress = tag59_companyaddress_list[0].strip()[:35] + '\n' + tag59_companyaddress_list[1].strip()[:35] + \
                                '\n' + tag59_companyaddress_list[2].strip()
        tag31d=tag50_companyaddress_list[0].strip()[:35]
        tag44f = tag59_companyaddress_list[0].strip()[:35]
        tag41a_bank = bank_bic.sample().iloc[0][0:4]
        tag41a_country = random.choice(country_list)
    
        # tag57a_bank = tag41a_bank
        # tag57a_country = tag41a_country
    
        TB = '{4:\n' + ':27:1/1\n:40A:' + tag40a + '\n:20:' + tag20 + '\n' + ':31C:' + val_date + \
             '\n' + ':40E:UCP LATEST VERSION\n:31D:' + val_date + tag31d + '\n:50:' + tag50_company + '\n' + \
             tag50_companyaddress + '\n' + ':59:' + tag59_company + '\n' + tag59_companyaddress + '\n' + ':32B:' + currency + \
             txn_val + '\n' + ':41A:' + tag41a_bank +  tag41a_country + '2A\n' + 'BY PAYMENT\n' + ':43P:NOT ALLOWED' '\n' + \
             ':43T:ALLOWED\n' + ':44E:' + tag31d + '\n' + ':44F:' + tag44f + '\n' + ':44C:' + tag44c + '\n' +\
             ':45A:+400,000 BOTTLES OF BEER' + '\n' + 'PACKED 12 TO AN EXPORT CARTON' + '\n' + '+FCA AMSTERDAM' '\n' + \
             ':46A: +SIGNED COMMERCIAL INVOICE IN DUPLICATE' + '\n' + '+PACKINGL LIST IN DUPLICATE' + '\n' + \
             '+FORWARDING AGENTS CERTIFICATE OF RECEIPT, SHOWING GOODS ADDRESSED TO APPLICANT' + '\n' + \
             ':71D:ALL BANKING CHARGES OUTSIDE ISSUING' + '\n' + 'BANK ARE FOR THE BENEFICIARY' + '\n' + \
             ':48:6/FORWARDING AGENTS CERT OF RECEIPT' + '\n' + ':49:CONFIRM' + '\n' + \
             ':58A:' + tag41a_bank + tag41a_country + '2A\n' + \
             ':57A:' + tag41a_bank + tag41a_country + '2A\n' + '-}'
    
        content = BHB + AHB + UHB + TB
    
        message_file = open(out_path + (
                "%0.12d" % random.randint(0, 999999999999)) + '-700.txt', 'w')
    
        try:
            message_file.write(content)
            message_file.close()
        except:
            pass
