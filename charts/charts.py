import matplotlib.pyplot as plt

def generate_pie_charts():

    encabezado = ['A','B','C']
    valores = [200, 34 ,120]

    fig,cordenada = plt.subplots()
    cordenada.pie(valores, labels = encabezado)
    plt.savefig('pie.png')
    plt.close()





