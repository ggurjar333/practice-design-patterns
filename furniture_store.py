class AbstractFactory(object):
    def create_chair(self):
        raise NotImplementedError
    
    def create_table(self):
        raise NotImplementedError
    
    def create_desk(self):
        raise NotImplementedError
    
class Chair(object):
    def __init__(self, name):
        self._name = name
    
    def __str__(self) -> str:
        return self._name
    
class Sofa(object):
    def __init__(self, name):
        self._name = name

    def __str__(self) -> str:
        return self._name
    
class Table(object):
    def __init__(self, name):
        self._name = name
    
    def __str__(self) -> str:
        return self._name
    

class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Victorian chair')
    
    def create_sofa(self):
        return Sofa('Victorian sofa')

    def create_table(self):
        return Table('Victorian table')

class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Modern chair')
    
    def create_sofa(self):
        return Sofa('Modern sofa')
    
    def create_table(self):
        return Table('Modern table')
    
class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Futuristic chair')
    
    def create_sofa(self):
        return Sofa('Futuristic sofa')
    
    def create_table(self):
        return Table('Futuristic table')
    

factory_1 = VictorianFactory()
factory_2 = ModernFactory()
factory_3 = FuturisticFactory()
# ''
# Factory 1
print(factory_1.create_chair())
print(factory_1.create_sofa())
print(factory_1.create_table())

# Factory 2
print(factory_2.create_chair())
print(factory_2.create_sofa())
print(factory_2.create_table())

# Factory 3
print(factory_3.create_chair())
print(factory_3.create_sofa())
print(factory_3.create_table())
