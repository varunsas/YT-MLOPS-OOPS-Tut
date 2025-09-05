## Initiate Class

# class employee:
#     ## special method/magic method/dunder method - constructor
#
#     def __init__(self):
#         self.id = 123
#         self.salary = 5000
#         self.designation= "SDE"
#
#
# ## Create an object/instance of the class
#
# sam= employee()
#
# print(sam.salary)
# print(sam.id)
# print(sam.designation)


#####################################################
class employee:
    ## special method/magic method/dunder method - constructor

    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 5000
        self.designation= "SDE"
        print("attributes/data has been initiated")

    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

## Create an object/instance of the class

sam= employee()

print(type(sam))

# sam.travel("Kerala")
