from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
Base de datos de LifeStore

lifestore_products = [id_product, name, price, category, stock]

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]

lifestore_searches = [id_search, id product]
"""

#1. PRODUCTOS MÁS VENDIDOS Y PRODUCTOS REZAGADOS


#---------------------------------------#
#1.1 Generar listado de los 5 productos con mayores ventas
#––––––––––––––––––––––––––––––---------#
'''
#Comentario: Se hace una nueva lista de lifestore_sales tomando los parametros [0] y [4], correspondientes a id_sales y refund. Posteriormente se utiliza if para filtrar únicamente las ventas efectuadas (- refund)

id_ventas_validas =[sale[1] for sale in lifestore_sales if sale[4] == 0]
for par in id_ventas_validas:
  print(par)

#Cálculo número de ocurrencias de la base de datos id_refund
frecuencia_ventas = {}

for par in id_ventas_validas:
  if par in frecuencia_ventas:
    frecuencia_ventas[par] += 1
  else:
    frecuencia_ventas[par] = 1

print("La frecuencia de los productos más comprados son: ", frecuencia_ventas)

'''
#---------------------------------------#
#1.2 Por categoria, generar listado con 10 productos con mayores busquedas
#–––––––––––––––––––––––––––––---------–#
"""
#Generación de lista de mayores búsquedas
mayores_busquedas = [producto[1] for producto in lifestore_searches]
for n in mayores_busquedas:
  print(n)

#Dicionario
frecuencia_busquedas = {}

#Se denomina el elemento b dentro del diccionario
for b in mayores_busquedas:
  if b in frecuencia_busquedas:
    frecuencia_busquedas[b] += 1
  else:
    frecuencia_busquedas[b] = 1

print("La frecuencia de los productos más buscados son: ", frecuencia_busquedas)

"""

#---------------------------------------#
#1.3 Por categoría, listado con 5 productos con menores ventas
#––––––––––––––––––––––––––––––---------#

"""
#Generación de lista de mayores búsquedas
mayores_busquedas = [producto[1] for producto in lifestore_searches]
for n in mayores_busquedas:
  print(n)

#Dicionario
frecuencia_busquedas = {}

#Se denomina el elemento b dentro del diccionario
for b in mayores_busquedas:
  if b in frecuencia_busquedas:
    frecuencia_busquedas[b] += 1
  else:
    frecuencia_busquedas[b] = 1

print("La frecuencia de los productos más buscados son: ", frecuencia_busquedas)

#Mismo 
"""

#---------------------------------------#
#1.4 Por categoría, listado con 10 productos con menores busquedas
#---------------------------------------#

"""
# Diccionario de busquedas por id
productos_busquedas = {}
for search in lifestore_searches:
    prod_id = search[1] #variable de producto que se buscó
    search_id = search[0] #variable de número de busqueda
    if search_id not in productos_busquedas.keys():
        productos_busquedas[search_id] = []
    productos_busquedas[search_id].append(prod_id)

# Diccionario de ids por categoria
cat_prods = {}
for prod in lifestore_products:
    prod_id = prod[0]
    cat = prod[3]
    if cat not in cat_prods.keys():
        cat_prods[cat] = []
    cat_prods[cat].append(prod_id)

# Ventas por categorias
cat_ventas = {}
for cat in cat_prods.keys():
    # La lista de productos de la categoria
    prods_list = cat_prods[cat]

    # Lista vacía para las search_id por categoria inciando ganancias y ventas en cero
    busquedas_cat = []
    ganancias = 0
    ventas = 0

    # Por cada producto de esa categoria
    for prod_id in prods_list:
        # Obtengo las reviews, precio y cantidad de ventas del producto
        if prod_id not in productos_busquedas.keys():
            continue
        searches = productos_busquedas[prod_id]
        precio = lifestore_products[prod_id-1][2]
        total_sales = len(searches)
        # Guardo las ganancias y total de ventas en los datos de la categoria
        ganancias += precio * total_sales
        ventas += total_sales
        busquedas_cat += searches

    # Calculo la search_id promedio de la categoria
    busq_prom_cat = sum(busquedas_cat)/len(busquedas_cat)
    # Guardo todo en mi diccionario
    cat_ventas[cat] = {
        'Busquedas promedio': busq_prom_cat,
        'Ganancias totales': ganancias,
        'ventas_totales': ventas
    }

f'string'

for key in cat_ventas.keys():
    print(key)
    for llave, valor in cat_ventas[key].items():
        print(f'\t {llave}: {valor}')
""
#---------------------------------------#
#EXTRA:  Por categoría, listado con 10 productos con menores busquedas
#---------------------------------------#
'''
#1 Creación de diccionario para organizar los productos por categorias
productos_por_categoria = {}

#2 Iterar dentro del diccionario las variables
for producto in lifestore_products:
  id = producto [0]
  cat = producto [3]

#3 Se revisa si la categoria se encuentra dentro del diccionario
  if cat not in productos_por_categoria.keys():
      productos_por_categoria[cat] = []
  productos_por_categoria[cat].append (id)     

#4 Creación de diccionario para organizar Producto y Búsqueda
busqueda_productos = {}
for prod in lifestore_searches:
  busqueda_productos[prod[1]] = 0

for busqueda in lifestore_searches:
  id_prod = busqueda[1]
  busqueda_productos[id_prod] += 1
print(busqueda_productos)

#5 productos_por_categoria + busqueda_productos

#Se imprime solo las categorias (8)
for key, value in productos_por_categoria.items():
    print(f"categoria", key)

#Cantidad de busquedas por categoria
    suma_busquedas = 0
    for el in value: #lista de id por categoría
        if el in busqueda_productos.keys():
          suma_busquedas += busqueda_productos[el]
    print(suma_busquedas)

'''