import pandas as pd


def modify_cash_receipt(file):
    if file.split('.')[-1] == 'csv':
        o_df = pd.read_csv(file)
        m_df = modify(o_df)
        m_df.to_csv('/client/client/' + file, index=False)
    else:
        o_df = pd.read_excel(file)
        m_df = modify(o_df)
        m_df.to_excel('/client/client/' + file, index=False)


def modify(df):
    df = df[['check_date', 'check_no', 'deposit_number', 'payor_name', 'check_amount']]
    df['check_date'] = pd.to_datetime(df.check_date)
    df.sort_values(by=['check_date'], inplace=True)
    df['check_date'] = df['check_date'].dt.strftime('%m/%d/%Y')
    amount_sum = '${:,.2f}'.format(df['check_amount'].sum())
    df['check_amount'] = df['check_amount'].apply(lambda amt: f'${amt:,.2f}')
    df = df.append(pd.Series(), ignore_index=True)
    df = df.append(pd.Series(), ignore_index=True)
    df = df.append({
            'check_date': None,
            'check_no': None,
            'deposit_number': None,
            'payor_name': None,
            'check_amount': amount_sum,
        }, ignore_index=True)
    return df

