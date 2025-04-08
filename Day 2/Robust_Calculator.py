def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.

    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        # Validate input types
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Invalid input type")

        # Perform operation
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a / b
        elif operator == '%':
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a % b
        elif operator == '**':
            return a ** b
        else:
            raise ValueError("Unsupported operator")

    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Error: {str(e)}"

# Example Usage:
print(calculator(10, 0, "/"))      # Output: Error: Division by zero
print(calculator(10, "five", "+")) # Output: Error: Invalid input type
print(calculator(10, 5, "$"))      # Output: Error: Unsupported operator
print(calculator(5, 3, '**'))      # Output: 125
