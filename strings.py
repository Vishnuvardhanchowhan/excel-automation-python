
print('''Hey brother,
please fill out your information here so we could collect it
and sell your information :) ,
Thanks in advance for making  us money .''')
first_name=input('please enter your first name here:')
lst_name=input('please enter your last name here:')
fav_color=input('what is your favourite colour?')
weight=int(input('what is your weight (in kgs)?'))
birth_year=int(input('what is your birth year in format yyyy? '))
age=2022-birth_year
print(lst_name+' likes '+fav_color)
print(lst_name+" your age is ",age,'years')
print(lst_name, "your weight is ", (1/0.45)*weight,"lbs")
# formatted strings  syntax f'{} xxx yy {}'
# where {} are used as holes in string for variables.
print(f'{first_name}.{lst_name} is a hacker :)')
print(lst_name[1:-1])
print(lst_name.upper())
print(lst_name.find('vishnu'))
print('vishnu' in lst_name)








