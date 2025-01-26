"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    file_path = "files/input/clusters_report.txt"


    with open(file_path) as file:
        aux = list(filter(None, map(str.strip, file.readlines())))[3:]

    columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]
    data, row = [], None

    for i in aux:
        i = i.split()

        if i[0].isdigit():
            if row: data.append(row)
            row = [int(i[0]), int(i[1]), float(i[2].replace(",", ".")), " ".join(i[4:]).replace(".", "")]
        else:
            row[-1] += " " + " ".join(i).replace(".", "")

    data.append(row)

    return pd.DataFrame(data, columns=columns)

print(pregunta_01())

