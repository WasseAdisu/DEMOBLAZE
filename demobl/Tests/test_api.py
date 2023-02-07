import allure
import pytest
import requests

from Api.constants.constants_loc import loginloc


class TestApi:

    @allure.description('test_api ')
    # @pytest.Mark.sanity
    def test_logApi(self):
        url = loginloc.url_signUp
        data = loginloc.signUo_correct
        responce = requests.post(url, json=data)
        responce.json()
        assert  responce.status_code == 200
        assert responce.elapsed.total_seconds() < 10
        assert responce.json()["errorMessage"] == "This user already exist."

    @allure.description('test_api ')
    # @pytest.Mark.sanity
    def test_viewcart(self):
        url = loginloc.url_viewcart
        data = loginloc.j_da
        responce = requests.post(url, json=data)
        responce.json()
        assert responce.status_code == 200
        assert  responce.elapsed.total_seconds() <10

    @allure.description('test_api ')
    # @pytest.Mark.sanity
    def test_addcart(self):
        url = loginloc.url_add_cart
        data = loginloc.item_data
        responce = requests.post(url, json=data)
        responce.json()
        assert responce.status_code == 200
        assert responce.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    #@pytest.Mark.sanity
    def test_api(self):
        url = "https://api.demoblaze.com/entries"
        responce = requests.get(url)
        responce.json()
        assert responce.status_code == 200
        assert responce.elapsed.total_seconds() < 10
        assert responce.json()["Items"][0]["title"] == "Samsung galaxy s6"


