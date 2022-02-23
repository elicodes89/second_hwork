united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

united_kingdom[1]['capital'] = "Cardiff"
print(united_kingdom[1]["capital"])

united_kingdom.append({'name':'Northern Ireland','capital': 'Belfast', 'population': 1811})
print(united_kingdom)


totalPopu = 0

for country in united_kingdom:
    population = country['population']
    totalPopu += population

print(totalPopu)


