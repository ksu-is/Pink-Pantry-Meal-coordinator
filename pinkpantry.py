print("Welcome to Pink Pantry Meal Coordinator!")

print("Enter the ingredients you currently have at home.")
print("Example: chicken, rice, cheese, eggs")

ingredients = input("Enter your ingredients: ").lower()

print("\nSearching for meal suggestions...\n")

if "chicken" in ingredients and "rice" in ingredients:
    print("Meal Suggestion: Chicken and Rice Bowl")
    print("Recipe Idea: Season chicken, cook rice, and combine in a bowl.")
    print("Suggested Side: Steamed vegetables")

elif "eggs" in ingredients and "cheese" in ingredients:
    print("Meal Suggestion: Cheesy Scrambled Eggs")
    print("Recipe Idea: Scramble eggs and melt cheese on top.")
    print("Suggested Side: Toast or fruit")

elif "pasta" in ingredients and "sauce" in ingredients:
    print("Meal Suggestion: Pasta with Sauce")
    print("Recipe Idea: Boil pasta and mix with your favorite sauce.")
    print("Suggested Side: Garlic bread")

elif "bread" in ingredients and "cheese" in ingredients:
    print("Meal Suggestion: Grilled Cheese Sandwich")
    print("Recipe Idea: Toast bread with melted cheese inside.")
    print("Suggested Side: Tomato soup")

elif "tortilla" in ingredients and "cheese" in ingredients:
    print("Meal Suggestion: Cheese Quesadilla")
    print("Recipe Idea: Heat tortilla with melted cheese inside.")

else:
    print("No exact recipe match found.")
    print("Try making a mixed bowl, sandwich, or simple snack with what you have!")
