from collections import namedtuple
person = namedtuple("p" , 'name, age , place',defaults=["23","vij"])
y=person("navya")
print(y)