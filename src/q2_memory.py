from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
from emoji import emoji_list

def q2_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Inicializar un contador para emojis
    emoji_counts = Counter()

    # Abrir el archivo especificado por file_path y procesar línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            # Parsear el JSON de la línea actual
            tweet = json.loads(line)
            # Obtener el contenido del tweet
            content = tweet['content']
            # Obtener la lista de emojis presentes en el contenido del tweet
            emojis = [emoji['emoji'] for emoji in emoji_list(content)]
            # Actualizar el contador de emojis con la frecuencia de emojis en el tweet actual
            emoji_counts.update(emojis)

    # Obtener los 10 emojis más comunes y devolverlos como una lista de tuplas (emoji, frecuencia)
    most_common_emojis = emoji_counts.most_common(10)
    return most_common_emojis
