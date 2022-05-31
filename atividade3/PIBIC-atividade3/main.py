#criando ferramentas (estão mais para gambiarras, mas tudo bem)
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

class tratar_dados_faltantes:

    def __init__(self):
        pass
    
    def conferir_faltantes(self, coluna, identidade_nulo):
        dados = coluna
        valores_nulos = []
        x = 0
        for i in dados:
            if dados[x] == identidade_nulo:
                return True
            x = x + 1
        return False
    
    def conferir_dados(self, coluna):
        try:
            x = 0
            for i in coluna:
                coluna[x] = int(coluna[x])
                x = x + 1
            valor_max = f"O valor máximo encontrado foi: {coluna.max()}"
            valor_min = f"O valor mínimo encontrado foi: {coluna.min()}"
            valor_med = f"A média entre os valores é: {coluna.mean()}"
            desvio_padrao = f"O desvio padrão é: {coluna.std()}"
            variancia = f"A variância é: {coluna.var()}"
            desvio_absoluto = f"O desvio absoluto é: {coluna.mad()}"
            mediana = f"A mediana é igual a {coluna.median()}"
            valores = [valor_max, valor_min, valor_med, desvio_padrao, variancia, desvio_absoluto, mediana]
            return valores
        
        except ValueError:
            print('Ops, algum erro ocorreu!')
        
    
    def tratar_faltantes(self, coluna, identidade_nulo):
        dados = coluna
        valores_normais = []
        x = 0
        for i in dados:
            if dados[x] != identidade_nulo:
                valores_normais.append(dados[x])
            x = x + 1

        valores_normais = np.array(valores_normais).astype(np.float)

        x = 0

        for i in dados:
            if dados[x] == identidade_nulo:
                dados[x] = int(valores_normais.mean())
            x = x + 1

            
    def checar_dataset(self, dataset, identidade_nulo):
        df = dataset
        ccdf = [] #ccdf = colunas com dados faltantes
        for i in df:
            is_null = tratar_dados_faltantes.conferir_faltantes(df[i], identidade_nulo)
            ccdf.append(is_null)
        return ccdf
    
    def tratar_dataset(self, dataset, identidade_nulo):
        df = dataset.copy()
        for i in df:
            if tratar_dados_faltantes.conferir_faltantes(df[i], identidade_nulo) == True:
                tratar_dados_faltantes.tratar_faltantes(df[i], identidade_nulo)
        return df
                
                
    def mostrar_dados(self, coluna):
        try:
            x = 0
            for i in coluna:
                coluna[x] = int(coluna[x])
                x = x + 1
            valor_max = ["valor máximo encontrado", coluna.max()]
            valor_min = ["valor mínimo encontrado", coluna.min()]
            valor_med = ["média entre valores", coluna.mean()]
            desvio_padrao = ["desvio padrão", coluna.std()]
            variancia = ["A variância é:", coluna.var()]
            desvio_absoluto = ["Desvio absoluto", coluna.mad()]
            mediana = ["Mediana", coluna.median()]
            valores = [valor_max, valor_min, valor_med, desvio_padrao, variancia, desvio_absoluto, mediana]
            valores = pd.DataFrame(valores)
            return valores
        except ValueError:
            print('Ops, algum erro ocorreu!')
            
    def listar_novos_dados(self, dados):
        try:
            data = []
            for coluna in df:
                data.append(tratar_dados_faltantes.mostrar_dados(df[coluna]))
            x = 0
            for i in data:
                print('='*50)
                print('Coluna {}'.format(x+1))
                print('='*50)
                print(data[x])
                x = x + 1
        except ValueError:
            print('Ops, algum erro ocorreu!')
            print('Você deve ter inserido os dados errados...')
            print('Tente:')
            print('(1) tratar os dados com a função "tratar_dataset"')
            print('(2) procurar colunas faltantes com a função "checar_dataset"')
            print('\n')
            
            
            
class tratar_dados_geral():
    
    def __init__(self):
        pass
    
    def set_novo_dataframe(self, old_df, new_df):
        try:
            df = new_df
        except ValueError:
            print("Ops, ocorreu um erro")
            print("""
            Sintaxe:
            tratar_dados_geral.set_novo_dataframe(dataframe_antigo, dataframe_novo)
            
            """)
    
    def one_hot_encoding(self, df):
        lenc = LabelEncoder()
        ohn = OneHotEncoder()
        copy_df = df.copy()
        for column in copy_df.columns:
            new_df = lenc.fit_transform(copy_df[column])
            ohn.fit(new_df.reshape(-1,1))
            t_new_df = ohn.transform(new_df.reshape(-1,1))
            t_new_df = t_new_df.toarray()
            copy_df[column] = t_new_df
        return copy_df
            
            
    def label_encoding(self, df):
        copy_df = df.copy()
        for column in copy_df:
            copy_df[column] = LabelEncoder().fit_transform(copy_df[column])
        return copy_df
            
    
    def reduzir_valor_dos_dados(self, data_frame):
        colunas__ = []
        for coluna in df:
            dataset = df[coluna]
            for item in dataset:
                if float(item) > 100:
                    if coluna not in colunas__:
                        colunas__.append(coluna)
        valores_f = []
        for coluna__ in colunas__:
            dataset = df[coluna__]
            z = 0
            for i in dataset:
                dataset[z] = int(dataset[z])
                z = z + 1
            media = df[coluna__].mean()
            desvio_padrao = df[coluna__].std()
            novos_valores = []
            for valor in dataset:
                novo_valor = (valor - media)/desvio_padrao
                novos_valores.append(novo_valor)
            valores_f.append(novos_valores)
        return valores_f
    
    def reduzir_numero_de_dados(self, coluna):
        pass  