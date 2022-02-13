from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

from statistics import mean

"""
Base de datos de LifeStore

lifestore_products = [id_product, name, price, category, stock]

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]

lifestore_searches = [id_search, id product]
"""

#----------------------------------------#
#3.4 Meses con más ventas en el año
#----------------------------------------#

#Variable
id_fecha = [[sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0] # Se toma el id venta + fecha

#Para categorizar usamos un diccionario
categorizacion_meses = {}

for par in id_fecha:
  #ID + Mes
  id = par[0]
  _, mes,_ = par[1].split("/") #Se toma únicamente el valor del mes, pues es representativo

  #Si mes no existe como llave, se crea
  if mes not in categorizacion_meses.keys():
    categorizacion_meses[mes]= []

  categorizacion_meses[mes].append(id) #Por medio de la función id se guarda el id y mes

for key in categorizacion_meses.keys():
  print(key) #Solo imprime los meses
  print(categorizacion_meses[key]) #Imprime el identificador de producto por mes

#para calcular por mes
suma_anual = 0
for key in categorizacion_meses.keys(): #Iteración
    lista_mes = categorizacion_meses[key] # Toma el contenido del mes y los agrupa en la lista
    suma_venta = 0
    for id_venta in lista_mes:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_product = info_venta[1]
        precio = lifestore_products[id_product - 1][2] #Extracción de columnas de Identificador (se pone -1 porque las listas empiezan con 0) y precio[2]
        suma_venta += precio

    print (key, "La suma mensual es de: ", "$", suma_venta, f"Número de ventas efectuadas: {len(lista_mes)}") # key = mes / suma_venta = total de precios / lista_mes = número de elementos del total de ventas por mes

#----------------------------------------#
#3.1 Total ingresos (Anual)
#----------------------------------------#
# Cantidad vendida * precio
    suma_anual += suma_venta #acumulado de ventas mensuales
    print("Acumulado mensual o total de ingresos anuales: ", "$", suma_anual)

promedio_mensual = suma_anual / len(lista_mes)
print("El promedio mensual del año 2020 es:" ,promedio_mensual)

