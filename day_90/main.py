def is_authenticated_user(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("authenticated", False):
            return func(*args, **kwargs)
        else:
            print("⛔ Access denied: User not authenticated.")
    return wrapper

@is_authenticated_user
def show_profile(username, **kwargs):
    print(f"👤 Showing profile for {username}")

# Example usage
show_profile("brendotdev", authenticated=True)
show_profile("brendotdev", authenticated=False)
