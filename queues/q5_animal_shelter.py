class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    def __str__(self):
        return f"d:{str(self.dogs)} c:{str(self.cats)}"

    def hasDogs(self):
        return len(self.dogs) > 0

    def hasCats(self):
        return len(self.cats) > 0

    def addDog(self, name):
        self.dogs.append(name)

    def addCat(self, name):
        self.cats.append(name)

    def getDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            return self.dogs.pop(0)

    def getCat(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.cats.pop(0)

    def getAnimal(self):
        if len(self.dogs) > 0:
            return self.dogs.pop(0)
        elif len(self.cats) > 0:
            return self.cats.pop(0)
        else:
            return None

def test_empty_shelter():
    ash = AnimalShelter()
    print(ash)
    assert ash.hasDogs() == False
    assert ash.hasCats() == False
    print("test_empty_shelter PASS")

def test_add_dogs():
    ash = AnimalShelter()
    ash.addDog('a')
    print(ash)
    assert ash.hasDogs()
    assert f"{ash}" == "d:['a'] c:[]"
    assert ash.hasCats() == False

    ash.addDog('b')
    print(ash)
    assert f"{ash}" == "d:['a', 'b'] c:[]"    

    print("test_add_dog PASS")


def test_add_cats():
    ash = AnimalShelter()
    ash.addCat('z')
    print(ash)
    assert ash.hasCats()
    assert f"{ash}" == "d:[] c:['z']"
    assert ash.hasDogs() == False

    ash.addCat('x')
    print(ash)
    assert f"{ash}" == "d:[] c:['z', 'x']"    

    print("test_add_cats PASS")


def test_get_dog():
    ash = AnimalShelter()
    ash.addDog('a')
    ash.addDog('b')
    ash.addDog('c')
    print(ash)
    d = ash.getDog()
    assert d == 'a'
    d = ash.getDog()
    assert d == 'b'
    print(ash)
    assert f"{ash}" == "d:['c'] c:[]"
    print("test_get_dog PASS")


def test_get_cat():
    ash = AnimalShelter()
    ash.addCat('z')
    ash.addCat('x')
    ash.addCat('y')
    print(ash)
    d = ash.getCat()
    assert d == 'z'
    d = ash.getCat()
    assert d == 'x'
    print(ash)
    assert f"{ash}" == "d:[] c:['y']"
    print("test_get_cat PASS")


def test_get_animal():
    ash = AnimalShelter()
    ash.addCat('z')
    ash.addCat('x')
    ash.addCat('y')
    ash.addDog('a')
    print(ash)

    a = ash.getAnimal()
    print(ash)
    assert a == 'a'
    assert f"{ash}" == "d:[] c:['z', 'x', 'y']"

    a = ash.getAnimal()
    print(ash)
    assert a == 'z'
    assert f"{ash}" == "d:[] c:['x', 'y']"

    a = ash.getAnimal()
    print(ash)
    assert a == 'x'
    assert f"{ash}" == "d:[] c:['y']"

    print("test_get_animal PASS")

test_empty_shelter()
test_add_dogs()
test_add_cats()
test_get_dog()
test_get_cat()
test_get_animal()
