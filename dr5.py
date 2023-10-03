import requests


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


# Ejemplo de uso
marca = "Mitsubishi"
anio_modelo = 2002
coches_por_marca_y_anio_modelo = obtener_coches_por_marca_y_anio_modelo(marca, anio_modelo)

print(f"Coches de la marca {marca} y año de modelo {anio_modelo}:")
for coche in coches_por_marca_y_anio_modelo:
    marca_coche, anio_coche = coche
    print(f"Marca: {marca_coche}, Año: {anio_coche}")
