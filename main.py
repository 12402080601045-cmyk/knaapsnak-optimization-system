
def knapsack_optimization():
    print("=" * 45)
    print("       KNAPSACK OPTIMISATION SYSTEM")
    print("=" * 45)

    try:
        n = int(input("Enter number of items: "))

        if n < 0 or n > 1000:
            print("Invalid number of items!")
            return

        capacity = int(input("Enter knapsack capacity: "))

        if capacity < 0 or capacity > 100000:
            print("Invalid capacity!")
            return

        if (n + 1) * (capacity + 1) > 5000000:
            print("Problem size too large!")
            return

        weights = []
        values = []

        for i in range(n):
            print(f"\nEnter details for Item {i + 1}")

            weight = int(input("Enter weight: "))
            value = int(input("Enter value: "))

            if weight < 0 or value < 0:
                print("Weight and value cannot be negative!")
                return

            weights.append(weight)
            values.append(value)

    except ValueError:
        print("Invalid input! Please enter integers only.")
        return

    # Dynamic Programming Table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            dp[i][w] = dp[i - 1][w]

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] +
                    dp[i - 1][w - weights[i - 1]]
                )

    # Maximum Profit
    maximum_profit = dp[n][capacity]

    # Backtracking to find selected items
    selected_items = []
    remaining = capacity
    total_weight = 0

    for i in range(n, 0, -1):
        if dp[i][remaining] != dp[i - 1][remaining]:
            selected_items.append(i)
            total_weight += weights[i - 1]
            remaining -= weights[i - 1]

    selected_items.reverse()

    # Display Results
    print("\n" + "=" * 45)
    print("           OPTIMISATION RESULT")
    print("=" * 45)

    print("Maximum Profit:", maximum_profit)
    print("\nSelected Items:")

    if not selected_items:
        print("No items selected.")
    else:
        print("Item\tWeight\tValue")

        for item in selected_items:
            print(
                f"{item}\t{weights[item-1]}\t{values[item-1]}"
            )

    print("Total Selected Items:", len(selected_items))
    print("Total Weight:", total_weight)
    print("Remaining Capacity:", capacity - total_weight)
    print("Total Profit:", maximum_profit)

    print("=" * 45)


if __name__ == "__main__":
    knapsack_optimization()
