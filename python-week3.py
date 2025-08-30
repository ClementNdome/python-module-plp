# week3_assignment.py

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is less than 20%, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
if __name__ == "__main__":
    try:
        # Prompt user input
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Call the function
        final_price = calculate_discount(price, discount_percent)

        # Print result
        if discount_percent >= 20:
            print(f"The final price after {discount_percent}% discount is: {final_price}")
        else:
            print(f"No discount applied. The price remains: {final_price}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
