import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__은 객체를 문자열로 표현하기 위해 사용. 해당 특별 메서드가 없으면 <Vector object at 0x10e100070>과 같은 문자열이 출력된다.
    # !r 포맷을 사용하면 결과 값을 반환할 때, ''가 포함되어 출력됨.
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, "test")
print(v1 * 3)