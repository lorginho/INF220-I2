def greet(name):
    """
    Greets the user with a personalized message.

    Args:
        name (str): The name of the user to greet.

    Returns:
        str: A string containing the greeting message.
    """
    if name.strip():  # Elimina espacios en blanco
        return f"Hello, {name}!"
    else:
        return "Hello, world!"


if __name__ == "__main__":
    # Elimina espacios en blanco al principio y al final
    user_name = input("Enter your name: ").strip()
    greeting = greet(user_name)
    print(greeting)