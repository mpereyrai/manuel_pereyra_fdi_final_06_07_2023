class Dieta:

    def _init_(self, id, Restriction, Restriccion, USD) -> None:
        self.id = id
        self.Restriction = Restriction
        self.Restriccion = Restriccion
        self.USD = USD
        


    def serialize(self):
        return {
            'id': self.id,
            'Restriction': self.Restriction,
            'Restriccion': self.Restriccion,
            'USD': self.USD
        }
