def build_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

build_profile(name="Brendan", age=28, role="Backend Developer")
