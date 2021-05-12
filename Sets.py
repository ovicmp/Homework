# set1 = {9, 2, 4, 6, 8, 22, 14, 16, 21, 20}
# set2 = {1, 2, 3, 5, 6, 9, 22, 14, 17, 22}

set1 = {9, 2, 4, 6, 8, 22, 14, 16, 21, 20}
set2 = {1, 2, 3, 5, 6, 9, 22, 14, 17, 22}

# union
print("Union :", set1 | set2)

# intersection
print("Intersection :", set1 & set2)

# difference
print("Difference :", set1 - set2)

# symmetric difference
print("Symmetric difference :", set1 ^ set2)

# from the Database
cities = [
    ('Berlin', 1234, 4321.1),  # 0 # name, population, surface
    ('Hamburg', 2345, 5432.2),  # 1
    ('Munich', 3456, 6543.3)  # 2
]

# select name, surface from ...
second_cities = [
        ('Berlin', 4321.1),  # 0 # name, population, surface
        ('Hamburg', 5432.2),  # 1
        ('Munich', 6543.3)  # 2
    ]

# 'name': [population, surface]
cities_by_name = {
    # structure for: key: value
    city: [population, surface]
    # condition, what do I need to do ?
    for (city, population, surface) in cities
}
print(cities_by_name)

cities_surface = {
    city: surface
    for city, _, surface in cities
}
print(cities_surface)

cities_populations = {
        city: population
        for city, population, _ in cities
    }
print(cities_populations)

    # city: surface, surface > 5000
big_cities = {
        city: surface
        for city, _, surface in cities
        if surface > 5000
    }
print(big_cities)

big_cities_as_list = [
        surface
        for _, _, surface in cities
        if surface > 5000
    ]
print(big_cities_as_list)

surface_dictionary = {
    city: str(surface) + ' km2'
    for city, _, surface in cities
}
print(surface_dictionary)
