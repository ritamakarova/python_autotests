import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='2fe68cdc7e49fd83a3f2a2285a055cbb'
HEADER = {'Contennt-Type' : 'application/json','trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "ritamakarova@yandex.ru",
    "password": "2ps-VVQ-tfc-cft"
   }
body_confirmation = {
    "trainer_token": TOKEN
   }
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
   }
body_new_name = {
    "pokemon_id": "69336",
    "name": "Мартазавр",
   }
body_catch = {
    "pokemon_id": "68602"
   }  


''' response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
# print (response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)
'''
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_new_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
