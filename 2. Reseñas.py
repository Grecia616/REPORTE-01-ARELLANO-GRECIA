from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
Base de datos de LifeStore

lifestore_products = [id_product, name, price, category, stock]

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]

lifestore_searches = [id_search, id product]
"""
#PRODUCTOS POR RESEÑA EN EL SERVICIO

#-------------------------------------------------#
#2.1 Listado para productos con mejores y peores reseñas
#-------------------------------------------------#

#Diccionario ID vs Reviews

product_reviews = {}
for sale in lifestore_sales:
    product_id = sale[1] #[1] = Producto vendido
    review = sale [2] #[2] = Score
    if product_id not in product_reviews.keys() :
        product_reviews[product_id] =[]
    product_reviews[product_id].append(review)

#print(product_reviews)
for key in product_reviews.keys():
    print("id producto vendido", key)
    #print("reviews", product_reviews[key])

#Orden de datos
reviews_order = sorted(product_reviews.items(), key = lambda item: item[1], reverse = True)
print(reviews_order)
