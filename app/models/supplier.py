class Supplier:
    def __init__(self, id, name, company_name, phone, address):
        self.id = id
        self.rename(name)
        self.change_company_name(company_name)
        self.change_phone(phone)
        self.change_address(address)

    
    def rename(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("name must be a string")
        
        name = new_name.strip()

        if not name:
            raise ValueError("name must not be empty")
        
        self.name = name
        


    def change_company_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("name must be a string")
        
        name = new_name.strip()

        if not name:
            raise ValueError("name must not be empty")
        
        self.company_name = name


    def change_phone(self, new_phone):
        if not isinstance(new_phone, str):
            raise ValueError("phone must be string")
        
        phone = new_phone.strip()

        if not phone:
            raise ValueError("phone must not be empty")

        if not phone.isdigit():
            raise ValueError("phone must contain only digit")
        
        self.phone = phone


    def change_address(self, new_address):
        if not isinstance(new_address, str):
            raise ValueError("address must be str")
        
        address = new_address.strip()

        if not address:
            raise ValueError("address must not be empty") 
        
        self.address = address