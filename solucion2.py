import requests


def obtener_coches_por_precio_maximo():
    # URL del API
    url = "https://myfakeapi.com/api/cars/"

    try:
        # Realizar solicitud HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        data = response.json()  # Obtener los datos de la respuesta en formato JSON
        coches = data["cars"]  # Obtener la lista de coches del diccionario "data"

        # Solicitar al usuario ingresar el precio máximo
        precio_maximo = float(input("Ingrese el precio máximo: "))

        # Filtrar los coches por precio máximo
        coches_por_precio_maximo = [coche for coche in coches if float(coche["price"].strip("$")) <= precio_maximo]

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


def mostrar_coches(coches):
    if not coches:
        print("No se encontraron coches.")
        return

    for coche in coches:
        print(coche)
    print()


# Uso de la función
coches = obtener_coches_por_precio_maximo()
print("Coches con precio máximo:")
mostrar_coches(coches)
