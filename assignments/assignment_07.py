class Food:
    # For @classmethod describe
    # name = 'Lemon'
    # kind = 'fruit'

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


    def describe(self):
        print("{} is a {} kind of food".format(self.name, self.kind))


    # @classmethod
    # def describe(cls):
    #     print("{} is a {} kind of food".format(cls.name, cls.kind))


    # @staticmethod
    # def describe(name, kind):
    #     print("{} is a {} kind of food".format(name, kind))


    def __repr__(self):
        return str(self.__dict__)


class Meat(Food):
    def __init__(self, name):
        super(Meat, self).__init__(name, 'meat')

    def cook(self):
        print("{} is being cooked".format(self.name))


class Fruit(Food):
    def __init__(self, name):
        super(Fruit, self).__init__(name, 'fruit')


    def clean(self):
        print("{} is being cleaned".format(self.name))


food = Food('Orange', 'Fruit')
# @staticmethod describe
# Food.describe('Orange', 'Fruit')
print(food)

pork = Meat('Pork')
pork.describe()
print(pork)

berry = Fruit('Berry')
berry.describe()
print(berry)

# @classmethod describe
# Food.describe()