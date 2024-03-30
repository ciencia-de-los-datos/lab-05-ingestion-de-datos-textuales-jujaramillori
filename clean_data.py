"""
La información requerida para este laboratio esta almacenada en el archivo 
"data.zip" ubicado en la carpeta raíz. Descomprima este archivo. 

A partir de esta informacion debe generar dos archivos llamados "train_dataset.csv" y 
"test_dataset.csv". Estos archivos deben tener la siguiente estructura:

* phrase: Texto de la frase. hay una frase por cada archivo de texto.
* sentiment: Sentimiento de la frase. Puede ser "positive", "negative" o "neutral". Este corresponde al nombre del directorio donde se encuentra ubicado el archivo.
"""
import pandas as pd
import os

# Funcion para leer los archivos de texto y almacenarlos en un DataFrame
def read_files(directory):
    phrases = []
    sentiments = []

# Se recorre el directorio y se obtienen los archivos de texto
    for subdir in os.listdir(directory):
        # Se verifica si el archivo es un directorio
        if os.path.isdir(os.path.join(directory, subdir)):
            # Se recorren los archivos de texto
            for file in os.listdir(os.path.join(directory, subdir)):
                # Se verifica si el archivo es un archivo de texto
                if file.endswith(".txt"):
                    # Se lee el archivo de texto
                    with open(os.path.join(directory, subdir, file), "r", encoding= "utf-8") as f:
                        # Se almacena el contenido del archivo de texto
                        for line in f:
                            # Se almacena la frase y el sentimiento
                            phrases.append(line.strip())
                            sentiments.append(subdir)
    return pd.DataFrame({"phrase": phrases, "sentiment": sentiments})

# Se leen los archivos de texto train y test y se almacenan en DataFrames
train_df = read_files("data/train")
test_df = read_files("data/test")

# print(read_files(train_df))
# print(read_files(test_df))

# Se almacenan los DataFrames en archivos CSV
train_df.to_csv("train_dataset.csv", index=False)
test_df.to_csv("test_dataset.csv", index=False)

# print(train_df['sentiment'].value_counts())
# print(test_df['sentiment'].value_counts())
# print(train_df.columns[0])
# print(train_df.columns[1])






