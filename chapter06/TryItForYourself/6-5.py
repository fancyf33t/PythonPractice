#rivers: make a dictionary containing three major rivers and the country each river runs through

major_rivers = {
    'nile river': 'egypt',
    'mississippi river': 'america',
    'amazon river': 'brazil',
}

for key, value in major_rivers.items():
    print(f"\nRiver: {key.title()}")
    print(f"\nCountry: {value.title()}")

print('*********************************')

#ok, now i need to make individual sentences while calling each key:value pair

for river in major_rivers.items():
    print(f"\nThis is a list of major rivers around the world:")
    print(f"\t{key.title()}")
for country in major_rivers.items():
    print(f"\nThey reside in these countries:")
    print(f"\t{value}")
#well that kinda worked......
#will revisit....

