try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["nonexistent"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("New file created.")
except KeyError as error_message:
    print(f"Key error: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
