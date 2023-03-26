# Recuerda que los DOCKERFILE son como una clase a partir de la cual se crea el contenedor

# Aqui estamos indicando con que verción de Python queremos que se haga el Contenedor
FROM python:3.8

# Aqui creamos una carpeta dentro del contenedor
WORKDIR /app

# Como una buena practica podemos copiar nuestros Requirements del proyecto usando COPY (BUENAS PRACTICAS)
COPY requirements.txt /app/requirements.txt
#    ORIGEN           CONTENEDOR
#  El espacio (' ') el ORIGEN y el CONTENEDOR es lo que indica COPIAR 

# Tambien podemos indicarle que corra el comando para instalar las dependecias (Requirements) con RUN
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt
# --NO-CACHE-DIR sirve para decir que no instale el CACHE (BUENAS PRACTICAS)
# --UPGRADE es para que si encuentre una actualización la aplique (BUENAS PRACTICAS)

# Por ultimo copiamos todo lo que esta dentro de la carpeta
COPY . /app
# EL ('.') significa ubicate en la misma carpeta y copia todo

# Crearemos un comando para que el contenedor se mantenda en ejecución constante (Esta escrito en BASH)
CMD bash -c 'while true; do sleep 1; done'
# Usamos CMD para indicar usar un comando (No estoy seguro), el comando lo uso tal cual lo indican en el curso.