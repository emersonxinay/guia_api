import requests


def obtener_coches_por_precio_maximo(num_coches):
    # URL del API
    url = "https://myfakeapi.com/api/cars/"
    try:
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


# Ejemplo de uso
num_coches = 20
coches_por_precio_maximo = obtener_coches_por_precio_maximo(num_coches)

if coches_por_precio_maximo:
    print(f"Los {num_coches} coches con los precios más altos:")
    for coche in coches_por_precio_maximo:
        print(coche)
else:
    print("No se encontraron coches.")
