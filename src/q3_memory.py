from typing import List, Tuple
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar un contador para los usernames mencionados
    username_counts = Counter()

    # Abrir el archivo especificado por file_path y procesar línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            # Parsear el JSON de la línea actual
            tweet = json.loads(line)
            # Obtener la lista de usuarios mencionados en el tweet actual
            mentioned_users = tweet.get('mentionedUsers')
            # Verificar si hay usuarios mencionados
            if mentioned_users:
                # Iterar sobre cada usuario mencionado
                for user in mentioned_users:
                    # Obtener el username del usuario
                    username = user.get('username')
                    # Verificar si se obtuvo un username válido
                    if username:
                        # Actualizar el contador de usernames con la frecuencia de cada username
                        username_counts[username] += 1

    # Obtener los 10 usernames más comunes y devolverlos como una lista de tuplas (username, frecuencia)
    most_influential_users = username_counts.most_common(10)
    return most_influential_users
