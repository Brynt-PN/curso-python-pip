import mod as md
import Charts as ch
import Read_csv_Dic as rd

def run():
    data = rd.read_csv('Data.csv')
    #print(data)
    while True:
        country = input('Ingresa el pais => ')  # Zimbabwe
        data_country = md.population_of_country(data,country)
        #print(data_country)
        if len(data_country) > 0:
            break
        else:
            print('No se encontro el pais')
    x , y = md.get_populations(data_country)
        #print(x)
        #print(y)
    ch.generate_bar_charts(x,y)

if __name__ == '__main__':
    run()