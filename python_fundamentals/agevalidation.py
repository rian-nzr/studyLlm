def validate_age(age):
    if age < 0:
        return "Age cannot be negative."
    elif age > 90:
        return "Age is way too old."
    elif age < 18:
        return "Age is too young."
    elif age < 25:
        return "Age is young."
    else:
        return "Age is within the valid range."
# Example usage
age = int(input("Enter your age: "))
result = validate_age(age)
print(result)