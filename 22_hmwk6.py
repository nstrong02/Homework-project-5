craig = {'first_name': 'Craig', 'last_name': 'Gutz', 'city': 'Aurora'}
print(craig['first_name'])
print(craig['last_name'])
print(craig['city'])
#this is numer 6.1


fav_num = {'stan_num': '4', 'joe_num': '2', 'bob_num': '6', 'dan_num': '1','jim_num': '8'}

print("Stan's favorite number is " + fav_num['stan_num'].title() +".")
print("Joe's favorite number is " + fav_num['joe_num'].title() +".")
print("Bob's favorite number is " + fav_num['bob_num'].title() +".")
print("Dan's favorite number is " + fav_num['dan_num'].title() +".")
print("Jim's favorite number is " + fav_num['jim_num'].title() +".")
#this is number 6.2


define = {'directory': 'A directory is like a list except it hold multiple possiblities in one single option.',
          'list': 'A list is a set that holds one or more items and can be drawn from by other processes',
          'ifelse': 'Ifelse means that If this is true then do this, but if it is not then do this.',
          'ifstatement': 'Like ifelse If Statemnts simply test for if and then if it is it takes action.',
          'boolean': 'A boolean is a test to verify if something is either true or false.'}
print(define['list'])
print(define['ifelse'])
print(define['ifstatement'])
print(define['boolean'])
print(define['directory'])
#this is 6.3


define = {'directory': 'A directory is like a list except it hold multiple possiblities in one single option.',
          'list': 'A list is a set that holds one or more items and can be drawn from by other processes',
          'ifelse': 'Ifelse means that If this is true then do this, but if it is not then do this.',
          'ifstatement': 'Like ifelse If Statemnts simply test for if and then if it is it takes action.',
          'boolean': 'A boolean is a test to verify if something is either true or false.',
          'argument': 'An argument is a value passed to a function or a method when calling it.',
          'loop': 'A loop does its function and uses the information it has been given until it has run out.',
          'class': 'Tells python to make a new kind of thing or category.',
          'attribute': 'A property that a class can have.',
          'while': 'Causes a loop until something stops being true.',}
for word, definition in define.items():
    print("\n" + word.title() + ": " + definition)
#this is 6.4



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

coders = ['phil', 'joe', 'jim', 'dan', 'sarah', 'ron', 'george', 'edward', 'jen']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
#this is 6.6


pets = []
pet = {'animal': 'hamster', 'name': 'ratman', 'owner': 'larry', 'weight': 1, 'diet': 'seeds'}
pets.append(pet)
pet = {'animal': 'dog', 'name': 'cujo', 'owner': 'casedy', 'weight': 24, 'diet': 'children'}
pets.append(pet)
pet = {'animal': 'cat', 'name': 'tiffany', 'owner': 'greg', 'weight': 3, 'diet': 'cat food'}
pets.append(pet)
pet = {'animal': 'cockatiel', 'name': 'screamer', 'owner': 'dilbert', 'weight': 1, 'diet': 'pellets'}
pets.append(pet)
pet = {'animal': 'goat', 'name': 'boy', 'owner': 'daniel', 'weight': 20, 'diet': 'anything'}
pets.append(pet)
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
#this was 6.8


fav_num = {'joe': [64, 255], 'dan': [21, 42, 32], 'rob': [5, 6, 8, 9]}

for name, numbers in fav_num.items():
    print("\n" + name.title() + " doesn't know why he like the following numbers, but he does:")
    for number in numbers:
        print("  " + str(number))
#this was 6.10


glossary = {'Camel': 'A humped horse that spits at people.',
          'Tiger': 'A harmless and oddly striped small cat.',
          'Deer': 'Another horse, but this one has tree horns with no leaves.',
          'Yeti': 'A large, old man who has grow too much hair in order to stay alive in chilly places.',
          'Dragon': 'Kinda like a muppet mixed with a bird and a reptile.',
          'Cow': 'A carnivorous pack hunter with many stomaches in order to eat and digest its many kills.',
          'Snake': 'A living and breathing noodle.',
        }
for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
#this is 6.12


car = input("What kinda car are you folks lookin' for? ")
print("Lemmie see if we got any " + car.title() + ".")
# this is 7.1


party_size = input("How many people in your group? ")
party_size = int(party_size)
if party_size > 8:
    print("Sorry, but there just ain't room for all of y'all at this here moment.")
else:
    print("You can hed on in.")
#this is 7.2


number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")
#this is 7.3


prompt = "\nWhat toppings you want on the pizza?"
prompt += "\nEnter 'quit' when you're done: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  Adding " + topping + " to the pizza.")
    else: break
#this is 7.4

prompt = "\nWhat toppings you want on the pizza?"
prompt += "\nEnter 'quit' when you're done: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  Adding " + topping + " to the pizza.")
    else: break
#this is 7.6

orders = ['salad', 'ham', 'cheesy', 'beef']
done_sandwiches = []

while orders:
    current_sandwich = orders.pop()
    print("I'm making your " + current_sandwich + " sandwich now.")
    done_sandwiches.append(current_sandwich)

print("\n")
for sandwich in done_sandwiches:
    print("I made a " + sandwich + " sandwich.")
#this is 7.8


name_prompt = "\nName? "
place_prompt = "If you could visit any one place in the entire world, where would you go? "
continue_prompt = "\nWant to rethink that? (yes/no) "
responses = {}
while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " wants to go to " + place.title() + ".")
#this is 7.10



def display_message():
    """What am I learning?"""
    msg = "I'm learning about functions."
    print(msg)
display_message()
#this is 8.1


def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Way of Kings')



def make_shirt(size='large', message='I love Python!'):
    """Describe the shirt that's about to be made."""
    print("\nI'm going to make a " + size + " shirt.")
    print('It is gonna say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'I love my dog!')
#this is 8.4



def city_country(city, country):
    """Give me a pair like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())
city = city_country('santiago', 'chile')
print(city)
city = city_country('shanghai', 'china')
print(city)
city = city_country('tokyo', 'japan')
print(city)
#this is 8.6


def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict
title_prompt = "\nWhat album? "
artist_prompt = "The artist? "

print("Enter 'quit' to stop.")
while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
print("\nThanks!")
#this is 8.8



def show_magicians(magicians):
    """Give a list of the magicians."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to the magician's name."""

    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
magicians = ['Houdini', 'Kaito', 'Merlin']
show_magicians(magicians)
print("\n")
make_great(magicians)
show_magicians(magicians)
#this is 8.10


def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a sandwich:")
    for item in items:
        print("  adding " + item + " to your sandwich.")
    print("Sandwich is done.")

make_sandwich('turkey', '', 'lettuce', 'ketchup')
make_sandwich('peanut butter', 'jelly')
make_sandwich('mustard', 'mayo', 'beef', 'american cheese')
#this is 8.12


def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {'manufacturer': manufacturer.title(), 'model': model.title()}
    for option, value in options.items():
        car_dict[option] = value
    return car_dict
my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)
#8.14


"""Functions related to printing 3d models."""
def print_models(unprinted_designs, completed_models):
    """Simulate printing the designs, until there are no more.Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the printed models."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
#8.15



