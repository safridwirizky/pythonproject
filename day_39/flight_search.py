import requests, os

class CollectData():
    def __init__(self):
        self.URL = "https://test.api.amadeus.com/v1"
        self.GET_URL = "/reference-data/locations/cities"
        self.city = 'PARIS'
        self.header = {
            
        }
        self.param_amadeus = {
            "keyword": self.city
        }

    def get_data(self):
        requests.get(url=self.URL+self.GET_URL, headers=)