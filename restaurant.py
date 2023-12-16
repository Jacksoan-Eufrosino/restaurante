class Cuisine:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Restaurant:
    def __init__(self, name, customer_rating, distance, price, cuisine_id):
        self.name = name
        self.customer_rating = customer_rating
        self.distance = distance
        self.price = price
        self.cuisine_id = cuisine_id

    def __str__(self):
        return "Nome: " + self.name + " Classificação: " + self.customer_rating + \
            " Distância: " + self.distance + " Preço: " + \
            self.price + " Cozinha: " + self.cuisine_id
