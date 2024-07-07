# write a complex to represent complex numbers,along with overload operator '+' and'*' which adds multiplies them
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
c1 = Complex(3, 2)
c2 = Complex(1, 7)

c3 = c1 + c2
c4 = c1 * c2

print("Sum:", c3)
print("Product:", c4)