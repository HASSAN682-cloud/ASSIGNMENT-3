def calculate_discount(price, discount_percentage):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percentage: The discount percentage (e.g., 10 for 10%).

  Returns:
    The final price after applying the discount, or the original price if no discount is applied.
  """
  if discount_percentage > 0:
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage (e.g., 10 for 10%): "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price != original_price:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"The original price is: {original_price}")