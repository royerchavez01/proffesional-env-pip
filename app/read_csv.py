import csv

def read_csv(path):
  with open(path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter = ',')
    header = next(reader)
    population_data = []
    
    for row in reader:
      iterable = zip(header, row)
      country_dict = { key: value for key, value in iterable}
      population_data.append(country_dict)
    
  return population_data


if __name__ == '__main__':
  population_data = read_csv('world_data.csv')
  print(population_data[1])
  
#Para ejecutar esto como script se tiene que hacer desde fuera de la carpeta por el path (python ./app/read_csv.py)