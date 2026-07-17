from app.models.item import Item
from app.models.customer import Customer
from app.models.order_item import OrderItem
from app.models.order import Order

from app.services.order_service import OrderService

keyboard = Item(
    1, "Keyboard Gaming", 100, 50, "Gaming"
)

table = Item(
    2, "Table AX12", 10, 100, "Furniture"
)

customer_mirza = Customer(
    1, "Mirza", "Padang", "0812345678"
)

order_service = OrderService()

mirza_order = order_service.create_order(
    id=1,
    customer=customer_mirza,
    user="Admin",
    order_date="2026-07-17"
)


order_service.add_item(
    mirza_order,
    keyboard,
    5
)

order_service.add_item(
    mirza_order,
    table,
    1
)

print(mirza_order.order_items)

for line in mirza_order.order_items:
    print(
        line.id,
        line.item.name,
        line.quantity,
        line.unit_price
    )
