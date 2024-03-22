from typing import List, Tuple
import json
from emoji import emoji_list
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Abrir el archivo JSON y leer las líneas
    with open(file_path, 'r') as f:
        tweets = f.readlines()

    # Unir el contenido de los tweets en una sola cadena
    single_string = "".join(json.loads(tweet)['content'] for tweet in tweets)
    
    # Obtener la lista de emojis presentes en la cadena
    emojis = [emoji['emoji'] for emoji in emoji_list(single_string)]

    # Contar la frecuencia de cada emoji y devolver los 10 más comunes como una lista de tuplas (emoji, frecuencia)
    return Counter(emojis).most_common(10)
