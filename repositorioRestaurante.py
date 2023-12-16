import estrutura_triNode
import leitura_csv
from restaurant import *

class RestaurantRepository:
    def __init__(self):
        self.__import_restaurants()

    def find_all(self):
        return self.restaurants

    def find_by_cuisine(self, cuisine_id):
        matching_restaurants = []
        for restaurant in self.restaurants:
            if restaurant.cuisine_id == cuisine_id:
                matching_restaurants.append(restaurant)
        return matching_restaurants

    def __import_restaurants(self):
        rest_dics = leitura_csv.read_csv('restaurants.csv')
        self.restaurants = [Restaurant(**rest) for rest in rest_dics]


class CuisineRepository:
    def __init__(self):
        self.__import_cuisines()

    def find_all(self):
        return self.cuisines

    def __import_cuisines(self):
        cuisine_dicts = leitura_csv.read_csv('cuisines.csv')
        self.cuisines = [Cuisine(**cuisine) for cuisine in cuisine_dicts]

repositorio_restaurante = RestaurantRepository()
repositorio_cozinha = CuisineRepository()
