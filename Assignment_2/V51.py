# Adding V2 to this and adding requirement 2, 8. Add an analytic that shows sales by region and product, showing the percentage of the
# quantity and total sales per region and product. This percentage should be a new
# column in the pivot table.
# Kaili Takara
# November 8th, 2026


import pandas as pd
import ssl
import time


#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context


DATASET_SOURCES = {
    "Sales Data": (
        "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download"
    ),
    "Sales Data 2": (
        "https://docs.google.com/spreadsheets/d/"
        "1-WaMJsVDd4njhRzQnvByh61WbLHL8m_sB0k2E5mnFTo/export?format=csv&gid=0"
    ),
}


def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Numbner of rows: {len(df)}")
        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None



def display_initial_rows(data):
    """Ask the user how many initial rows to show and print them.

    Accepts a positive integer or 'all'. Invalid entries are reported and
    the user is re-prompted.
    """
    while True:
        response = input(
            f"\nHow many initial rows would you like to see? "
            f"(1-{len(data)}, or 'all'): "
        ).strip().lower()

        if response == "all":
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f"Invalid input '{response}'. Please enter a whole number or 'all'.")
            continue

        if num_rows < 1:
            print("Please enter a number greater than 0.")
            continue

        if num_rows > len(data):
            print(f"Only {len(data)} rows available; showing all of them.")
            continue

        print(data.head(num_rows))
        return


def show_employees_by_region(data):
    """Print the number of unique employees in each sales region."""
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("\nNumber of employees by region:")
    print(counts.to_string())


def get_user_selection(options, prompt, required=False, single=False):
    """Prompt for comma-separated option numbers and return the chosen options.

    Re-prompts on invalid input. An empty entry returns [] unless required.
    """
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))
        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected


def generate_custom_pivot_table(data):
    """Interactively build and display a pivot table."""
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns available to aggregate.")
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table)


def show_average_sales_by_region(data):
    """Pivot average sales (quantity * unit_price) by region, with state and sale type sub-columns."""
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))


def show_sales_by_region_and_product(data):
    """Show quantities, sales, and each product's share of its region totals."""
    product_column = next(
        (column for column in ("product", "produce_name") if column in data.columns),
        None,
    )
    required = ["sales_region", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if product_column is None:
        missing.append("product or produce_name")
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return None

    numeric_values = {}
    invalid_rows = pd.Series(False, index=data.index)
    for column in ("quantity", "unit_price"):
        cleaned_values = (
            data[column]
            .astype("string")
            .str.replace(r"[$,]", "", regex=True)
            .str.strip()
        )
        converted_values = pd.to_numeric(cleaned_values, errors="coerce")
        invalid_rows |= converted_values.isna()
        numeric_values[column] = converted_values

    if invalid_rows.any():
        print(
            f"Warning: Skipping {invalid_rows.sum()} row(s) with missing or "
            "invalid quantity or unit_price values."
        )
        for column in ("quantity", "unit_price"):
            invalid_values = numeric_values[column].isna()
            if invalid_values.any():
                examples = data.loc[invalid_values, column].head(5).tolist()
                print(f"  {column} examples: {examples}")

    valid_rows = ~invalid_rows
    if not valid_rows.any():
        print("Cannot calculate sales: no rows have valid quantity and unit_price values.")
        return None

    sales = data.loc[valid_rows].assign(
        quantity=numeric_values["quantity"].loc[valid_rows],
        unit_price=numeric_values["unit_price"].loc[valid_rows],
    )
    sales["total_sales"] = sales["quantity"] * sales["unit_price"]
    pivot_table = pd.pivot_table(
        sales,
        index=["sales_region", product_column],
        values=["quantity", "total_sales"],
        aggfunc="sum",
    )
    region_totals = pivot_table.groupby(level="sales_region")[["quantity", "total_sales"]].transform("sum")
    quantity_totals = region_totals["quantity"].where(region_totals["quantity"].ne(0))
    sales_totals = region_totals["total_sales"].where(region_totals["total_sales"].ne(0))
    pivot_table["quantity_pct_of_region"] = (
        pivot_table["quantity"].div(quantity_totals).mul(100)
    )
    pivot_table["sales_pct_of_region"] = (
        pivot_table["total_sales"].div(sales_totals).mul(100)
    )

    print("\nSales by region and product (percentages are each product's share of its region):")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    return pivot_table


def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Average sales by region, by state and sale type", show_average_sales_by_region),
    ("Sales by region and product with percentages", show_sales_by_region_and_product),
    ("Exit the program", exit_program),
)


def display_menu():
    """Show the menu and return a valid selection as an index into menu_options."""
    while True:
        print("\nSales Data Menu")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")


def main():
    dataset = get_user_selection(
        list(DATASET_SOURCES),
        "\nSelect the sales data to load:",
        required=True,
        single=True,
    )[0]
    sales_data = load_csv(DATASET_SOURCES[dataset])

    if sales_data is None:
        return

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]
            action(sales_data)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()