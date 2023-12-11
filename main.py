from indices import *

class Service:
    def __init__(self, restaurant_reposoitory):
        self.restaurant_repository = restaurant_reposoitory

    def busca(self, query):
        results = []

        if query.name:
            nomes_encontrados = restaurante.buscar(query.name)
            results.append(nomes_encontrados)
            if nomes_encontrados is None:
                results.append(RestaurantRepository.find_all())

        if query.customer_rating:
            results.append(rating.maior_igual(int(query.customer_rating)))

        if query.distance:
            results.append(distancia.menor_igual(int(query.distance)))

        if query.price:
            results.append(valor.menor_igual(int(query.price)))

        if not query.distance and not query.customer_rating and not query.price and not query.name and not query.cuisine_id:
            results.append(RestaurantRepository().find_all())

        return leitura_csv.find_intersection(results)

if __name__ == '__main__':
    service1 = Service(RestaurantRepository)
    restaurante1 = Restaurant(None, 5, 7, 10, 0) #Nome - Classificação - Distância - Preço - Cozinha
                                                    #Falta cuisine
    for r in service1.busca(restaurante1):
        print(r)
