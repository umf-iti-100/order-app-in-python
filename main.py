from src.Database import Database
from src.OrderItem import OrderItem
from src.utils.ConsoleUtils import ConsoleUtils

class Main(object):
    
    def main(self):
    
        while True:
            
            print("Menu:")
            print("1 - Add Order Item")
            print("2 - List Orders")
            print("3 - Remove Order Item")
            print("4 - Exit")
            
            option = ConsoleUtils.askInteger("Option: ")
            
            if option==1:
                self.addOrderItem()
            elif option==2:
                self.listOrders()
            elif option==3:
                self.removeOrderItemById()
            elif option==4:
                quit(1)
            else:
                print("Invalid Option. Try it again!")

    def addOrderItem(cls):
    
        print("Add Order Item")
        amount = ConsoleUtils.askInteger("Amount: ")
        value = ConsoleUtils.askFloat("Value: ")
        discount = ConsoleUtils.askFloat("Discount: ")
        oi = OrderItem(amount, value, discount)
        Database.getInstance().save(oi)

    def listOrders(cls):
        
        print("List Order Items:")
        items = Database.getInstance().getAll()
        for oi in items:
            print(oi.toString())

    def removeOrderItemById(cls):
        
        print("Remove Order Item by Id:")
        id = ConsoleUtils.askInteger("Id: ")
        Database.getInstance().removeById(id)
        

Main().main()