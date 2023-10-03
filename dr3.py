import requests


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


# Ejemplo de uso
vin = "SAJWJ0FF3F8321657"
coche_por_vin = obtener_coche_por_vin(vin)

if coche_por_vin:
    print(f"Coche con identificador VIN {vin}:")
    print(coche_por_vin)
else:
    print(f"No se encontró un coche con el identificador VIN {vin}.")
