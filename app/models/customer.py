class Customer:
    def __init__(self, id, name, address, phone):
        self.id = id

        self.rename(name)
        self.change_address(address)
        self.change_phone(phone)

    def rename(self, new_name):

        if not isinstance(new_name, str):
            raise ValueError("name must be a string")

        name = new_name.strip()

        if not name:
            raise ValueError("name must not be empty")

        self.name = name

    def change_address(self, new_address):

        if not isinstance(new_address, str):
            raise ValueError("address must be a string")

        address = new_address.strip()

        if not address:
            raise ValueError("address must not be empty")

        self.address = address

    def change_phone(self, new_phone):

        if not isinstance(new_phone, str):
            raise ValueError("phone number must be a string")

        phone = new_phone.strip()

        if not phone:
            raise ValueError("phone number must not be empty")

        if not phone.isdigit():
            raise ValueError("phone number must contain only digits")

        self.phone = phone