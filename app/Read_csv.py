# Primero importamos un modulo nativo CSV para poder leer
# archivos .csv
import csv

# Aqui estamos creando una función que imprima en pantalla
# todo el contenido del CSV fila a fila
def read_csv(f):# Parametro es la dirección del archivo
    with open(f,'r') as csv_f:# WITH OPEN para abrin
        reader = csv.reader(csv_f,delimiter=',')# Ejecutamos
        # una función del modulo CSV ".READER" para leer
        # y le pasamos 2 argumentos el contenido abierto 
        # del archivo CSV_F y el DELIMITER (lo que separa
        # los datos en el archivo) en este caso es ','
        # todo esto lo cuardamos en la variable READER
        for i in reader:# Con FOR recorremos READER
            print('***' * 5)# Esto es un separador
            print(i)# Imprimimos linea a linea

# Aqui nos aseguramos de poder usar este archivo como
# MODULO pero tambien como SCRIP decretando que cuando
# se ejecute verifique si se esta ejecutando desde el 
# mismo archivo y si es asi que ejecute la función READ_CSV
if __name__ == '__main__':
    # OBS: 
    # 1 - Cuando des una dirección comiensa con el nombre
    # no con '/' sino no lo detectara.
    # 2 - Ejecuta todo referenciando desde la carpeta abierta
    # en el Visual Estudio, asi el archivo este en una sub 
    # Carpeta por ejemplo ponemos APP/DATA.CSV a pesar de 
    # que este SCRIP esta en la misma carpeta APP.
    # 3 - Recuerda que si tienes el error "FileNotFoundError: [Errno 2] 
    # No such file or directo" y el nombre esta bien referenciado,
    # en el navegador de archivos ve a la carpeta donde se 
    # encuentra el archivo da clic en la ruta y cuando se
    # seleccione escribe "cmd" y da ENTER, se abrira el CMD
    # luego digita "code ." y da ENTER.
    read_csv('app/Data.csv')