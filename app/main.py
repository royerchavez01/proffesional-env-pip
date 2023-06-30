'''Para importar de otra carpeta:

import sys
sys.path.insert(0, ‘/the/folder/path/name-package/’)
Poner ruta de modulo .py
from name-package import name-module'''

import charts
import read_csv
import utils


def run():
  data = read_csv.read_csv('world_data.csv')

  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  labels = list(map(lambda x: x['Country/Territory'], data))
  values = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(labels, values)
 

  #MOSTRAR POBLACION DE UN PAÍS CON EL TIEMPO
  
  country = input('Type country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()