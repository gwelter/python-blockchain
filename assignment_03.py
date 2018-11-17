persons = [
    {
        "name": "Guilherme",
        "age": 27,
        "hobbies": ["Gaming", "Reading", "Bike"]
    },
    {
        "name": "Gustavo",
        "age": 19,
        "hobbies": ["Gaming", "Excercices", "Comics"]
    },
    {
        "name": "Mirian",
        "age": 29,
        "hobbies": ["Reading", "Volleyball"]
    }
]
print(persons)

names = [person["name"] for person in persons]
print(names)

print(all([person["age"] > 20 for person in persons]))

persons_copy = [person.copy() for person in persons]
persons_copy[0]["name"] = "Eloi"
print(persons[0]["name"])
print(persons_copy[0]["name"])

person_1, person_2, person_3 = persons

print(person_1)
print(person_2)
print(person_3)
