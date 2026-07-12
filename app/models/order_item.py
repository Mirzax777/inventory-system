class OrderItem:
    def __init__(self, id, item, quantity, unit_price):
        self.id = id
        self.item = item

        self.change_quantity(quantity)
        self.change_unit_price(unit_price)

    def change_quantity(self, new_quantity):
        if new_quantity <= 0:
            raise ValueError(
                "quantity must be greater than zero"
            )

        self.quantity = new_quantity

    def change_unit_price(self, new_price):
        if new_price <= 0:
            raise ValueError(
                "price must be greater than zero"
            )

        self.unit_price = new_price

    def subtotal(self):
        return self.quantity * self.unit_price