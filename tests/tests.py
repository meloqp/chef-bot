from bot.recipes import normalize_cookware, normalize_ingredients, find_recipes

class TestClass:

    recipes = [
  {
    "name": "Яичница с помидорами",
    "time_to_cook": 10,
    "description": "Быстрый завтрак: нежные яйца с сочными помидорами.",
    "ingredients": ["яйцо", "помидор", "лук"],
    "cookware": ["сковорода"],
    "how_to_cook": "Нарежьте лук и обжарьте на сковороде 2 минуты. Добавьте нарезанные помидоры и готовьте 3 минуты, пока они не станут мягкими. Взбейте яйца с щепоткой соли, влейте в сковороду и аккуратно перемешивайте, пока масса не схватится."
  },
  {
    "name": "Паста с томатным соусом",
    "time_to_cook": 20,
    "description": "Простая паста в домашнем соусе из помидоров и чеснока.",
    "ingredients": ["макароны", "помидор", "чеснок", "лук"],
    "cookware": ["кастрюля", "сковорода"],
    "how_to_cook": "Отварите макароны в кастрюле с подсоленной водой по инструкции на упаковке. Пока они варятся, обжарьте на сковороде нарезанные лук и чеснок 2 минуты, добавьте нарезанные помидоры и тушите 10 минут. Смешайте откинутые макароны с соусом."
  },
  {
    "name": "Салат из огурцов и помидоров",
    "time_to_cook": 5,
    "description": "Свежий летний салат, готовится за несколько минут.",
    "ingredients": ["огурец", "помидор", "лук"],
    "cookware": [],
    "how_to_cook": "Нарежьте огурцы и помидоры, добавьте тонкие кольца лука. Посолите, заправьте ложкой масла, аккуратно перемешайте и сразу подавайте."
  }
    ]

    DEFAULT_COOKWARE = ["сковорода", "кастрюля"]
    EMPTY_USER_INGREDIENTS = []

    ingredients_for_recipe_with_zero_cookwar = ["огурец", "помидор", "лук"]

    def test_empty_user_ingredients(self):
        result = find_recipes(self.EMPTY_USER_INGREDIENTS, self.recipes, self.DEFAULT_COOKWARE)
        assert len(result) == 0

    def test_empty_user_cookware(self):
        result = find_recipes(self.ingredients_for_recipe_with_zero_cookwar, self.recipes, [])
        assert len(result) == 1

    def test_recipe_zero_cookware_with_user_cookware(self):
        result = find_recipes(self.ingredients_for_recipe_with_zero_cookwar, self.recipes, self.DEFAULT_COOKWARE)
        assert len(result) == 1

    def test_normalize_igredients(self):
        assert set(["яйцо", "помидор", "лук"]) == set(normalize_ingredients(["яйца", "томат", "лук"]))

    def test_normalize_cookware(self):
        assert set(["сковорода"]) == set(normalize_cookware(["сковородка"]))