import store
from fastapi import FastAPI #Si estando en un entorno virtual ENV_ no te lee el codigo es por que el interprete esta en global por lo tanto las dependencias que instalaste en tu entorno no las detecta, lo que debes hacer es ir an VER, luego a PALETA DE COMANDOS, luego coloca en buscar y recuerda que al activar un entorno podras ver la ruta por lo general es ENV_EJEM/BIN/PYTHON3, esto significa que debes entrar a la carpeta con el nombre del entrono, luego a BIM y al final seleccionar PYTHON3 y esa sera la dirección correcta del interprete de tu entorno virtual ENV.
from fastapi.responses import HTMLResponse #Importamos esta dependencia para devolver HTML en nuestro servido.


app = FastAPI() #Creamos una instacia de la APP (Es crear un objeto en base a una Clase, consultar la POO)
#OBS: Luego en la termina usaremos UVICOR para lanzar nuestro servidor a internet usando la siguiente sintaxis.
# UVICORN MAIN:APP --RELOAD
# (COMANDO)-(NOMBRE DEL ARCHIVO Y NOMBRE DE LA APP)-(REGLA DEL COMANDO)
# --RELOAD es para que el servidor se actualize automaticamente tras cualquier cambio

'*****************************************************'
@app.get('/') #Esto es un decorador, usamos un '@' luego el APP antes definido y el metodo GET, por ultimo entrelos parentesis la ruta que usamos para mostrar la función definida a continuación
def get_list(): #Devolver una lista, con esto definimos que nos devolvera en la pagina la API
    return [1,2,3] # Esto es lo que nos retorna
'*****************************************************'
@app.get('/contac', response_class=HTMLResponse) #Aqui ponemos otra dirección y agregamos una clase que devuelve HTML, RESPONSE_CLASS= nos dice que clase de info nos retornara
def get_list():
    return '''
            <h1>Hola soy una Pagina</h>
            <p>Soy un parrafo</p>
    '''
'*****************************************************'

def run():
    store.get_categories()

if __name__ == '__main__':
    run()