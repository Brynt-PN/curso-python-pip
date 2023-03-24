import mod as md
import Charts as ch
import Read_csv_Dic as rd
import pandas as pd


def run():
    df = pd.read_csv('Data.csv')#Funcion de Pandas para leer directamente un CSV
    df = df[df['Continent'] == 'Africa']#Filtramos indicando la columna y el valor deseado todo dentro de una lista.
    country = df['Country/Territory'].values #Obtenemos los valores de la fila countries
    Porcentages = df['World Population Percentage'].values #Obtenemos los valores de la fila porsentage
#OBS : El .VALUES hace que retorne como valores.

    '''data = rd.read_csv('Data.csv')
    #print(data[0])
    data = list(filter(lambda i : i['Continent'] == 'South America', data))
    enc, val = md.get_country_percentage(data)'''

    ch.generate_pie_chart(country,Porcentages) #Pasamos los datos para el grafico

if __name__ == '__main__':
    run()