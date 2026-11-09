tacos={
    "tortillas":["maiz", "harina"],
    "guisos":["bisteck","tripa","pastor"]
}
print(f"Tu has ordenado unos tacos de{tacos['guisos'][0]}")
print(f"En tortillas de {tacos['tortillas'][1]}")
#enu de usuarios
user = {
    "charly":{
        "firstname":"carlos",
        "middlename":"antonio",
        "lastname":"tovar garcia",
        "location":"Mexico",
        "age":24
    },
    "Thefresh":{
        "firstname":"Angel",
        "middlename":"Ubaldo",
        "lastname":"Abundis Gonzalez",
        "location":"Mexico",
        "age":24
    }
}
for user,user_info in user.items():
    full_name = f"{user_info["firstname"]}{user_info["middlename"]}{user_info["lastname"]}"
    print(full_name)