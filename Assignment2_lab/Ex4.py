from pathlib import Path

import pandas as pd


def display_initial_rows(df):
    while True:
        user_input = input("How many initial rows would you like to see? ")

        try:
            num_rows = int(user_input)
            if num_rows < 0:
                print("Please enter a non-negative whole number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        print(df.head(num_rows))
        return


def show_employees_by_region(df):
    employee_counts = (
        df.groupby("sales_region")["employee_id"]
        .nunique()
        .sort_index()
    )
    print(employee_counts)


def exit_program():
    print("Exiting the program.")


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Exit the program", exit_program),
)


def display_menu():
    print("\nSales Data Menu")
    for index, (description, _) in enumerate(menu_options):
        print(f"{index}: {description}")
    return input("Select an option: ")


def main():
    csv_path = Path(__file__).with_name("sales_data_test.csv")
    df = pd.read_csv(csv_path)

    while True:
        selection = display_menu()
        try:
            option_index = int(selection)
        except ValueError:
            print("Invalid selection. Please enter a menu number.")
            continue

        if not 0 <= option_index < len(menu_options):
            print(f"Please enter a number from 0 to {len(menu_options) - 1}.")
            continue

        action = menu_options[option_index][1]
        if action is exit_program:
            action()
            break
        action(df)


if __name__ == "__main__":
    main()