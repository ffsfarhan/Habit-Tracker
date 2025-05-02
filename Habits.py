import json
from datetime import date
import os

habits_file = "habits.json"

if os.path.exists(habits_file):
    with open(habits_file, "r") as f:
        habits = json.load(f)
else:
    habits = {}


def save_habits():
    with open(habits_file, "w") as f:
        json.dump(habits, f)


def add_habits():
    name = input("Enter habit name: ").lower()
    if name not in habits:
        habits[name] = []
        print(f"Habit '{name}' added successfully!")
    else:
        print(f"Habit '{name}' already exists.")


def mark_done():
    if not habits:
        print("No habits available to mark as done. Please add habits first.")
        return

    name = input("Enter habit name to mark as done: ").lower()
    if name not in habits:
        print(f"'{name}' is not a valid habit. Please add it first.")
        return

    today = str(date.today())
    if today not in habits[name]:
        habits[name].append(today)
        print(f"Marked '{name}' as done for {today}.")
    else:
        print(f"'{name}' is already marked as done today.")


def view_habits():
    if not habits:
        print("No habits to display.")
        return

    for h, days in habits.items():
        count = len(days)
        if count == 0:
            print(f"{h}: Not done yet")
        elif count == 1:
            print(f"{h}: Done on 1 day - {days}")
        else:
            print(f"{h}: Done on {count} days - {days}")


def reset_data():
    global habits
    habits = {}
    with open(habits_file, "w") as f:
        json.dump(habits, f)
    print("Habit data has been reset.")


def main_menu():
    while True:
        print("\n--- Habit Tracker Menu ---")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habit Progress")
        print("4. Reset Habit Data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_habits()
        elif choice == "2":
            mark_done()
        elif choice == "3":
            view_habits()
        elif choice == "4":
            reset_data()
        elif choice == "5":
            save_habits()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
