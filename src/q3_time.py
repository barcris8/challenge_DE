from typing import List, Tuple 
from collections import Counter  
import json  

def q3_time(file_path: str) -> List[Tuple[str, int]]:  
    # Abrir el archivo en modo lectura
    with open(file_path, 'r') as f:  
        # Leer todas las líneas del archivo, parsear el JSON y obtener la lista de usuarios mencionados en cada tweet
        tweet = [json.loads(line)['mentionedUsers'] for line in f.readlines()]  

    # Extraer los nombres de usuario de la lista de usuarios mencionados, excluyendo los valores None
    usernames = [user['username'] for obj in tweet if obj is not None for user in obj]

    # Contar la frecuencia de cada nombre de usuario y devolver los 10 más comunes como una lista de tuplas (nombre de usuario, frecuencia)
    return Counter(usernames).most_common(10)
