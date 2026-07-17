class Order:
    def __init__(self, id, customer, user, order_date, status):
        self.id = id

        self.customer = customer
        self.user = user
        self.order_date = order_date
        self.status = status

        self.order_items = []



    def add_item(self, order_item):
        self.order_items.append(order_item)


    def remove_item(self, order_item):
        self.order_items.remove(order_item)
    
    
    def mark_paid(self):
        if self.status == "Cancelled":
            raise ValueError(
                "cancelled order cannot be paid"
            )

        self.status = "Paid"
    
    
    def mark_shipped(self):
        if self.status == "Cancelled":
            raise ValueError(
                "cancelled order cannot be shipped"
            )
        
        if self.status != "Paid":
            raise ValueError(
                "only paid orders can be shipped"
            )

        self.status = "Shipped"

    
    def mark_complete(self):
        if self.status == "Cancelled":
            raise ValueError(
                "cancelled order cannot be mark complete"
            )
        
        if self.status != "Shipped":
            raise ValueError("only shipped order can be mark complete")

        self.status = "Complete"
    
    def cancel(self):
        if self.status == "Complete":
            raise ValueError(
                "Completed order cannot be cancelled"
            )
        
        self.status = "Cancelled"
    
    
    def calculate_total(self):
        total = 0

        for order_item in self.order_items:
            total += order_item.subtotal()

        return total