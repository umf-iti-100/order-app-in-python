from src.Database import Database
from src.OrderItem import OrderItem
from src.utils.ConsoleUtils import ConsoleUtils

class Main(object):
    
    def main(self):
    
        while True:
            
            ConsoleUtils.cls()
            
            print("Menu:")
            print("1 - Add Order Item")
            print("2 - List Orders")
            print("3 - Remove Order Item")
            print("4 - Find Errors")
            print("5 - Exit")
            
            option = ConsoleUtils.askInteger("Option: ")
            
            if option==1:
                self.addOrderItem()
            elif option==2:
                self.listOrders()
            elif option==3:
                self.removeOrderItemById()
            elif option==4:
                self.findErrors()
            elif option==5:
                quit(1)
            else:
                print("Invalid Option. Try it again!")

    def addOrderItem(cls):
    
        ConsoleUtils.cls()
    
        print("Add Order Item")
        
        amount = ConsoleUtils.askInteger("Amount: ")
        value = ConsoleUtils.askFloat("Value: ")
        discount = ConsoleUtils.askFloat("Discount: ")
        
        oi = OrderItem(amount, value, discount)
        
        Database.getInstance().save(oi)
        
        ConsoleUtils.askString("Done. Press enter to continue")

    def listOrders(cls):
        
        ConsoleUtils.cls()
        
        print("List Order Items:")
        
        items = Database.getInstance().getAll()
        for oi in items:
            print(oi.toString())
        
        ConsoleUtils.askString("Done. Press enter to continue")

    def removeOrderItemById(cls):
        
        ConsoleUtils.cls()
        
        print("Remove Order Item by Id:")
        
        id = ConsoleUtils.askInteger("Id: ")
        Database.getInstance().removeById(id)
        
        ConsoleUtils.askString("Done. Press enter to continue")
    
    def findErrors(self):
        
        ConsoleUtils.cls()
        
        print("Is order item valid?")
        
        items = Database.getInstance().getAll()
        
        for item in items:
            print("id="+str(item.id) +" => " + str(item.isValid()))
            
        ConsoleUtils.askString("Done. Press enter to continue")
            
Main().main()