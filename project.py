import csv
import json
from matplotlib import pyplot as plt
import numpy as np

pop = open('data/Global_annual_population.csv')
pop_usa = open('data/POPTOTUSA647NWDB.csv')
reader = csv.reader(pop)
reader2 = csv.reader(pop_usa)
pop = list(reader)
pop_usa = list(reader2)
pop = pop[1:]
pop_usa = pop_usa[1:]
population = []
years = []
population_usa = []
for year in pop:
    years.append(int(year[0]))
    population.append(int(float(year[1])*1000))
for year in pop_usa:
    population_usa.append(int(float(year[1])//1000000))
plt.figure('Global and USA Population Since 1960')
plt.title('Global and USA Population Since 1960')
plt.plot(years, population, 'b', label='Global Population in Millions')
plt.plot(years, population_usa, 'k', label='US Population in Millions')
plt.xlabel('Year')
plt.legend()
plt.xticks(np.arange(min(years),max(years),step=20))
plt.yticks(np.arange(min(population_usa),max(population),500))
plt.ylabel('Global vs US Population in Millions')
plt.show()

pokemon = open('data/pokedex.json')
reader = pokemon.read()
pokemon_json=json.loads(reader)
pokemon_list=pokemon_json['pokemon']
types={'Grass':0, 'Fire':0, 'Water':0}
for i in pokemon_list:
    for type in i['type']:
        if type in types:
            types[type]+=1
pokemon_x = types.keys()
pokemon_y = types.values()
plt.figure('# of Pokemon for the 3 Main Types')    
plt.title('# of Pokemon for the 3 Main Types')
plt.bar(pokemon_x, pokemon_y, width=0.5)
plt.xlabel('Type')
plt.ylabel('Number of Pokemon')
plt.show()