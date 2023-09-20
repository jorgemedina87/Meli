import pandas as pd

class PaymentMethodsTransformer:

    def transform(self, df):
        max_length = df['non_mercado_pago_payment_methods'].apply(len).max()
        expanded_df = pd.DataFrame(df['non_mercado_pago_payment_methods'].tolist())
        count_not_none = expanded_df.notnull().sum(axis=1)
        df['non_mercado_pago_payment_methods_count'] = self._map_counts(count_not_none)
        return df

    def _map_counts(self, count_series):
        mapping = {
            0: 0,
            1: 1,
            2: 2,
            3: 3
        }
        return count_series.replace(mapping).where(count_series <= 3, 4)



