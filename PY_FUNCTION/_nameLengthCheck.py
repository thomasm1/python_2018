given_name = "Thomas"
middle_names = "Milton"
family_name = "Maestas"

 #todo: calculate how long this name is
name_length = (given_name + ' ' + middle_names + ' ' + family_name)
name_length = len(name_length)

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)
