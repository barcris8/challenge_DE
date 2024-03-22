import matplotlib.pyplot as plt
import pandas as pd

def function_dispersion_graph(name_f1, time_f1, mem_usage_f1, name_f2, time_f2, mem_usage_f2):
    # Medidas de tiempo y memoria para diferentes funciones
    funciones = {
        name_f1: {'tiempo': time_f1, 'memoria': mem_usage_f1},
        name_f2: {'tiempo': time_f2, 'memoria': mem_usage_f2}
    }

    # Extraer las medidas de tiempo y memoria de las funciones
    tiempos = [funciones[funcion]['tiempo'] for funcion in funciones]
    memorias = [funciones[funcion]['memoria'] for funcion in funciones]

    # Colores para cada función
    colores = ['b', 'g']  # Azul y verde

    # Nombres de las funciones
    nombres = list(funciones.keys())

    # Crear el gráfico de dispersión con colores y nombres
    fig, ax = plt.subplots()
    for i, funcion in enumerate(funciones):
        ax.scatter(tiempos[i], memorias[i], c=colores[i], label=nombres[i])

    # Etiquetas de los ejes y título
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Memoria máxima en uso (Mb)')
    plt.title(f'{name_f1} vs {name_f2}')

    # Mostrar el nombre de cada función en el gráfico
    for i, funcion in enumerate(funciones):
        ax.text(tiempos[i], memorias[i], nombres[i])
        
        
     # Crear un DataFrame con los datos
    data = {'Funcion': list(funciones.keys()), 'Tiempo(s)': tiempos, 'Memoria(Mb)': memorias}
    df = pd.DataFrame(data)

    # Mostrar los datos en forma de tabla
    print(df)

    # Mostrar el gráfico
    plt.show()
