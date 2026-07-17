from app.models.order import Order
from app.models.order_item import OrderItem

class OrderService:

    def create_order(
        self, 
        id, 
        customer, 
        user, 
        order_date
    ):
        return Order(
            id=id,
            customer=customer,
            user=user,
            order_date=order_date,
            status="Pending"
        )
    
    def add_item(
        self,
        order,
        item,
        quantity
    ):
        order_item = OrderItem(
            id=len(order.order_items) + 1,
            item=item,
            quantity=quantity,
            unit_price=item.price
        )

        order.add_item(order_item)

        return order_item