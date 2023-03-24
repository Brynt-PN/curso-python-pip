import requests as rqs

def get_categories():
    r = rqs.get('https://api.escuelajs.co/api/v1/categories')
    categories = r.json()
    for categories in categories:
        print(categories['name'])

#Conseguir un diccionario de ID : NAME de la categoria.
    '''id_name = {categories['id'] : categories['name'] for categories in categories}
    print(id_name)'''