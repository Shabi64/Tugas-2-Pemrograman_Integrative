class MetricBMI:
    def __init__(self, weight, height):
        self._weight = weight  # in kilograms
        self._height = height  # in meters

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    def BMI_Value(self):
        bmi = self._weight / (self._height ** 2)
        return bmi

# Example usage:
person = MetricBMI(weight=70, height=1.75)
print("Weight:", person.weight, "kg")
print("Height:", person.height, "m")
print("BMI:", person.BMI_Value())
