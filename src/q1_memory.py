from typing import List, Tuple
from datetime import datetime, date
from collections import Counter
import json

def q1_memory(file_path: str) -> List[Tuple[date, str]]:
    # Diccionario para contar los tweets por fecha y usuario
    tweets_count = {}

    # Abrir el archivo JSON y procesar línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            # Parsear el JSON de la línea actual
            tweet = json.loads(line)
            # Extraer la fecha del tweet y convertirla a objeto datetime.date
            date = datetime.strptime(tweet['date'].split('T')[0], "%Y-%m-%d").date()
            # Extraer el nombre de usuario del tweet
            username = tweet['user']['username']

            # Verificar si la fecha ya está en el diccionario, si no, inicializar un diccionario vacío para esa fecha
            if date not in tweets_count:
                tweets_count[date] = {}
            # Verificar si el usuario ya está en el diccionario de la fecha actual, si no, inicializar su contador en 0
            if username not in tweets_count[date]:
                tweets_count[date][username] = 0
            # Incrementar el contador de tweets para el usuario en la fecha correspondiente
            tweets_count[date][username] += 1

    # Lista para almacenar las fechas y los usuarios más activos
    result = []
    # Ordenar el diccionario por la suma de los valores de los contadores de usuario en orden descendente y seleccionar los primeros 10
    for date, users_count in sorted(tweets_count.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]:
        # Obtener el usuario más activo para la fecha actual
        top_user = max(users_count, key=users_count.get)
        # Agregar la fecha y el usuario más activo a la lista de resultados
        result.append((date, top_user))

    return result

