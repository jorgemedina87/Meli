import pandas as pd

class ShippingTransformer:

    def transform(self, df):
        shipping_normalized = pd.json_normalize(df['shipping'])
        shipping_normalized['local_pick_up'] = shipping_normalized['local_pick_up'].astype(int)
        shipping_normalized.rename(columns={'local_pick_up': 'shipping_local_pick_up'}, inplace=True)
        shipping_normalized['shipping_mode_me2'] = shipping_normalized['mode'].apply(lambda x: 1 if x == 'me2' else 0)

        df['shipping_local_pick_up'] = shipping_normalized['shipping_local_pick_up']
        df['shipping_mode_me2'] = shipping_normalized['shipping_mode_me2']
        
        return df
