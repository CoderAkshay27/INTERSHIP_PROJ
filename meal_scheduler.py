import pandas as pd
from datetime import datetime, date

# Global state
meals = []
meal_ids = set()
next_id = 1

def validate_date(date_str: str) -> date:
    """Ensure the date is valid, in YYYY-MM-DD format, and not in the past."""
    try:
        d = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("❌ Invalid date. Use format YYYY-MM-DD with a real calendar date (e.g., 2025-07-21).")
    
    if d < date.today():
        raise ValueError("❌ Date cannot be in the past.")
    return d

def parse_ingredients(ingredients_str: str) -> list:
    """Convert comma-separated ingredients into a clean list."""
    ingredients = [i.strip() for i in ingredients_str.split(",") if i.strip()]
    if not ingredients:
        raise ValueError("❌ Please enter at least one valid ingredient.")
    return ingredients

def add_meal(name: str, date_str: str, ingredients_str: str) -> int:
    """Add a meal to the global list with validated input."""
    global next_id

    if not name.strip():
        raise ValueError("❌ Meal name cannot be empty.")

    meal_date = validate_date(date_str)
    ingredients = parse_ingredients(ingredients_str)

    meal_id = next_id
    next_id += 1

    meals.append({
        "id": meal_id,
        "name": name.strip(),
        "date": meal_date,
        "ingredients": ingredients
    })

    meal_ids.add(meal_id)
    print(f"✅ Meal #{meal_id} added: \"{name.strip()}\" on {meal_date} with {len(ingredients)} ingredient(s).")
    return meal_id

def view_meals():
    """Display all meals sorted by date."""
    if not meals:
        print("ℹ️ No meals scheduled yet.")
        return

    print("\n📅 Scheduled Meals:")
    for meal in sorted(meals, key=lambda m: m["date"]):
        ingredient_list = ", ".join(meal["ingredients"])
        print(f"  {meal['id']}: {meal['name']} — {meal['date']} — Ingredients: {ingredient_list}")
    print()

def generate_ingredients_df() -> pd.DataFrame:
    """Create a DataFrame summarizing ingredient frequency."""
    records = [
        {"ingredient": ingredient, "meal_id": meal["id"]}
        for meal in meals for ingredient in meal["ingredients"]
    ]

    if not records:
        return pd.DataFrame(columns=["ingredient", "count"])

    df = pd.DataFrame(records)
    return df.groupby("ingredient").size().reset_index(name="count")

def export_ingredients_csv(filename="ingredients.csv"):
    """Export the ingredient summary to a CSV file."""
    df = generate_ingredients_df()
    if df.empty:
        print("⚠️ No ingredients to export.")
        return

    try:
        df.to_csv(filename, index=False)
        print(f"✅ Exported {len(df)} ingredients to {filename}")
    except Exception as e:
        print(f"❌ Failed to write CSV: {e}")

def main_menu():
    """Main loop for user interaction."""
    print("🥗 HealthyBites Weekly Meal Scheduler\n")
    while True:
        try:
            command = input("Choose an action [add/view/export/quit]: ").strip().lower()
            if command == "add":
                try:
                    name = input("  Meal name: ").strip()
                    date_str = input("  Date (YYYY-MM-DD): ").strip()
                    ingredients = input("  Ingredients (comma-separated): ").strip()
                    add_meal(name, date_str, ingredients)
                except ValueError as ve:
                    print(ve)
            elif command == "view":
                view_meals()
            elif command == "export":
                export_ingredients_csv()
            elif command == "quit":
                print("👋 Goodbye!")
                break
            else:
                print("❓ Unknown command. Please use add, view, export, or quit.")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Program interrupted. Exiting safely.")
            break

if __name__ == "__main__":
    main_menu()
