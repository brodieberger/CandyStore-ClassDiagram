from typing import List


class Product:
    """Generic product class."""
    
    def __init__(self, product_id: int, name: str, price: float, description: str):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def display(self):
        return f"{self.name} - ${self.price:.2f}"


class Candy(Product):
    """Specific type of product (inherits Product)."""
    
    def __init__(self, candy_id: int, name: str, price: float, quantity: int, flavor: str):
        super().__init__(candy_id, name, price, description=f"{flavor} flavor")
        self.quantity = quantity
        self.flavor = flavor

    def is_available(self) -> bool:
        """Check if candy is available in stock."""
        return self.quantity > 0

    def reduce_stock(self, amount: int):
        """Reduce the stock quantity by the specified amount."""
        if amount > self.quantity:
            raise ValueError("Not enough stock")
        self.quantity -= amount

    def add_stock(self, amount: int):
        """Increase the stock quantity by the specified amount."""
        self.quantity += amount

    def set_stock(self, amount: int):
        """Set the stock quantity to the specified amount."""
        self.quantity = amount


class Catalog:
    """Collection of all candies."""
    
    def __init__(self):
        self.candies: List[Candy] = []

    def add_candy(self, candy: Candy):
        """Add a candy to the catalog."""
        self.candies.append(candy)

    def search(self, keyword: str) -> List[Candy]:
        """Search for candies by keyword in the name."""
        return [c for c in self.candies if keyword.lower() in c.name.lower()]
