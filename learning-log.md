# Session 1

## Topic

Domain Model - Item, category, customer

## Learned

- Models should protect their own data.
- Constructor can reuse validation methods.
- Stock changes should go through business methods.
- ID can be provided by another layer and simply stored in the model.

## Completed

- Item entity
  - rename()
  - change_price()
  - change_category()
  - increase_stock()
  - decrease_stock()

- customer entity

- category entity

Session Summary

Completed Models:

- Item
- Category
- Customer
- Supplier
- Order
- OrderItem
- StockTransaction

Concepts Learned:

- Entity responsibilities
- Validation inside models
- Order ↔ OrderItem relationship
- Item references inside OrderItem
- Business workflow modeling
- Immutable transaction records
- Git basic workflow
