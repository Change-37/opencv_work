class Parent:
    num = 0
    def __init__(self, num) -> None:
        self.num = num
        print('Parent class called')

class Child(Parent):
    def __init__(self, num) -> None:
        super().__init__(num)
        print('Child class called')

    def displayValue(self):
        print('num :', self.num)

cd = Child(37)
cd.displayValue()