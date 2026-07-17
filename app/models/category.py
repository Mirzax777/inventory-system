class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        
        self.rename(name)
    
    def rename(self, new_name):

        if not isinstance(new_name, str):
            raise ValueError("name must be a string")


        name = new_name.strip()

        if not name:
            raise ValueError("name must not be empty")
        
        self.name = name