import requests
import json

with open('dados.txt') as arquivo:
    infos = arquivo.readlines()
    autorizacao = infos[0].strip().replace('\\n', '')
    client_id = infos[1].strip().replace('\\n', '')
    client_secret = infos[2].strip().replace('\\n', '')
    product_id = infos[3].strip().replace('\\n', '')


url = (f'https://api-sec-vlc.hotmart.com/security/oauth/token?grant_type=client_credentials&client_id={client_id}'
       f'&client_secret={client_secret}')
headers = {
    "Authorization": f"Basic {autorizacao}",
    "Content-Type": "application/json"
}

# Passando as informações necessários para pegar o token de acesso.
response = requests.post(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erro na solicitação:", response.status_code)
    exit()

print('-' * 60)

url = ('https://developers.hotmart.com/payments/api/v1/sales/history?transaction_status=COMPLETE'
       f'&start_date=1659322801000&end_date=30008999167000&product_id={product_id}&max_results=999')
headers = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {data["access_token"]}'
}

# Usando o token de acesso para obter informações sobre o histórico de vendas.
new_response = requests.get(url, headers=headers)

if response.status_code == 200:
    new_response_data = new_response.json()
    print(new_response_data)

    print('-' * 60)

    print(new_response_data['page_info'])

    print('-' * 60)

    print(new_response_data['items'])
else:
    print("Erro na solicitação:", response.status_code)
    exit()
