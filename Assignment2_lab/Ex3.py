from pathlib import Path

import pandas as pd


def display_initial_rows(df):
    while True:
        user_input = input("How many initial rows would you like to see? ")
        response = input

        try:
            num_rows = int(response)
            if num_rows < 0:
                print("Please enter a non-negative whole number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        print(df.head(num_rows))
        return


def main():
    csv_path = Path(__file__).with_name("sales_data_test.csv")
    df = pd.read_csv(csv_path)

    try:
        while True:
            display_initial_rows(df)
    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()
