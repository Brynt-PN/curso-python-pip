import mod as md
import Charts as ch
import Read_csv_Dic as rd

def run():
    data = rd.read_csv('app/Data.csv')
    #print(data[0])
    data = list(filter(lambda i : i['Continent'] == 'South America', data))
    enc, val = md.get_country_percentage(data)
    ch.generate_pie_chart(enc,val)

if __name__ == '__main__':
    run()