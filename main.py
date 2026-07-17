from app.models.item import Item
from app.models.customer import Customer
from app.models.order_item import OrderItem
from app.models.order import Order
from app.models.transaction import StockTransaction


print("=" * 50)
print("CREATE ITEMS")
print("=" * 50)

keyboard = Item(
    id=1,
    name="Gaming Keyboard",
    quantity=10,
    price=20,
    category="Electronic"
)

mouse = Item(
    id=2,
    name="Gaming Mouse",
    quantity=15,
    price=10,
    category="Electronic"
)

print(
    f"Item #{keyboard.id}: "
    f"{keyboard.name} | "
    f"Stock={keyboard.quantity} | "
    f"Price={keyboard.price}"
)

print(
    f"Item #{mouse.id}: "
    f"{mouse.name} | "
    f"Stock={mouse.quantity} | "
    f"Price={mouse.price}"
)


print("\n" + "=" * 50)
print("CREATE CUSTOMER")
print("=" * 50)

customer = Customer(
    id=1,
    name="Mirza",
    address="Padang",
    phone="08123456789"
)

print(
    f"Customer #{customer.id}: "
    f"{customer.name}"
)


print("\n" + "=" * 50)
print("CREATE ORDER")
print("=" * 50)

order = Order(
    id=1,
    customer=customer,
    user="Admin",
    order_date="2026-07-14",
    status="Pending"
)

print(
    f"Order #{order.id} "
    f"Status={order.status}"
)


print("\n" + "=" * 50)
print("CREATE ORDER ITEMS")
print("=" * 50)

order_item_1 = OrderItem(
    id=1,
    item=keyboard,
    quantity=2,
    unit_price=keyboard.price
)

order_item_2 = OrderItem(
    id=2,
    item=mouse,
    quantity=3,
    unit_price=mouse.price
)

order.add_item(order_item_1)
order.add_item(order_item_2)

for order_item in order.order_items:
    print(
        f"{order_item.item.name} | "
        f"Qty={order_item.quantity} | "
        f"Unit Price={order_item.unit_price} | "
        f"Subtotal={order_item.subtotal()}"
    )


print("\n" + "=" * 50)
print("ORDER TOTAL")
print("=" * 50)

print(
    f"Total = {order.calculate_total()}"
)


print("\n" + "=" * 50)
print("PAY ORDER")
print("=" * 50)

print("Before:", order.status)

order.mark_paid()

print("After :", order.status)


print("\n" + "=" * 50)
print("REDUCE STOCK")
print("=" * 50)

print(
    f"Before {keyboard.name}: "
    f"{keyboard.quantity}"
)

keyboard.decrease_stock(
    order_item_1.quantity
)

print(
    f"After  {keyboard.name}: "
    f"{keyboard.quantity}"
)

print()

print(
    f"Before {mouse.name}: "
    f"{mouse.quantity}"
)

mouse.decrease_stock(
    order_item_2.quantity
)

print(
    f"After  {mouse.name}: "
    f"{mouse.quantity}"
)


print("\n" + "=" * 50)
print("CREATE STOCK TRANSACTIONS")
print("=" * 50)

transaction_1 = StockTransaction.from_order(
    id=1,
    item=keyboard,
    quantity=order_item_1.quantity,
    order_id=order.id,
    transaction_date="2026-07-14"
)

transaction_2 = StockTransaction.from_order(
    id=2,
    item=mouse,
    quantity=order_item_2.quantity,
    order_id=order.id,
    transaction_date="2026-07-14"
)

for transaction in (
    transaction_1,
    transaction_2
):
    print(
        f"Transaction #{transaction.id} | "
        f"Item={transaction.item.name} | "
        f"Type={transaction.transaction_type} | "
        f"Qty={transaction.quantity} | "
        f"Ref={transaction.reference_type} "
        f"#{transaction.reference_id}"
    )


print("\n" + "=" * 50)
print("SHIP ORDER")
print("=" * 50)

order.mark_shipped()

print(
    f"Status = {order.status}"
)


print("\n" + "=" * 50)
print("COMPLETE ORDER")
print("=" * 50)

order.mark_complete()

print(
    f"Status = {order.status}"
)


print("\n" + "=" * 50)
print("FINAL STOCK")
print("=" * 50)

print(
    f"{keyboard.name}: "
    f"{keyboard.quantity}"
)

print(
    f"{mouse.name}: "
    f"{mouse.quantity}"
)