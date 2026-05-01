# Pink Pantry Meal Coordinator
# Sprint 3 Final Version

recipes = {
    "Chicken Rice Bowl": {
        "calories": 520,
        "ingredients": {
            "chicken": "1 cooked chicken breast",
            "rice": "1 cup cooked rice",
            "broccoli": "1/2 cup broccoli",
            "soy sauce": "1 tablespoon soy sauce"
        },
        "alternatives": {
            "broccoli": "spinach, peas, or mixed vegetables",
            "soy sauce": "teriyaki sauce, hot sauce, or garlic seasoning"
        },
        "steps": "Cook rice, add chicken and broccoli, then season with soy sauce."
    },

    "Cheesy Scrambled Eggs": {
        "calories": 350,
        "ingredients": {
            "eggs": "2 large eggs",
            "cheese": "1/4 cup shredded cheese",
            "milk": "2 tablespoons milk",
            "bread": "1 slice toast"
        },
        "alternatives": {
            "milk": "water, cream, or almond milk",
            "bread": "tortilla, biscuit, or English muffin"
        },
        "steps": "Whisk eggs with milk, cook in a pan, add cheese, and serve with toast."
    },

    "Pasta with Meat Sauce": {
        "calories": 650,
        "ingredients": {
            "pasta": "2 cups cooked pasta",
            "ground beef": "1/2 cup cooked ground beef",
            "sauce": "1/2 cup tomato sauce",
            "parmesan": "2 tablespoons parmesan"
        },
        "alternatives": {
            "ground beef": "turkey, sausage, lentils, or mushrooms",
            "parmesan": "mozzarella, cheddar, or no cheese"
        },
        "steps": "Boil pasta, cook beef, mix with sauce, and top with parmesan."
    },

    "Grilled Cheese and Tomato Soup": {
        "calories": 580,
        "ingredients": {
            "bread": "2 slices bread",
            "cheese": "2 slices cheese",
            "butter": "1 tablespoon butter",
            "tomato soup": "1 cup tomato soup"
        },
        "alternatives": {
            "butter": "mayo, olive oil, or cooking spray",
            "tomato soup": "chicken soup, vegetable soup, or marinara sauce"
        },
        "steps": "Butter bread, add cheese, grill until golden, and serve with warm soup."
    },

    "Chicken Quesadilla": {
        "calories": 610,
        "ingredients": {
            "tortilla": "1 large tortilla",
            "chicken": "1/2 cup cooked chicken",
            "cheese": "1/2 cup shredded cheese",
            "salsa": "2 tablespoons salsa"
        },
        "alternatives": {
            "salsa": "hot sauce, sour cream, or diced tomatoes"
        },
        "steps": "Fill tortilla with chicken and cheese, heat until crispy, and serve with salsa."
    },

    "Tuna Salad Sandwich": {
        "calories": 430,
        "ingredients": {
            "tuna": "1 can tuna",
            "mayo": "1 tablespoon mayo",
            "bread": "2 slices bread",
            "lettuce": "1 handful lettuce"
        },
        "alternatives": {
            "mayo": "Greek yogurt, ranch, or mustard",
            "lettuce": "spinach, pickles, or cucumber"
        },
        "steps": "Mix tuna with mayo, place on bread, add lettuce, and serve."
    },

    "Loaded Baked Potato": {
        "calories": 500,
        "ingredients": {
            "potato": "1 large baked potato",
            "cheese": "1/4 cup shredded cheese",
            "bacon": "2 strips bacon",
            "sour cream": "2 tablespoons sour cream"
        },
        "alternatives": {
            "bacon": "ham, turkey bacon, or beans",
            "sour cream": "Greek yogurt, ranch, or butter"
        },
        "steps": "Bake potato, cut it open, and top with cheese, bacon, and sour cream."
    },

    "Veggie Fried Rice": {
        "calories": 480,
        "ingredients": {
            "rice": "1 cup cooked rice",
            "eggs": "1 large egg",
            "mixed vegetables": "1 cup mixed vegetables",
            "soy sauce": "1 tablespoon soy sauce"
        },
        "alternatives": {
            "mixed vegetables": "peas, carrots, corn, or broccoli",
            "soy sauce": "teriyaki sauce, salt, or garlic seasoning"
        },
        "steps": "Cook vegetables, scramble egg, add rice, and season with soy sauce."
    },

    "Turkey Avocado Wrap": {
        "calories": 540,
        "ingredients": {
            "tortilla": "1 large tortilla",
            "turkey": "4 slices turkey",
            "avocado": "1/2 avocado",
            "lettuce": "1 handful lettuce"
        },
        "alternatives": {
            "turkey": "chicken, ham, tuna, or tofu",
            "avocado": "hummus, mayo, or cheese"
        },
        "steps": "Layer turkey, avocado, and lettuce in tortilla, then roll into a wrap."
    },

    "Breakfast Yogurt Bowl": {
        "calories": 390,
        "ingredients": {
            "yogurt": "1 cup yogurt",
            "granola": "1/2 cup granola",
            "banana": "1 sliced banana",
            "honey": "1 tablespoon honey"
        },
        "alternatives": {
            "granola": "cereal, nuts, or crushed crackers",
            "honey": "maple syrup, peanut butter, or cinnamon"
        },
        "steps": "Add yogurt to a bowl, then top with granola, banana, and honey."
    }
}


def get_user_ingredients():
    print("Welcome to Pink Pantry Meal Coordinator!")
    print("Enter ingredients you have, separated by commas.")
    print("Example: chicken, rice, cheese, eggs, bread")
    user_input = input("\nYour ingredients: ")

    ingredient_list = user_input.split(",")
    cleaned_ingredients = []

    for item in ingredient_list:
        cleaned_ingredients.append(item.strip().lower())

    return cleaned_ingredients


def find_matching_recipes(user_ingredients):
    matches = []

    for recipe_name, recipe_info in recipes.items():
        matched = []
        missing = []

        for ingredient in recipe_info["ingredients"]:
            if ingredient in user_ingredients:
                matched.append(ingredient)
            else:
                missing.append(ingredient)

        score = len(matched)

        if score > 0:
            matches.append({
                "name": recipe_name,
                "score": score,
                "total": len(recipe_info["ingredients"]),
                "matched": matched,
                "missing": missing
            })

    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches


def show_recipe_details(match):
    recipe_name = match["name"]
    recipe = recipes[recipe_name]

    print("\n" + "=" * 50)
    print("Best Meal Suggestion:", recipe_name)
    print("Estimated Calories:", recipe["calories"])
    print("Ingredient Match:", str(match["score"]) + "/" + str(match["total"]))

    print("\nIngredients and Measurements:")
    for ingredient, amount in recipe["ingredients"].items():
        print("- " + ingredient.title() + ": " + amount)

    print("\nRecipe Steps:")
    print(recipe["steps"])

    if len(match["missing"]) > 0:
        print("\nMissing Ingredients and Alternatives:")
        for missing_item in match["missing"]:
            if missing_item in recipe["alternatives"]:
                print("- Missing " + missing_item.title() + ": try " + recipe["alternatives"][missing_item])
            else:
                print("- Missing " + missing_item.title() + ": no alternative listed")
    else:
        print("\nYou have every ingredient needed for this recipe!")


def show_results(matches):
    if len(matches) == 0:
        print("\nNo recipe matches found.")
        print("Try entering ingredients like chicken, rice, eggs, cheese, pasta, bread, or tortilla.")
    else:
        print("\nTop Recipe Matches:")

        for i in range(min(3, len(matches))):
            match = matches[i]
            print(str(i + 1) + ". " + match["name"] + " - " +
                  str(match["score"]) + "/" + str(match["total"]) + " ingredients matched")

        show_recipe_details(matches[0])


def main():
    user_ingredients = get_user_ingredients()
    matches = find_matching_recipes(user_ingredients)
    show_results(matches)


main()
