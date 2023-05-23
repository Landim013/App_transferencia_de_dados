import requests

def last_chat_id(token):
    try:
        url = "https://api.telegram.org/bot{}/getUpdates".format(token)
        response = requests.get(url)
        if response.status_code == 200:
            json_msg = response.json()
            for json_result in reversed(json_msg['result']):
                message_keys = json_result['message'].keys()
                print(message_keys)
                if ('kkk' in message_keys) or ('group_chat_created' in message_keys):
                    return json_result['message']['chat']['id']
            print('Nenhum grupo encontrado')
        else:
            print('A resposta falhou, cógido de status: {}'.format(response.status_code))
    except Exception as e:
        print("Erro no getUpdates: ", e)

def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
        print('foi')
    except Exception as e:
        print('Erro no sendMessage: ', e)
#tokenLandim = "5874652496:AAGvNK6WlmsQ2ClnvX_DunfP7abPqfQx4eo"
#token_monitorb2b = "5314422542:AAGbXECqxtq3CCLIVErgK46G2X6X1tEbdlk"
token_monitorb2b = "5874652496:AAGvNK6WlmsQ2ClnvX_DunfP7abPqfQx4eo"
chat_id = '-1001721209785'
chat_id_dois = '-653087109'
chat_alto_tiete = '-844737653'

landim= '1310371343'
#msg = "MONITORAMENTO\n*CLIENTE FORA*\n\nCliente: {}\nId Vantive: {}\nIP: {}".format(cliente, id_vantive, ip)

#mteste = "teste"

msg = 'teste'


#send_message(token_monitorb2b, landim, msg)

res = last_chat_id(token_monitorb2b)
print(res)


