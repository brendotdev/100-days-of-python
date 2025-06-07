def is_authenticated(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if user and user.get("authenticated"):
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper

@is_authenticated
def view_dashboard(*args, **kwargs):
    print("Welcome to your dashboard!")

# Example usage
user1 = {"name": "Alice", "authenticated": True}
user2 = {"name": "Bob", "authenticated": False}

view_dashboard(user=user1)  # Should succeed
view_dashboard(user=user2)  # Should fail
