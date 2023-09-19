spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names=[]
    for i in spicy_foods:
        names.append(i.get("name"))
    return names


def get_spiciest_foods(spicy_foods):
    heat_foods=[]
    for food in spicy_foods:
        if food.get("heat_level") > 5:
            heat_foods.append(food)
    return heat_foods



def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        word_output =""
        word_output += food.get("name") + " " + "(" + food.get("cuisine") + ")" + " " + "|" + " " + "Heat Level: " + ("🌶" * food.get("heat_level"))
        print(word_output)



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine in food.values() :
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        word_output =""
        if food.get("heat_level") > 5:
            word_output += food.get("name") + " " + "(" + food.get("cuisine") + ")" + " " + "|" + " " + "Heat Level: " + ("🌶" * food.get("heat_level"))
            print(word_output)


def get_average_heat_level(spicy_foods):
    food_sum=0
    count=0

    for food in spicy_foods:
        food_sum += food.get("heat_level")
        count += 1
    return int(food_sum / count)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods