import pandas as pd
import re

class WarrantyTransformer:
    def __init__(self):
        # Expresiones regulares generales
        self.patterns = [
            r"garant[íi]?z?ado",
            r"\b\d+\s*(d[ií]as?|horas?|semanas?|meses?|a[nñ]os?)\b",
            r"(cambio|devoluci[óo]n|probar|prueba|oficial|escrita|f[aá]brica|fabricante|relojero|apple|vida)",
            r"100\s?%\s?garantizado",
            r"por falla (del )?\w+",
            r"s[íi]",
        ]
    
    def transform(self, value):
        value_str = str(value).lower()
        
        # Chequeo explícito para "Sin garantía"
        if "sin garantía" in value_str or pd.isna(value) or value is None:
            return 0

        # Si alguno de los patrones se encuentra en el valor, retorna "Si"
        if any(re.search(pattern, value_str) for pattern in self.patterns):
            return 1
        
        # Si no coincide con ningún patrón, retorna "No"
        return 0

