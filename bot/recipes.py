import json
from pathlib import Path
import random

path = Path(__file__).resolve().parent.parent / "data" / "recipes.json"

def load_recipes() -> list[dict]:
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)

def normalize(user_ingredients: list[str]) -> list[str]:
    return [ingredient.lower().strip() for ingredient in user_ingredients]

def find_recipes(user_ingredients: list[str], user_time_to_cook: int , recipes: list[dict]) -> list[dict]:
    found = []
    for recipe in recipes:
        if recipe["time_to_cook"] <= user_time_to_cook and set(recipe["ingredients"]).issubset(set(user_ingredients)):
            found.append(recipe)
    return found


recipes = load_recipes()

if __name__ == "__main__":

    user_ingredients: list[str] = input("Введите ингредиенты через одним сообщением через ',' - ").split(',')
    user_time_to_cook: int = int(input("Введите максимальное время готовки (в минутах)! - "))

    normalize_user_ingredients = normalize(user_ingredients)
    available_recipes = find_recipes(normalize_user_ingredients, user_time_to_cook ,recipes)

    if len(available_recipes) == 0:
        print("Нет подходящих рецептов! :(")
    else:
        print(random.choice(available_recipes))

