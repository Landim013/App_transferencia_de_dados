import mysql.connector
from mysql.connector import Error
from subprocess import Popen, PIPE
import subprocess
from datetime import datetime, time
import time
import requests

from constantes import HOST_INACESSIVEL, PING, SLEEP, VEZES


def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print('Erro no sendMessage: ', e)


con = mysql.connector.connect(host='localhost', database='mysql',
                              user='root', password='')

try:
    if con.is_connected():
        while (True):
            db_info = con.get_server_info()
            print('Conectado ao servidor MySQL versão ', db_info)
            cursor = con.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print("Conectado ao banco de dados ", linha)

            query = """SELECT  ip,modelo,nome, vezes_off, id_programa  
                            FROM ping_danilo ;"""
            cursor.execute(query)

            linhas = cursor.fetchall()
            ativos = 0
            inativos = 0
            for linha in linhas:
                ip = linha[0]
                modelo = linha[1]
                nome = linha[2]
                vezes = int(linha[3])
                id_prog = linha[4]
                print('ok 1')

                resposta = subprocess.run(
                    'ping {} -n {}'.format(ip, PING), stdout=PIPE)
                rede_destino = str(resposta)
                if (resposta.returncode == 0 and HOST_INACESSIVEL not in rede_destino):
                    ativos += 1
                    update = "UPDATE ping_danilo SET SITUACAO = true WHERE id_programa = {}".format(id_prog)
                        
                    update_vezes = "UPDATE ping_danilo SET vezes_off = 0 WHERE id_programa = {}".format(id_prog)
                    cursor.execute(update_vezes)
                    print('ok 2')
                else:
                    vezes += 1
                    inativos += 1

                    print(vezes)
                    if (vezes == VEZES):

                        token = '5874652496:AAGvNK6WlmsQ2ClnvX_DunfP7abPqfQx4eo'
                        chat_id = ''
                        id = '1310371343'

                        msg = """MONITORAMENTO\n**CLIENTE FORA**
                        \n\nTipo de cliente: EQUIPAMENTO DE REDE \nIP: {}\nMODELO: {}\nNOME: {}""".format(ip, modelo, nome)

                        send_message(token, id, msg)

                    update = "UPDATE ping_danilo SET situacao = false WHERE id_Programa= {}".format(id_prog)
                    update_vezes = "UPDATE ping_danilo SET vezes_off = {} WHERE id_programa = {}".format(vezes, id_prog)
                    cursor.execute(update_vezes)

                cursor.execute(update)
                con.commit()
                print("IP: {} --- MODELO: {}".format(ip, modelo))
                print("Tipo de cliente: ELEMENTO DE REDE")

            horario = datetime.today().strftime('%d/%m %H:%M')
            inserir_hora = "INSERT INTO horarios (ultimo_ping, tipo_cliente) values('{}', 'ELEMENTO DE REDE')".format(horario)
            cursor.execute(inserir_hora)
            con.commit()
            '''print("Ativos: {} \nInativos: {}".format(ativos, inativos))
            print('Fimmmmmmmmmmmmmmmmmmmm')'''
            time.sleep(SLEEP)

            # cursor.close()


except Error as e:
    print(e)

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada.")
