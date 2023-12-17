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

def main():
    while True:
        print("\n-=-=-=-=-=-=-=-=-=-=Busca Food=-=-=-=-=-=-=-=-=-=-")
        print("\nBem vindo ao Busca Food, seu buscador de Restaurantes!")
        print("\nMENU DE ESCOLHA:")

        name = (input("\nNome do Restaurante (Digite -1 para passar ou 0 para sair): "))
        if name == '0':
            print('Volte sempre!')
            break

        try:
            rating = int(input("\nClassificação do Restaurante (Digite -1 para passar): "))
        except ValueError:
            raise Exception('Classificação deve ser um número inteiro')
        
        try:
            distance = float(input("\nDistância do Restaurante (Digite -1 para passar): "))
        except ValueError:
            raise Exception('Distância deve ser um número ')
        
        try:
            price = float(input("\nPreço Médio do Restaurante (Digite -1 para passar): "))
        except ValueError:
            raise Exception('Preço deve ser um número ')
        
        cuisine = (input("\nTipo de Culinária do Restaurante (Digite -1 para passar):"))
        print()
        
        if name == '-1':
            name = None 
        if rating == -1:
            rating = None 
        if distance == -1:
            distance = None 
        if price == -1:
            price = None 
        if cuisine == '-1':
            cuisine = None 

        service1 = Service(repositorio_restaurante)
        restaurante1 = Restaurant(name,rating,distance,price,cuisine) #Nome - Classificação - Distância - Preço - Cozinha

        def bubble_sort_distance(vetor):
            if len(vetor) < 1 :
                return
            trocou = True
            elementos = len(vetor)-1
            while trocou:
                trocou = False
                for i in range(elementos):
                    if int(vetor[i].distance) > int(vetor[i+1].distance):
                        trocou = True
                        vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
        
        def bubble_sort_rating(vetor):
            if len(vetor) < 1 :
                return
            trocou = True
            elementos = len(vetor)-1
            while trocou:
                trocou = False
                for i in range(elementos):
                    if int(vetor[i].distance) == int(vetor[i+1].distance):
                        if int(vetor[i].customer_rating) < int(vetor[i+1].customer_rating):
                            trocou = True
                            vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

        def bubble_sort_price(vetor):
            if len(vetor) < 1 :
                return
            trocou = True
            elementos = len(vetor)-1
            while trocou:
                trocou = False
                for i in range(elementos):
                    if int(vetor[i].distance) == int(vetor[i+1].distance):
                        if int(vetor[i].customer_rating) == int(vetor[i+1].customer_rating):
                            if int(vetor[i].price) > int(vetor[i+1].price):
                                trocou = True
                                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
        
        resultado =  service1.busca(restaurante1)
        bubble_sort_distance(resultado)
        bubble_sort_rating(resultado)
        bubble_sort_price(resultado)
        if len(resultado) > 5:
            resultado = resultado[0:5]
        
        if len(resultado) < 1 :
            print('Sem resultados')
        else:
            for r in resultado:
                print(r)
        
        resp = input('\nDeseja continuar? [S/N]: ').upper().strip()[0]
        if resp == 'N':
            print('Volte sempre!')
            break

        

if __name__ == '__main__':
    main()

