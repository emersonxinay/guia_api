import requests


def obtener_coches_por_color(color):
    # URL del API
    url = "https://myfakeapi.com/api/cars/"
    try:
        # Realizar solicitud HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        data = response.json()  # Obtener los datos de la respuesta en formato JSON
        coches = data["cars"]  # Obtener la lista de coches del diccionario "data"

        # Filtrar los coches por color
        coches_por_color = [coche for coche in coches if coche["car_color"] == color]
        return coches_por_color

    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud HTTP
        print(f"Error al realizar la solicitud HTTP: {str(e)}")

    except ValueError as e:
        # Manejar errores al procesar la respuesta JSON
        print(f"Error al procesar la respuesta JSON: {str(e)}")

    except Exception as e:
        # Manejar otros errores inesperados
        print(f"Error inesperado: {str(e)}")



def obtener_coches_por_precio_maximo(num_coches):
    
    # URL del API
    url = "https://myfakeapi.com/api/cars/"
    try:
        num_coches = int(round(num_coches))
        # Realizar solicitud HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        data = response.json()  # Obtener los datos de la respuesta en formato JSON
        coches = data["cars"]  # Obtener la lista de coches del diccionario "data"

        # Ordenar la lista de coches por precio en orden descendente
        coches_ordenados_por_precio = sorted(coches, key=lambda coche: float(coche["price"].strip("$")), reverse=True)

        # Seleccionar los primeros num_coches coches de la lista ordenada
        coches_por_precio_maximo = coches_ordenados_por_precio[:num_coches]
        return coches_por_precio_maximo

    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud HTTP
        print(f"Error al realizar la solicitud HTTP: {str(e)}")

    except ValueError as e:
        # Manejar errores al procesar la respuesta JSON
        print(f"Error al procesar la respuesta JSON: {str(e)}")

    except Exception as e:
        # Manejar otros errores inesperados
        print(f"Error inesperado: {str(e)}")


def obtener_coche_por_vin(vin):
    # URL del API
    url = f"https://myfakeapi.com/api/cars/"

    try:
        # Realizar solicitud HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        data = response.json()  # Obtener los datos de la respuesta en formato JSON
        coches = data["cars"]  # Obtener la lista de coches del diccionario "data"

        # Buscar el coche por VIN
        coche_por_vin = next((coche for coche in coches if coche["car_vin"] == vin), None)
        return coche_por_vin

    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud HTTP
        print(f"Error al realizar la solicitud HTTP: {str(e)}")

    except ValueError as e:
        # Manejar errores al procesar la respuesta JSON
        print(f"Error al procesar la respuesta JSON: {str(e)}")

    except Exception as e:
        # Manejar otros errores inesperados
        print(f"Error inesperado: {str(e)}")
# requerimiento 4
def obtener_coches_por_marca_y_modelo(marca, modelo):
    # URL del API
    url = "https://myfakeapi.com/api/cars/"
    try:
        response = requests.get(url)  # Realizar solicitud HTTP GET
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        data = response.json()  # Obtener los datos de la respuesta en formato JSON
        coches = data["cars"]  # Obtener la lista de coches del diccionario "data"

        # Filtrar los coches por marca y modelo
        coches_por_marca_y_modelo = [(coche["car"], coche["car_model"]) for coche in coches if
                                     coche["car"] == marca and coche["car_model"] == modelo]

        return coches_por_marca_y_modelo

    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud HTTP
        print(f"Error al realizar la solicitud HTTP: {str(e)}")

    except ValueError as e:
        # Manejar errores al procesar la respuesta JSON
        print(f"Error al procesar la respuesta JSON: {str(e)}")

    except Exception as e:
        # Manejar otros errores inesperados
        print(f"Error inesperado: {str(e)}")

# Requerimiento 5
def obtener_coches_por_marca_y_anio_modelo(marca, anio_modelo):
    # URL del API
    url = f"https://myfakeapi.com/api/cars/"

    try:
        response = requests.get(url)  # Realizar solicitud HTTP GET
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        data = response.json()  # Obtener los datos de la respuesta en formato JSON
        coches = data["cars"]  # Obtener la lista de coches del diccionario "data"

        # Filtrar los coches por marca y año de modelo
        coches_por_marca_y_anio_modelo = [(coche["car"], coche["car_model_year"]) for coche in coches if
                                          coche["car"] == marca and coche["car_model_year"] == anio_modelo]

        return coches_por_marca_y_anio_modelo

    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud HTTP
        print(f"Error al realizar la solicitud HTTP: {str(e)}")

    except ValueError as e:
        # Manejar errores al procesar la respuesta JSON
        print(f"Error al procesar la respuesta JSON: {str(e)}")

    except Exception as e:
        # Manejar otros errores inesperados
        print(f"Error inesperado: {str(e)}")



def mostrar_coches(coches):
    for coche in coches:
        print(coche)
    print()


def menu():
    print("¡Bienvenido al menú de opciones de coches!")
    print("1. Obtener coches por color")
    print("2. Obtener coches por precio máximo")
    print("3. Obtener coche por car_vin")
    print("4. Obtener coches por marca y modelo")
    print("5. Obtener coches por marca y año de modelo")
    print("6. Salir")
    print()

    while True:
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            color = input("Ingrese el color de los coches: ")
            coches_por_color = obtener_coches_por_color(color)
            if coches_por_color:
                print(f"Coches con color {color}:")
                mostrar_coches(coches_por_color)
            else:
                print(f"No se encontraron coches con el color {color}.")

        elif opcion == "2":
            precio_maximo = float(input("Ingrese la cantidad de coches para mostrar los precios más altos: "))
            coches_por_precio_maximo = obtener_coches_por_precio_maximo(precio_maximo)
            if coches_por_precio_maximo:
                print(f"Coches con precio máximo de ${precio_maximo}:")
                mostrar_coches(coches_por_precio_maximo)
            else:
                print(f"No se encontraron coches con un precio máximo de ${precio_maximo}.")

        elif opcion == "3":
            vin = input("Ingrese el VIN del coche: ")
            coche_por_vin = obtener_coche_por_vin(vin)
            if coche_por_vin:
                print(f"Información del coche con VIN {vin}:")
                print(coche_por_vin)
                print()
            else:
                print(f"No se encontró un coche con el VIN {vin}.")

        elif opcion == "4":
            marca = input("Ingrese la marca de los coches: ")
            modelo = input("Ingrese el modelo de los coches: ")
            coches_por_marca_y_modelo = obtener_coches_por_marca_y_modelo(marca, modelo)
            if coches_por_marca_y_modelo:
                print(f"Coches de la marca {marca} y modelo {modelo}:")
                mostrar_coches(coches_por_marca_y_modelo)
            else:
                print(f"No se encontraron coches de la marca {marca} y modelo {modelo}.")

        elif opcion == "5":
            marca = input("Ingrese la marca de los coches: ")
            anio_modelo = int(input("Ingrese el año de modelo de los coches: "))
            coches_por_marca_y_anio_modelo = obtener_coches_por_marca_y_anio_modelo(marca, anio_modelo)
            if coches_por_marca_y_anio_modelo:
                print(f"Coches de la marca {marca} y año de modelo {anio_modelo}:")
                mostrar_coches(coches_por_marca_y_anio_modelo)
            else:
                print(f"No se encontraron coches de la marca {marca} y año de modelo {anio_modelo}.")

        elif opcion == "6":
            print("¡Gracias por usar el programa!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        print()


# Ejecutar el menú
menu()