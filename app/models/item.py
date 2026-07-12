class Item:
    def __init__(
            self,
            id,
            name,
            quantity,
            price,
            category
    ):
        self.id = id

        self.rename(name)
        self.change_price(price)
        self.change_category(category)

        if quantity < 0:
            raise ValueError(
                "quantity cannot be negative"
            )
        self.quantity = quantity


    def increase_stock(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        
        self.quantity += amount


    def decrease_stock(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        
        if amount > self.quantity:
            raise ValueError("insufficient stock")
        
        self.quantity -= amount


    def change_price(self, new_price):
        if new_price <= 0:
            raise ValueError("new price must be greater than zero")
        
        self.price = new_price


    def rename(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("name must be a string")
        
        name = new_name.strip()

        if not name:
            raise ValueError("name must not be empty")

        self.name = name


    def change_category(self, new_category):
        if not isinstance(new_category, str):
            raise ValueError("category must be a string")

        category = new_category.strip()

        if not category:
            raise ValueError("category must not be empty")

        self.category = category        
