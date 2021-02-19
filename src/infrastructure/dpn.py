import pandas as pd


def modify_dpn(file):
    if file.split('.')[-1] == 'csv':
        o_df = pd.read_csv(file)
        output = modify(o_df)
        return output
    else:
        o_df = pd.read_excel(file)
        output = modify(o_df)
        return output


def modify(df):
    event_categories = pd.read_csv('csv/dpn_categories.csv')
    event_categories['event'] = event_categories['event'].apply(
        lambda v: str(v).lower().replace('-', '').replace('/', '').replace(' ', '').strip()
    )
    df['event_name'] = df['event_name'].apply(
        lambda v: str(v).lower().replace('-', '').replace('/', '').replace(' ', '').strip()
    )
    output_dict = {}
    for client, frame in df.groupby(['full_name']):
        output_dict[client] = {'id_no': frame['id_no'].iloc[0]}
        for idx, row in frame.iterrows():
            if row['event_name'] in event_categories['event'].unique():
                category = event_categories.iloc[
                    event_categories.event[event_categories.event == row['event_name']].index
                ]['category'].iloc[0].strip()
                if category in output_dict[client].keys():
                    output_dict[client][category] = output_dict[client][category] + 1
                else:
                    output_dict[client][category] = 1
    return output_dict

