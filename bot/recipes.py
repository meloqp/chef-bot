import json
from pathlib import Path
import random

path = Path(__file__).resolve().parent.parent / "data" / "recipes.json"

def load_recipes() -> list[dict]:
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)

def normalize_ingredients(user_ingredients: list[str]) -> list[str]:
    ingredient_synonyms = [{"помидор":["помидоры", "томат", "томаты"]}, 
                           {"яйцо":["яйца", "куриные яйца"]},
                           {"картошка":["картофель", "бульба"]}]
    normalize_user_ingredients = [ingredient.lower().strip() for ingredient in user_ingredients]
    result: list[str] = []
    for user_ingredient in normalize_user_ingredients:
        matched = user_ingredient
        for igredient_synonym in ingredient_synonyms:
            for main_name, variants in igredient_synonym.items():
                if user_ingredient == main_name or user_ingredient in variants:
                    matched = main_name
        result.append(matched)
    return result

def normalize_cookware(user_cookware: list[str]) -> list[str]:
    cookware_synonyms = [{"духовка":["духовой шкаф"]}, 
                         {"сковорода":["сковородка"]}]
    normalize_user_cookware = [cookware.lower().strip() for cookware in user_cookware]
    result: list[str] = []
    for cookware in normalize_user_cookware:
        matched = cookware
        for cookware_synonym in cookware_synonyms:
            for main_name, variants in cookware_synonym.items():
                if cookware == main_name or cookware in variants:
                    matched = main_name
        result.append(matched)
    return result


def find_recipes(
        user_ingredients: list[str],
        recipes: list[dict], 
        cookware: list[str],
        max_time: int | None = None) -> list[dict]:
    found = []
    for recipe in recipes:
        if set(recipe["ingredients"]).issubset(set(user_ingredients)) and (max_time is None or recipe["time_to_cook"] <= max_time) and (set(recipe["cookware"]).issubset(set(cookware)) or len(recipe["cookware"]) == 0):
            found.append(recipe)
    return found


if __name__ == "__main__":

    DEFAULT_COOKWARE = ["сковорода", "кастрюля"]

    recipes = load_recipes()

    user_ingredients: list[str] = input("Введите ингредиенты одним сообщением через ',' - ").split(',')
    user_cookware: list[str] = input("Введите посуду одним сообщением через ',' - ").split(',')
    max_time: int | None = int(input("Введите максимальное время готовки в минутах (если вам все равно на время, то отправьте 0)! - "))
    
    if max_time == 0:
        max_time = None
    user_cookware = [x.strip() for x in user_cookware if x.strip()]

    if len(user_cookware) == 0:
        user_cookware = DEFAULT_COOKWARE

    normalize_user_ingredients = normalize_ingredients(user_ingredients)
    normalize_user_cookware = normalize_cookware(user_cookware)
    
    available_recipes = find_recipes(normalize_user_ingredients, recipes, normalize_user_cookware, max_time)

    if len(available_recipes) == 0:
        print("Нет подходящих рецептов! :(")
    else:
        print(random.choice(available_recipes))

