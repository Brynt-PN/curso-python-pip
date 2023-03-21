import Read_csv_Dic as rd
import Charts as Ch

data = rd.read_csv('app/Data.csv')
años = ['2022 Population',
        '2020 Population',
        '2015 Population',
        '2010 Population',
        '2000 Population',
        '1990 Population',
        '1980 Population',
        '1970 Population',]

def str_num(x):
    new_str = ''
    num = '1234567890'
    for i in x:
        if i in num:
            new_str += i
    return new_str

def reduccion_data(data_reduc):
    keys = []
    values = []
    new_data = []
    for i in data_reduc:
        for a in i:
            if a in años:
                y = i[a]
                b = str_num(a)
                keys.append(b)
                values.append(y)
        proto_data = zip(keys,values)
        data_iterable = {k : v for k,v in proto_data}
        new_data.append(data_iterable)
    return keys,values

cordenadas = reduccion_data(data)
k,v = cordenadas
Ch.generate_bar_charts(k,v)


