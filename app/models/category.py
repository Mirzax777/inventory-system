class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        
        self.rename(name)
    
    def rename(self, new_name):
        name = new_name.strip()

        if not name:
            raise ValueError("name must not be empty")
        
        self.name = name