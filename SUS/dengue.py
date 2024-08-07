# %%
import pandas as pd
import numpy as np
import csv

# %%

df = pd.read_csv('sinan_dengue_sample_2024.csv',low_memory=False,quoting= csv.QUOTE_NONE, encoding='utf-8')

df.columns = df.columns.str.strip('"')

# Remover aspas dos valores nas células
df = df.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)

# Mostrar as primeiras linhas do DataFrame limpo
print('Total de colunas :',len(df.columns))
print('Todas as colunas :',df.columns.tolist())
print(df.shape)
# %%

# Função para determinar se os valores são string ou int
def determine_type(x):
    if pd.api.types.is_integer_dtype(x):
        return 'int'
    elif pd.api.types.is_float_dtype(x):
        return 'float'
    elif pd.api.types.is_string_dtype(x):
        return 'string'
    else:
        return 'other'

# Aplicar a função a cada coluna
column_types = df.apply(lambda col: determine_type(col))

# Mostrar os tipos de cada coluna
print(column_types)

# %%

print(df['CS_SEXO'].value_counts())
print(df['CS_RACA'].value_counts())
print(df['DT_OBITO'].value_counts())
# %% 
print(df['DT_OBITO'].dtypes)
print("Não tiveram data de óbito (SUPONDO DE NÃO TEVE ÓBITO) :",df['DT_OBITO'].isna().sum())
print("Total de registros : ",len(df['DT_OBITO']))
print("Total de registros com DATA DE ÓBITO : ",  len(df['DT_OBITO']) - df['DT_OBITO'].isna().sum())
# %%

pd.set_option('display.max_columns', None)  # Mostra todas as colunas
df.head(7)