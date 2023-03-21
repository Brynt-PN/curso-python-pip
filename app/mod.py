def get_populations(data):
    for i in data:
        data_compres = {
                    '2022':int(i['2022 Population']),
                    '2020':int(i['2020 Population']),
                    '2015':int(i['2015 Population']),
                    '2010':int(i['2010 Population']),
                    '2000':int(i['2000 Population']),
                    '1990':int(i['1990 Population']),
                    '1990':int(i['1990 Population']),
                    '1980':int(i['1980 Population']),
                    '1970':int(i['1970 Population'])
                    }
        keys = list(data_compres.keys())
        values = list(data_compres.values())
        return keys,values

def population_of_country(data, country):
    result = list(filter(lambda item : item['Country/Territory'] == country, data))
    return result

def get_country_percentage(data):
    data_percentage = {i['Country/Territory']:float(i['World Population Percentage']) for i in data}
    return data_percentage.keys(),data_percentage.values()
