# Primero importamos MATPLOTLIB especificamente .PYPLOT este
# modulo sirve para crear graficos con Python.
# OBS:
    # 1- Para importar solo coloca en la terminar
    # PIP INSTALL + "NOMBRE DEL MODULO A IMPORTAR"
    # 2- Si ya instalaste y no reconose o te sale el 
    # error "Modulenotfounderror no module named", ve a 
    # VER => PALETA DE COMANDOS => PYTHON: SELECCION DE INTERPRETE
    # => Ahi selecciona el que a la derecha diga GLOBAL.
import matplotlib.pyplot as plt# Con AS podemos renombrar la
# libreria para no escribir un nombre muy largo, en este caso
# la renombramos PLT.

def generate_bar_charts(name,eje_x,eje_y):# Creamos una funcion para
    # ejecutar los graficos.
    # Definimos cordenadas del eje X
    # Tambien las del eje Y
    figura,cordenadas = plt.subplots()# La funcion 
    # PLT.SUBPLOTS() nos retornara 2 variables que
    # lo mas probable es que sean OBJETOS, la segunda
    # variable son CORDENADAS.
    cordenadas.bar(eje_x,eje_y)# Con la funcion BAR en el
    # en el OBJETO CORDENADAS indicamos que queremos crear
    # un grafico de barras, nos solicitara 2 argumentos
    # valores para el eje x,y.
    plt.savefig(f'Img/{name}.png')
    plt.close()

def generate_pie_chart(encabesado,valor):
    figura,cordenadas = plt.subplots()
    cordenadas.pie(valor,labels=encabesado)# PIE es para grafico
    # circular, nos pido 2 argumentos, primero los valores
    # luego lo que seria el encabezado, de la siguiente forma
    # .PIE(VALORES, LABELS="ENCABESADO"), siempre debe ir 
    # LABELS eh igualarlo a lo que serina los encabesados.
    cordenadas.axis('equal')# Definimos que haga el grafricco en 
    # el centro.
    plt.savefig('Img/pie.png')
    plt.close()
    

# Nuevamente definimos para poder usar este archivo como SCRIP
if __name__ == '__main__':
    eje_x = ['a','b','c']
    eje_y = [100,200,80]
    generate_bar_charts(eje_x,eje_y)
    generate_pie_chart(eje_x,eje_y)





