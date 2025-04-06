from dataclasses import dataclass

@dataclass
class GoProduct:
    Product_number: int
    Product_brand: str
    Unit_sale_price: float
    Quantity:int

    def __eq__(self, other):
        return self.Product_number == other.Product_number

    def __hash__(self):
        return hash(self.Product_number)

    def __str__(self):
        return self.Product_number
