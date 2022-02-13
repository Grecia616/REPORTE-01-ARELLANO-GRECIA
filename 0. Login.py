from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
Base de datos de LifeStore

lifestore_products = [id_product, name, price, category, stock]

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]

lifestore_searches = [id_search, id product]
"""
#0 LOGIN DE USUARIO

""""
Usuario:  
  Grecia_Arellano
Contraseña:
  Abeq03 
"""

Usuario_Acceso = False
No_Intentos = 0

#1 Mensaje de Bienvenida
Mensaje_bienvenida = "¡Bienvenido(a) a LifeStore!\nPor favor, ingrese su Usuario y Contraseña"
print(Mensaje_bienvenida)

#2 Número de intentos
while not Usuario_Acceso:
  Usuario = input("Usuario: ")
  Contraseña = input("Contraseña: ")
  No_Intentos += 1

#3 Usuario y Contraseña deben coincidir
  if Usuario == "Grecia_Arellano" and Contraseña == "Abeq03" :
    Usuario_Acceso = True

#4 Bienvenida al IntraStore (Usuario y Contraseña Correcta)
    print("¡Bienvenido(a) al IntraStore!")

#5 Define número de intentos / Si Usuario y Contraseña son diferentes 
  else:
    print("Tienes", 3 - No_Intentos, "intentos restantes" )
    if Usuario == "Grecia_Arellano" :
      print("Contraseña Incorrecta")
    else:
      print(f"El Usuario: {Usuario} no está registrado")
  
  if No_Intentos == 3: 
    exit()