import datetime

def display_bank_info(page):
    info = str()
    if page == 1:
        info = """BDO SAVINGS ACCOUNT INFORMATION \n 
Minimum Initial Deposit: Php 2,000.00 
Minimum MADB Requirement: Php 2,000.00
Minimum Balance To Earn Interest: Php 5,000.00 
Gross Interest Rate Per Annum: 0.0625%\n
BDO TIME DEPOSIT INFORMATION
Minimum Initial Placement: Php 1,000.00 
Terms of Placement: 30, 180, 360 Days"""
    elif page == 2:
        info = """LANDBANK SAVINGS ACCOUNT INFORMATION \n 
Minimum Initial Deposit: Php 5,000.00 
Minimum MADB Requirement: Php 500.00
Gross Interest Rate Per Annum: 0.05%\n
LANDBANK TIME DEPOSIT INFORMATION
Minimum Initial Placement: Php 1,000.00 
Terms of Placement: 30, 180, 360 Days \n"""
    elif page == 3:
        info = """PNB SAVINGS ACCOUNT INFORMATION \n 
Minimum Initial Deposit: Php 3,000.00 
Minimum MADB Requirement: Php 10,000.00
Minimum Balance To Earn Interest: Php 10,000.00 
Gross Interest Rate Per Annum: 0.1%\n
PNB TIME DEPOSIT INFORMATION
Minimum Initial Placement: Php 1,000.00 
Terms of Placement: 30, 180, 360 Days \n"""
    
    return info

def simple_interest(deposit_value, interest, time, time_unit="", bank="", comparison=False):
    current_time = datetime.date.today()
    result = str()
    if time_unit == "years":
        for i in range(1, time+1):
            simple_interest = (deposit_value*i*interest)
            tax = simple_interest * 0.2
            maturity_value = deposit_value + (simple_interest-tax)
            result += f"{current_time+datetime.timedelta(days=i*365)} | Interest: {simple_interest:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            
        result = f"{bank} SAVINGS ACCOUNT INTEREST PROJECTION (PER YEAR) \n" + result
        
    elif time_unit == "months":
        for i in range(1, time+1):
            simple_interest = (deposit_value*(i/12)*interest)
            tax = simple_interest * 0.2
            maturity_value = deposit_value + (simple_interest-tax)
            result += f"{current_time+datetime.timedelta(days=i*30)} | Interest: {simple_interest:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            
        result = f"{bank} SAVINGS ACCOUNT INTEREST PROJECTION (PER MONTH) \n" + result
    
    if comparison == True:
        return maturity_value
    else:
        return result

def bdo_time_deposit(deposit_value, term, comparison=False):
    current_time = datetime.date.today()
    interest = float()
    result = str()
    match(term):
        case 30:
            if deposit_value >= 1000 and deposit_value < 1000000:
                interest = 0.00125
            elif deposit_value >= 1000000:
                interest = 0.0025
            time_deposit = (deposit_value*(term/360)*interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit-tax)
            result = f"{current_time+datetime.timedelta(days=30)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"BDO TIME DEPOSIT ACCOUNT INTEREST (30 DAYS) \n" + result

        case 180:
            if deposit_value >= 1000 and deposit_value < 100000:
                interest = 0.00125
            elif deposit_value >= 100000 and deposit_value < 1000000:
                interest = 0.0025
            elif deposit_value >= 1000000 and deposit_value < 5000000:
                interest = 0.00375
            elif deposit_value >= 5000000:
                interest = 0.005
            time_deposit = (deposit_value*(term/360)*interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit-tax)
            result = f"{current_time+datetime.timedelta(days=180)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"BDO TIME DEPOSIT ACCOUNT INTEREST (180 DAYS) \n" + result
        
        case 360:
            if deposit_value >= 1000 and deposit_value < 100000:
                interest = 0.00125
            elif deposit_value >= 100000 and deposit_value < 1000000:
                interest = 0.0025
            elif deposit_value >= 1000000 and deposit_value < 5000000:
                interest = 0.00375
            elif deposit_value >= 5000000:
                interest = 0.005
            time_deposit = (deposit_value*(term/360)*interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit-tax)
            result = f"{current_time+datetime.timedelta(days=360)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"BDO TIME DEPOSIT ACCOUNT INTEREST (360 DAYS) \n" + result

    if comparison == True:
        return maturity_value
    else:
        return result

def landbank_time_deposit(deposit_value, term, comparison=False):
    current_time = datetime.date.today()
    interest = float()
    result = str()
    match(term):
        case 30:
            if deposit_value >= 1000 and deposit_value < 50000:
                interest = 0.00125
            elif deposit_value >= 50000 and deposit_value < 300000:
                interest = 0.00215
            elif deposit_value >= 300000 and deposit_value < 500000:
                interest = 0.0031
            elif deposit_value >= 500000 and deposit_value < 1000000:
                interest = 0.00405
            elif deposit_value >= 1000000:
                interest = 0.005
            time_deposit = (deposit_value*(term/360)*interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit-tax)
            result = f"{current_time+datetime.timedelta(days=30)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"LANDBANK TIME DEPOSIT ACCOUNT INTEREST (30 DAYS) \n" + result

        case 180:
            if deposit_value >= 1000 and deposit_value < 50000:
                interest = 0.00275
            elif deposit_value >= 50000 and deposit_value < 300000:
                interest = 0.00435
            elif deposit_value >= 300000 and deposit_value < 500000:
                interest = 0.005
            elif deposit_value >= 500000 and deposit_value < 1000000:
                interest = 0.0056
            elif deposit_value >= 1000000:
                interest = 0.0065
            time_deposit = (deposit_value * (term / 360) * interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit - tax)
            result = f"{current_time + datetime.timedelta(days=180)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"LANDBANK TIME DEPOSIT ACCOUNT INTEREST (180 DAYS) \n" + result
        
        case 360:
            if deposit_value >= 1000 and deposit_value < 50000:
                interest = 0.0035
            elif deposit_value >= 50000 and deposit_value < 300000:
                interest = 0.0056
            elif deposit_value >= 300000 and deposit_value < 500000:
                interest = 0.00625
            elif deposit_value >= 500000 and deposit_value < 1000000:
                interest = 0.00685
            elif deposit_value >= 1000000:
                interest = 0.0075
            time_deposit = (deposit_value * (term / 360) * interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit - tax)
            result = f"{current_time + datetime.timedelta(days=360)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"LANDBANK TIME DEPOSIT ACCOUNT INTEREST (360 DAYS) \n" + result

    if comparison == True:
        return maturity_value
    else:
        return result

def pnb_time_deposit(deposit_value, term, comparison=False):
    current_time = datetime.date.today()
    interest = float()
    result = str()
    match(term):
        case 30:
            if deposit_value >= 10000 and deposit_value < 250000:
                interest = 0.00125
            elif deposit_value >= 250000 and deposit_value < 1000000:
                interest = 0.0025
            elif deposit_value >= 1000000:
                interest = 0.00375
            time_deposit = (deposit_value*(term/360)*interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit-tax)
            result = f"{current_time+datetime.timedelta(days=30)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"PNB TIME DEPOSIT ACCOUNT INTEREST (30 DAYS) \n" + result

        case 180:
            if deposit_value >= 10000 and deposit_value < 250000:
                interest = 0.00125
            elif deposit_value >= 250000 and deposit_value < 1000000:
                interest = 0.0025
            elif deposit_value >= 1000000:
                interest = 0.00375
            time_deposit = (deposit_value * (term / 360) * interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit - tax)
            result = f"{current_time + datetime.timedelta(days=180)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"PNB TIME DEPOSIT ACCOUNT INTEREST (180 DAYS) \n" + result

        case 360:
            if deposit_value >= 10000 and deposit_value < 250000:
                interest = 0.00125
            elif deposit_value >= 250000 and deposit_value < 1000000:
                interest = 0.0025
            elif deposit_value >= 1000000:
                interest = 0.00375
            time_deposit = (deposit_value * (term / 360) * interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit - tax)
            result = f"{current_time + datetime.timedelta(days=360)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"PNB TIME DEPOSIT ACCOUNT INTEREST (360 DAYS) \n" + result

    if comparison == True:
        return maturity_value
    else:
        return result
    
def custom_time_deposit(deposit_value, interest, term, comparison=False):
    current_time = datetime.date.today()
    result = str()
    match(term):
        case 30:
            time_deposit = (deposit_value*(term/360)*interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit-tax)
            result = f"{current_time+datetime.timedelta(days=30)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"CUSTOM TIME DEPOSIT ACCOUNT INTEREST (30 DAYS) \n" + result

        case 180:
            time_deposit = (deposit_value * (term / 360) * interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit - tax)
            result = f"{current_time + datetime.timedelta(days=180)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"CUSTOM TIME DEPOSIT ACCOUNT INTEREST (180 DAYS) \n" + result

        case 360:
            time_deposit = (deposit_value * (term / 360) * interest)
            tax = time_deposit * 0.2
            maturity_value = deposit_value + (time_deposit - tax)
            result = f"{current_time + datetime.timedelta(days=360)} | Interest: {time_deposit:.2f} | Tax: 20% | Maturity Value: {maturity_value:.2f} \n"
            result = f"CUSTOM TIME DEPOSIT ACCOUNT INTEREST (360 DAYS) \n" + result

    if comparison == True:
        return maturity_value
    else:
        return result