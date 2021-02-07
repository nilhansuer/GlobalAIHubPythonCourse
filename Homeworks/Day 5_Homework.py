print("*****Animals*****")

class Animals: 
    def __init__(self, a_name, a_type, a_legs):
        self.animalname = a_name
        self.animaltype= a_type
        self.animallegs= a_legs
    def print_animalname(self): 
        print(self.animalname)
    def print_animaltype(self): 
        print(self.animaltype)
    def print_animallegs(self):
        print(self.animallegs)
    def print_animalstatus(self):
        print(self.animalname + " is a " + self.animaltype + " and it has " + str(self.animallegs) + " legs. ")
animal1 = Animals("Max","Dog", 4)
animal1.print_animalname()
animal1.print_animaltype()
animal1.print_animallegs()
animal1.print_animalstatus()

print(" ")
print("*****Dogs*****")

class Dogs(Animals):
    def __init__(self, d_name, d_kind, d_color):
        self.dogname = d_name
        self.dogkind = d_kind
        self.dogcolor = d_color
    def print_dogname(self):
        print(self.dogname) 
    def print_dogkind(self):
        print(self.dogkind)
    def print_dogcolor(self):
        print(self.dogcolor)
    def print_dogstatus(self):
        print(self.dogname + " is a " + self.dogkind + " and its color is " + self.dogcolor + ".")

dog1 = Dogs("Ice", "Husky", "white")
dog1.print_dogname()
dog1.print_dogkind()
dog1.print_dogcolor()
dog1.print_dogstatus()

print(" ")
print("*****Cats*****")

class Cats(Animals):
    def __init__(self, c_name, c_kind, c_color):
        self.catname = c_name 
        self.catkind = c_kind
        self.catcolor = c_color
    def print_catname(self):
        print(self.catname) 
    def print_catkind(self):
        print(self.catkind)
    def print_catcolor(self):
        print(self.catcolor)
    def print_catstatus(self):
        print(self.catname + " is a " + self.catkind + " and its color is " + self.catcolor + " .")

cat1 = Cats("Minnie", "Scottish", "grey")
cat1.print_catname()
cat1.print_catkind()
cat1.print_catcolor()
cat1.print_catstatus()
