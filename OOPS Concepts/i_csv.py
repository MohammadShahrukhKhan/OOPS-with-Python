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
            print(item)  
            Item(
                name = item.get("name"),
                branch = item.get("branch"),
                roll = item.get("roll")
            )   
        
    def __repr__(self):
        return f"Item ('{self.name}', {self.branch}, {self.roll})"

Item.instantiate_from_csv()
print(Item.all)
