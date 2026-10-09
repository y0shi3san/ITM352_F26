"""Calculate the fewest U.S. coins needed to make an amount of change."""

COINS = (
    (25, "quarter"),
    (10, "dime"),
    (5, "nickel"),
    (1, "penny"),
)


def make_change(amount_cents: int) -> list[tuple[str, int]]:
    """Return each coin name and its count for an amount given in cents."""
    if amount_cents < 0:
        raise ValueError("The amount cannot be negative.")

    result = []
    for value, name in COINS:
        count = 0
        for _ in range(amount_cents // value):
            amount_cents -= value
            count += 1
        if count:
            result.append((name, count))
    return result


def main() -> None:
    try:
        amount_cents = int(input("Enter the change amount in cents: "))
    except ValueError:
        print("Please enter a whole number of cents.")
        return

    try:
        coins = make_change(amount_cents)
    except ValueError as error:
        print(error)
        return

    if not coins:
        print("No change is needed.")
        return

    for name, count in coins:
        if count != 1:
            name = "pennies" if name == "penny" else name + "s"
        print(f"{count} {name}")


if __name__ == "__main__":
    main()