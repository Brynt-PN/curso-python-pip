import csv

# Aqui convertiremos los datos extraidos en un DICCIONARIO
# donde la clave sea la cabesera de la columna y el valor
# sea el contenido y asi se facilite su lectura.
def read_csv(f):
    with open(f,'r') as csv_f:
        reader = csv.reader(csv_f,delimiter=',')
        header = next(reader)# Al ser READER un iterable,
        # podemos iterar su primera linea de forma manual
        # y asi capturar las cabeseras y guardarlas en una
        # variable aparte HEADER
        BD = [] # Creamos una LISTA para guardar tosos los 
        # DICCIONARIOS que vamos a crear.
        for i in reader:
            iterable = zip(header,i)# Con ZIP unimos 2 LISTAS
            # y las guardamos en ITERABLE, lo que retorna es una
            # lista de TUPLAS, cada tupla es un par de datos
            dic_iterable = {key : value for key,value in iterable}
            # Usamos el formato DIC COMPRES para crear un Diccionario,
            # dudas revisa el archivo 05_Dic_Comprimidos, le indicamos
            # que tome los valores de ITERABLE
            BD.append(dic_iterable)# Guardamos cada nuevo DICCIONARIO
            # en BD.
            
        return BD# La funcion debe retornar el contenido de BD, importante
        # que este RETURN este afuera del FOR

if __name__ == '__main__':
    data = read_csv('Data.csv')# Cuando se ejecute guardara
    # el contenido de la función (RETURN BD) en una variable DATA
    print(data[0])# Podemos imprimir el contenido seta todos o 
    # solo uno de los datos.