import requests


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


# Ejemplo de uso
marca = "Toyota"
modelo = "Echo"
coches_por_marca_y_modelo = obtener_coches_por_marca_y_modelo(marca, modelo)

if coches_por_marca_y_modelo:
    print(f"Coches de la marca {marca} y modelo {modelo}:")
    for marca, modelo in coches_por_marca_y_modelo:
        print(f"Marca: {marca}, Modelo: {modelo}")
else:
    print(f"No se encontraron coches de la marca {marca} y modelo {modelo}.")
