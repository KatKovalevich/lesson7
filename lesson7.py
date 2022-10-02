# задача 1

class Matrix:

    def__init__(self, my_mx):
        self.my_mx = my_mx

    def __str__(self):
        return '\n'.join('\t'.join(map(str,row)) for row in self.my_mx)

    def__add__(self, other):
        for i in range(len(self.my_mx)):
            for j in range(len(other.my_mx[i])):
                self.my_mx[i][j] = self.my_mx[i][j] + other.my_mx[i][j]
        return Matrix.__str__(self)


# задача 2

class Сlothes:
    def__init__(self, size, hight):
     self.size = size
     self.hight = hight

    def get_square_c(self):
        return self.size / 6.5 + 0.5

    def get_square_j(self):
        return self.hight * 2 + 0.3

 @property
    def get_square_full(self):
        return str(f'Площадь ткани на одежду \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_c}'

class Jacket(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_j}'


# задача 3

class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def__add__(self, other):
        return self.amount + other.amount}

    def__sub__(self, other):
        return self.amount - other.amount if (self.amount - other.amount) > 0 else print('Операция невозможна!')

    def__mul__(self, other):
        return self.amount * other.amount

    def__truediv__(self, other):
        return self.amount // other.amount



