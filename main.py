from indices import *

class Service:
    def __init__(self, restaurant_repository):
        self.restaurant_repository = restaurant_repository

    def busca(self, query):
        resultados = []

        if query.name:
            nomes_encontrados = restaurante.buscar(query.name)
            resultados.append(nomes_encontrados)

        if query.cuisine_id:
            cozinhas_encontradas = cuisine_indice.buscar(query.cuisine_id)
            encontrados = []
            for c in cozinhas_encontradas:
                restaurante_cozinhas = repositorio_restaurante.find_by_cuisine(c.id)
                for rest in restaurante_cozinhas:
                    encontrados.append(rest)
            resultados.append(encontrados)


        if query.customer_rating:
            resultados.append(rating.maior_igual(int(query.customer_rating)))

        if query.distance:
            resultados.append(distancia.menor_igual(int(query.distance)))

        if query.price:
            resultados.append(valor.menor_igual(int(query.price)))

        if not query.distance and not query.customer_rating and not query.price and not query.name and not query.cuisine_id:
            resultados.append(RestaurantRepository().find_all())

        return leitura_csv.find_intersection(resultados)

if __name__ == '__main__':
    service1 = Service(repositorio_restaurante)
    restaurante1 = Restaurant('Deli', 2, 10, 100, 'I') #Nome - Classificação - Distância - Preço - Cozinha

    for r in service1.busca(restaurante1):
        print(r)
