import pandas as pd

class TagsTransformer:

    def transform(self, df):
        expanded_tags = df['tags'].apply(pd.Series).add_suffix('_tags')
        df['tags_dragged_bids_and_visits'] = 0
        df.loc[expanded_tags['0_tags'] == 'dragged_bids_and_visits', 'tags_dragged_bids_and_visits'] = 1
        return df


