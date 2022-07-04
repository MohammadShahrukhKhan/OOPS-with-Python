import csv

class Item:

    all = []

    def __init__(self, name, branch, roll):
        
        self.name = name
        self.branch = branch
        self.roll = roll

        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('_items_.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)  
            Item(
                name = item.get("name"),
                branch = item.get("branch"),
                roll = item.get("roll") 
            )   

    @staticmethod
    def is_integer(num):
        # we shall count out the floats that are point zero 
        # i.e. 5.0, 19.0
        if isinstance(num, float):
            # count out the floats that are point zero 
            return num.is_integer() 
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item ('{self.name}', '{self.branch}', '{self.roll}')"

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(4.0))






