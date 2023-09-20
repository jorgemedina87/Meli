import pandas as pd
import re

class SellerAddressTransformer:

    def transform(self, df):
        # Calculo de la columna 'seller_address_stateid'
        seller_address_normalized = pd.json_normalize(df['seller_address'])
        seller_address_normalized['state.id'] = self._map_state_id(seller_address_normalized['state.id'])
        seller_address_normalized.rename(columns={'state.id': 'seller_address_stateid'}, inplace=True)
        
        return seller_address_normalized

    def _map_state_id(self, state_id_column):
        return state_id_column.apply(lambda x: 'AR-C' if x == 'AR-C' else ('AR-B' if x == 'AR-B' else 'OTHER'))
