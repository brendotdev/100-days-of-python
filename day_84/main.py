class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        print("Getting Celsius...")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        print("Setting Celsius...")
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero.")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        print("Deleting Celsius...")
        del self._celsius

    @property
    def fahrenheit(self):
        print("Converting to Fahrenheit...")
        return self._celsius * 9 / 5 + 32


temp = Temperature(25)
print(temp.celsius)         # Getting
print(temp.fahrenheit)      # Convert
temp.celsius = 30           # Set
del temp.celsius            # Delete
