import requests

# Función para convertir un precio en formato de cadena a un valor numérico
def convertir_precio(precio_str):
    try:
        # Eliminar el símbolo "$" y cualquier carácter que no sea un número o un punto
        precio_str = ''.join(filter(lambda x: x.isdigit() or x == '.', precio_str))
        return float(precio_str)
    except ValueError:
        return 0.0  # Si no se puede convertir, se devuelve 0.0

def obtener_coches_precio_mayor_o_igual(precio_minimo):
    # URL del API
    url = "https://myfakeapi.com/api/cars/"

    try:
        # Realizar solicitud HTTP GET
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la respuesta es exitosa
        data = response.json()  # Obtener los datos de la respuesta en formato JSON
        coches = data["cars"]  # Obtener la lista de coches del diccionario "data"

        # Convertir el precio de cada coche a un valor numérico y filtrar por precio mínimo
        coches_filtrados = [coche for coche in coches if convertir_precio(coche["price"]) >= precio_minimo]

        # Ordenar la lista filtrada por precio de mayor a menor
        coches_ordenados_por_precio = sorted(coches_filtrados, key=lambda coche: convertir_precio(coche["price"]), reverse=True)

        # Limitar la lista resultante a los primeros 20 coches
        primeros_20_coches = coches_ordenados_por_precio[:4]

        return primeros_20_coches

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

# Obtener el precio mínimo desde el usuario
precio_minimo = float(input("Ingrese el precio mínimo: "))

# Uso de la función
coches_filtrados = obtener_coches_precio_mayor_o_igual(precio_minimo)
print(f"Los primeros 20 coches con precio mayor o igual a ${precio_minimo}:")
mostrar_coches(coches_filtrados)
