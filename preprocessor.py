import pandas as pd


def preprocess(df, region_df):
    # Keep only Summer Olympics data
    df = df[df['Season'] == 'Summer']

    # Merge with region (country) data
    df = df.merge(region_df, on='NOC', how='left')

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # One-hot encode the Medal column (Gold / Silver / Bronze)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    # Remove any duplicate columns created during concat
    df = df.loc[:, ~df.columns.duplicated()]

    return df