import pandas as pd
import mysql.connector
from mysql.connector import Error

con = mysql.connector.connect(host='127.0.0.1', database='clientes2', 
                              user='root', password='')

try:
    if con.is_connected():
        db_info = con.get_server_info()
        print('Conectado ao servidor MySQL versão ', db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)

        tabela = pd.read_excel('BDS.xlsx')
       
            
            
           
              #print(f"{i} - SLA: {sla} - IP: {ip}")
           
    buscar = """SELECT `id_programa`, `id_vantive`, `cliente`, `ip`, `situacao`, `tipo_cliente`, `sla`, `vezes_off`, `grupo`, `vip`, `ponta`, `id_associado` FROM `pings` WHERE 1 """
    cursor= con.cursor()

    cursor.execute(buscar)
    
    id_v = []
    nome = []
    ip = []
    sla = []
    grupo = []
    linhas = cursor.fetchall()
    print('numeros total de linhas: ', cursor.rowcount)
    total =  cursor.rowcount
    for linha in linhas:
       # print("id",linha[1])
        #print("nome",linha[2])
        
        id_v.append ( linha[1])
        nome.append ( linha[2])
        ip.append (linha[3])
        sla.append (linha[6])
        grupo.append (linha[8])

    n=0
    for c in range(0,total):
        
        if c < total:
            i = c
            tabela.loc[c,"Id_vantive"] = id_v[i]
            tabela.loc[c,"Cliente"] = nome[i]
            tabela.loc[c,"Ip"] = ip[i]
            tabela.loc[c,"Sla"] = sla[i]
            tabela.loc[c,"Grupo"] = grupo[i]
        c+=1
    print(tabela)
    tabela.to_excel('BDS.xlsx')


    con.commit()
    cursor.close()

except Error as e:
    print(e)

finally:   
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada.")