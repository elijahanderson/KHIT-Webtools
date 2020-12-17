import pandas as pd

def modify_cash_receipt(file):
    df = pd.read_csv(file)
    df = df[['payor_name', 'check_no', 'check_date', 'deposit_number']]
    df['check_date'] = pd.to_datetime(df.check_date)
    df.sort_values(by=['check_date'], inplace=True)
    df.to_csv('/client/client/' + file, index=False)
    
