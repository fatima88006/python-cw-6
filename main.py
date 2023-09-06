person = {
        "name": "Fatima",
        "age": 17,
        "hobbies": ["reading books" , "watching tv" , "playing sport"]
}

print(person.get("name"))
print(person.get("age"))

person["age"]=18
person['country'] = "Spain"
print(person)
print (len(person))
person["hobbies"].append ("playing video gams")
print(person)
def check_hobbies(person):
    if len(person["hobbies"]) >= 3 :
        return"wow you are amazing"
    else:
         return "put more if you can"
print(check_hobbies(person))
