import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='2fe68cdc7e49fd83a3f2a2285a055cbb'
HEADER = {'Contennt-Type' : 'application/json','trainer_token' : TOKEN }
TRAINER_ID = '5056'
NAME = 'Марта'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'
    
@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '70149')]) 
def test_parametrize (key, value) : 
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value    
    
def test_status_code():
    response_trainers = requests.get(url = f'{URL}/trainers', params = {'name': NAME})
    assert response_trainers.status_code == 200 