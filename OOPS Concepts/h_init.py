class classic:

    all = []

    def __init__(self, name, branch, roll):
        
        self.name = name
        self.branch = branch
        self.roll = roll

        # Actions to Execute 
        classic.all.append(self)

    def __repr__(self):
        return f"classic('{self.name}', {self.branch}, {self.roll})"

Class1 = classic("Shahrukh", "E.C.E", 18101090027)
Class1 = classic("Lalit", "E.E.E", 17101080021)
Class1 = classic("Rajesh", "C.S.E", 15101050075)
Class1 = classic("Pallavi", "M.E", 16101060066)
Class1 = classic("Nishant", "C.E", 13101010085)

print(classic.all)

# for inst in classic.all:
    # print(inst.name)

