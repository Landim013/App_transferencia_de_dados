from sqlite3 import Cursor
import pandas as pd
import mysql.connector
from mysql.connector import Error

Sheetl_df = pd.read_excel("Elemento_de_rede.xlsx") #conectando a planilha

for i, dados in enumerate(Sheetl_df['IP']):  #colunas e valores da planilha
    ip = Sheetl_df.loc[i,"IP"]
    nome = Sheetl_df.loc[i,"Nome"]
    modelo = Sheetl_df.loc[i,"Modelo"]    
    

    conectar = mysql.connector.connect(host = 'localhost', database ='mysql', user='root' ,password='')
    inserir = """INSERT INTO ping_danilo(IP,NOME,MODELO,VEZES_OFF,situacao)
    VALUES ('{}', '{}', '{}', 0,0) """. format(ip, nome, modelo)

    
    print(inserir)

    try:
        cursor= conectar.cursor()

        cursor.execute(inserir)
        conectar.commit()
        
        
    except:
        continue
cursor.close()    