class StockTransaction:
    def __init__(
        self,
        id,
        item,
        transaction_type,
        quantity,
        reference_type,
        reference_id,
        transaction_date
    ):
        # Unique transaction identifier
        self.id = id

        # Reference to the Item involved in this transaction
        self.item = item

        # Validate transaction type
        # IN     = stock received
        # OUT    = stock shipped/sold
        # ADJUST = manual stock correction
        if transaction_type not in (
            "IN",
            "OUT",
            "ADJUST"
        ):
            raise ValueError(
                "invalid transaction type"
            )

        self.transaction_type = transaction_type

        # Transaction quantity must be positive
        if quantity <= 0:
            raise ValueError(
                "quantity must be greater than zero"
            )

        self.quantity = quantity

        # Validate reference type if provided
        # ORDER       = created from a customer order
        # PROCUREMENT = created from stock receiving
        # MANUAL      = created from manual adjustment
        if reference_type is not None:
            if reference_type not in (
                "ORDER",
                "PROCUREMENT",
                "MANUAL"
            ):
                raise ValueError(
                    "invalid reference type"
                )

        # Store transaction reference information
        self.reference_type = reference_type
        self.reference_id = reference_id

        # Date and time when transaction occurred
        self.transaction_date = transaction_date

    @classmethod
    def from_order(
        cls,
        id,
        item,
        quantity,
        order_id,
        transaction_date
    ):
        """
        Create an OUT transaction from an Order.

        Example:
        Customer buys 5 keyboards.
        Stock decreases by 5.
        """

        return cls(
            id=id,
            item=item,
            transaction_type="OUT",
            quantity=quantity,
            reference_type="ORDER",
            reference_id=order_id,
            transaction_date=transaction_date
        )

    @classmethod
    def from_procurement(
        cls,
        id,
        item,
        quantity,
        procurement_id,
        transaction_date
    ):
        """
        Create an IN transaction from a Procurement.

        Example:
        Supplier delivers 100 keyboards.
        Stock increases by 100.
        """

        return cls(
            id=id,
            item=item,
            transaction_type="IN",
            quantity=quantity,
            reference_type="PROCUREMENT",
            reference_id=procurement_id,
            transaction_date=transaction_date
        )

    @classmethod
    def from_manual_adjustment(
        cls,
        id,
        item,
        quantity,
        transaction_date
    ):
        """
        Create an ADJUST transaction.

        Example:
        System says 50 laptops.
        Physical count finds 47.
        Inventory is adjusted.
        """

        return cls(
            id=id,
            item=item,
            transaction_type="ADJUST",
            quantity=quantity,
            reference_type="MANUAL",
            reference_id=None,
            transaction_date=transaction_date
        )