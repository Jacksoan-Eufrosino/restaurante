# Restaurante
O projeto Restaurante é uma aplicação que visa gerenciar e organizar informações relacionadas a uma variedade de restaurantes. Com uma estrutura orientada a objetos, o projeto oferece funcionalidades que permitem aos usuários pesquisar, filtrar e obter informações específicas sobre restaurantes com base em critérios como o tipo de culinária, classificação, nome, preço e distância.

# Implementação
Para o funcionamento do projeto, foi necessário a criação de alguns arquivos citados abaixo:

### estrutura_triNode.py

Possui uma estrutura de árvore com métodos que tem a finalidade de buscar um elemento na árvore e outro método para adicionar um elemento na árvore.

### indices.py

Contém duas estruturas com a finalidade de adicionar e realizar buscas. A primeira classe NumberInvertedIndex é utilizada para adicionar e buscar elementos do tipo numérico, podendo escolher se deseja realizar a busca pelo elemento maior ou igual que o valor passado como parâmetro ou menor ou igual. Já a segunda classe PartialStringInvertedIndex é utilizada apenas para adicionar elementos do tipo str, realizando também buscas utilizando uma estrutura de árvore.

### leitura_csv.py

Estrutura para ler e armazenar os elementos dos arquivos csv.

### repositorioRestaurante.py

Organiza todos os restaurantes e cozinhas em diferentes classes, e retorna cada um deles ao serem instanciados.

### restaurant.py

Possui uma classe que contém os parâmetros __name, customer_rating, distance, price, cuisine_id.__

# Execução

O programa contém um menu de escolha que irá solicitar um parâmetro por vez, na ordem do NOME - CLASSIFICAÇÃO, DISTÂNCIA, PREÇO e TIPO DA COZINHA. Para ignorar um dos parâmetros basta digitar -1, e para cancelar a busca basta digitar 0 na primeira requisição do nome do restaurante. Ao terminar a busca, será solicitado se o usuário deseja realizar outra busca ou se deseja encerrar o programa.

# Contribuintes
**Antony César - 20231380013**

**Arthur de Macêdo - 20231380021**

**Gabriel Andrade - 20231380027**

**Jacksoan Eufrosino - 20231380018**
