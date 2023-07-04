'''Para importar de otra carpeta:

import sys
sys.path.insert(0, ‘/the/folder/path/name-package/’)
Poner ruta de modulo .py
from name-package import name-module'''

import charts
import read_csv
import utils
import pandas as pd


def run():
  '''
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  labels = list(map(lambda x: x['Country/Territory'], data))
  values = list(map(lambda x: x['World Population Percentage'], data))
  '''

  df = pd.read_csv('world_data.csv')  # Es lo mismo que read_csv.py
  df = df[df['Continent'] == 'Africa']  # Es lo mismo que la linea de filter

  labels = df['Country/Territory'].values # Countries o labels
  values = df['World Population Percentage'].values # percentages o values
  charts.generate_pie_chart(labels, values)
  
   #MOSTRAR POBLACION DE UN PAÍS CON EL TIEMPO
  data = read_csv.read_csv('world_data.csv')
  country = input('Type country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()