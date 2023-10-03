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


# Ejemplo de uso
color = "blue"
coches_por_color = obtener_coches_por_color(color)

if coches_por_color:
    print(f"Coches con color {color}:")
    for coche in coches_por_color:
        print(coche)
else:
    print(f"No se encontraron coches con el color {color}.")
