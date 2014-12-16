__author__ = 'Stuart'

#Look up collections.OrderedDict


#create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida': 'FL',
    'California':'CA',
    'New York': "NY",
    'Michigan': 'MI'
}
#create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}
#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-'*10)
print('NY state has: {}\n'
      'OR State has: {}'.format(cities['NY'], cities['OR']))

#print some states
print('-'*10)
print("Michigan's abbreviation is: {}\n"
      "Florida's abbreviation is: {}".format(states['Michigan'], states['Florida']))

#do it by using the state then cities dict
print('-'*10)
print('Michigan has: {}\n'
      'Florida has: {}'.format(cities[states['Michigan']],cities[states['Florida']]))

#print every state abbreviation
print('-'*10)
for state, abbrev in states.items():
    print('{} is abbreviated {}'.format(state,abbrev))

#print every city in state
print('-'*10)
for abbrev,city in cities.items():
    print("{} has the city {}".format(abbrev,city))

#now do both at the same time
print('-'*10)
for state,abbrev in states.items():
    print("{} state is abbreviated {} and has city {}".format(state,abbrev,cities[abbrev]))

#safely get an abbreviation for a state that may not be there
print('-'*10)
state = states.get('Texas', None)
if not state:
    print("Sorry, no Texas")

#get a city with a default value
city = cities.get("TX",'Does not exist')
print("The city for the state 'TX' is {}".format(city))
