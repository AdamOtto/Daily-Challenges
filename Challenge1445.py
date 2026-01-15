"""
The United States uses the imperial system of weights and measures,
which means that there are many different, seemingly arbitrary units to measure distance.
There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

Create a data structure that can efficiently convert a certain quantity of one unit to the correct
amount of any other unit. You should also allow for additional units to be added to the system.
"""
class ImperialConv:

    def Foot2Inch(self, foot):
        return foot * 12

    def Inch2Foot(self, inch):
        return inch / 12

    def Yard2Foot(self, yard):
        return yard * 3

    def Foot2Yard(self, foot):
        return foot / 3

    def Chain2Yard(self, chain):
        return 22 * chain

    def Yard2Chain(self, yard):
        return yard / 22

    def Mile2Chain(self, mile):
        return mile * 80

    def Chain2Mile(self, chain):
        return chain / 80

    def Chain2Inch(self, chain):
        return self.Foot2Inch(self.Yard2Foot(self.Chain2Yard(chain)))

    def Inch2Chain(self, inch):
        return self.Yard2Chain(self.Foot2Yard(self.Inch2Foot(inch)))

    def Mile2Yard(self, mile):
        return self.Chain2Yard(self.Mile2Chain(mile))


IC = ImperialConv()
# Return 792
print(IC.Chain2Inch(1))
# Return 2
print(IC.Inch2Chain(1584))
# Return 176000
print(IC.Mile2Yard(100))