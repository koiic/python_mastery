# python dataclass implementation"""    dataclass (cls=None, init=True, repr=True, eq=True, order=False, unsafehash=False, frozen=False)"""import jsonfrom dataclasses import dataclass, field, asdict, astupleages = [1, 28, 34, 420]@dataclass(order=True, unsafe_hash=True, frozen=True)class Animal:    """ creating an animal class"""    name: str    species: str = field(init=False, default='amphibians')    is_mammal: bool    no_of_legs: int = field(hash=False, repr=False, compare=False)@dataclass()class Address:    lat: float    long: float    city: str    country: str@dataclass()class Person:    """ creating a person  class"""    name: str    address: Address    gender: str = field(default='Male')    age: int = field(default_factory=lambda: sum(ages) // len(ages))    is_senior: bool = field(default=False)    def __post_init__(self):        print('---', self.age)        self.is_senior = True if self.age >= 50 else False"""Inheritance"""@dataclass()class A:    x: int = 10    y: int = 20@dataclass()class B(A):    z: int = 30    x: int = 50if __name__ == '__main__':    x = Animal('lion', True, 2)    print(x)    print(x.name, x.is_mammal, x.species)    x2 = Animal('xish', False, 0)    print(x < x2)    print(hash(x))    new_address = Address(23.56, 78.20, 'lagos', 'nigeria')    new_person = Person('calory', new_address, 'male')    print(new_person)    n = asdict(new_person)    print('******', n['address']['lat'])    print(asdict(new_person))    print(astuple(new_person))    json_data = json.dumps(asdict(new_person))    print('^^^^', type(json_data))    print(json.dumps(asdict(new_person)))    b = B()    print('++++', b)