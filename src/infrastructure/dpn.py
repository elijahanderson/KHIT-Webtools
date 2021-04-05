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
    df = df[df['event_name'] == df['service']]
    df['event_name'] = df['event_name'].apply(
        lambda v: str(v).lower().replace('-', '').replace('/', '').replace(' ', '').strip()
    )
    output_dict = {}
    for key, frame in df.groupby(['full_name', 'program_name']):
        dict_key = key[0] + '/' + key[1]
        output_dict[dict_key] = {'id_no': str(frame['id_no'].iloc[0])}
        for idx, row in frame.iterrows():
            if row['event_name'] in event_categories['event'].unique() and row['is_noshow'] == False:
                category = event_categories.iloc[
                    event_categories.event[event_categories.event == row['event_name']].index
                ]['category'].iloc[0].strip()
                if category in output_dict[dict_key].keys():
                    output_dict[dict_key][category] = str(int(output_dict[dict_key][category]) + 1)
                else:
                    output_dict[dict_key][category] = str(1)
    return output_dict

