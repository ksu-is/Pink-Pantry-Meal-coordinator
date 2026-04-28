print("Welcome to Pink Pantry Meal Coordinator!")

ingredients = input("Enter ingredients you have (separated by commas): ").lower()

if "chicken" in ingredients and "rice" in ingredients:
    print("Meal Suggestion: Chicken and Rice Bowl")

elif "eggs" in ingredients and "cheese" in ingredients:
    print("Meal Suggestion: Cheesy Scrambled Eggs")

elif "pasta" in ingredients and "sauce" in ingredients:
    print("Meal Suggestion: Pasta with Sauce")

else:
    print("Try making a simple meal with what you have available!")
