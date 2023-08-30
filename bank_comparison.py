from interest import *

def compare_simple_banks(deposit_value, interest, time, time_unit="", custom = False):
    result = str()
    if time_unit == "years":
        maturity1 = simple_interest(deposit_value, 0.000625, time, time_unit="years", comparison=True)
        maturity2 = simple_interest(deposit_value, 0.001, time, time_unit="years", comparison=True)
        maturity3 = simple_interest(deposit_value, 0.0005, time, time_unit="years", comparison=True)
    
    elif time_unit == "months":
        maturity1 = simple_interest(deposit_value, 0.000625, time, time_unit="months", comparison=True)
        maturity2 = simple_interest(deposit_value, 0.001, time, time_unit="months", comparison=True)
        maturity3 = simple_interest(deposit_value, 0.0005, time, time_unit="months", comparison=True)

    if custom == True:
        if time_unit == "years":
            maturity4 = simple_interest(deposit_value, interest, time, time_unit="years", comparison=True)
        elif time_unit == "months":
            maturity4 = simple_interest(deposit_value, interest, time, time_unit="months", comparison=True)

        result += f"Maturity value for Custom Bank account: {maturity4}\n"
        result += f"Maturity value for BDO account: {maturity1}\n"
        result += f"Maturity value for PNB account: {maturity2}\n"
        result += f"Maturity value for Landbank account: {maturity3}\n"

        if maturity1 > maturity2 and maturity1 > maturity3 and maturity1 > maturity4:
            result += f"The BDO account has the highest maturity value.\n"
        elif maturity2 > maturity1 and maturity2 > maturity3 and maturity2 > maturity4:
            result += f"The PNB account has the highest maturity value.\n"
        elif maturity3 > maturity1 and maturity3 > maturity2 and maturity3 > maturity4:
            result += f"The Landbank account has the highest maturity value.\n"
        elif maturity4 > maturity1 and maturity4 > maturity2 and maturity4 > maturity3:
            result += f"The Custom Bank account has the highest maturity value.\n"
        else:
            result += f"Two or more accounts have the same maturity value."

    else:
        result += f"Maturity value for BDO account: {maturity1}\n"
        result += f"Maturity value for PNB account: {maturity2}\n"
        result += f"Maturity value for Landbank account: {maturity3}\n"
        if maturity1 > maturity2 and maturity1 > maturity3:
            result += f"The BDO account has the highest maturity value.\n"
        elif maturity2 > maturity1 and maturity2 > maturity3:
            result += f"The PNB account has the highest maturity value.\n"
        elif maturity3 > maturity1 and maturity3 > maturity2:
            result += f"The Landbank account has the highest maturity value.\n"
        else:
            result += "Two or more accounts have the same maturity value.\n"

    return result

def compare_timedep_banks(deposit_value, term):
    result = str()
    maturity1 = bdo_time_deposit(deposit_value, term, comparison=True)
    maturity2 = pnb_time_deposit(deposit_value, term, comparison=True)
    maturity3 = landbank_time_deposit(deposit_value, term, comparison=True)

    result += f"Maturity value for BDO account: {maturity1:.2f}\n"
    result += f"Maturity value for PNB account: {maturity2:.2f}\n"
    result += f"Maturity value for Landbank account: {maturity3:.2f}\n"

    if maturity1 > maturity2 and maturity1 > maturity3:
        result += "The BDO account has the highest maturity value.\n"
    elif maturity2 > maturity1 and maturity2 > maturity3:
        result += "The PNB account has the highest maturity value.\n"
    elif maturity3 > maturity1 and maturity3 > maturity2:
        result += "The Landbank account has the highest maturity value.\n"
    else:
        result += "Two or more accounts have the same maturity value.\n"
        
    return result

def compare_timedep_banks_custom(deposit_value, interest, term):
    result = str()

    maturity1 = bdo_time_deposit(deposit_value, term, comparison=True)
    maturity2 = pnb_time_deposit(deposit_value, term, comparison=True)
    maturity3 = landbank_time_deposit(deposit_value, term, comparison=True)
    maturity4 = custom_time_deposit(deposit_value, interest, term, comparison=True)

    result += f"Maturity value for Custom Bank account: {maturity4:.2f}\n"
    result += f"Maturity value for BDO account: {maturity1:.2f}\n"
    result += f"Maturity value for PNB account: {maturity2:.2f}\n"
    result += f"Maturity value for Landbank account: {maturity3:.2f}\n"

    if maturity1 > maturity2 and maturity1 > maturity3 and maturity1 > maturity4:
        result += "The BDO account has the highest maturity value."
    elif maturity2 > maturity1 and maturity2 > maturity3 and maturity2 > maturity4:
        result += "The PNB account has the highest maturity value."
    elif maturity3 > maturity1 and maturity3 > maturity2 and maturity3 > maturity4:
        result += "The Landbank account has the highest maturity value."
    elif maturity4 > maturity1 and maturity4 > maturity2 and maturity4 > maturity3:
        result += "The Custom Bank account has the highest maturity value."
    else:
        result += "Two or more accounts have the same maturity value."

    return result