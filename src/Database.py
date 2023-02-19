class Database:

    instance = None
    
    orderItems = []
    
    @staticmethod
    def getInstance():

        if Database.instance == None:
            Database.instance = Database()
        
        return Database.instance

    def save(self, orderItem):
        self.orderItems.append(orderItem)

    def removeById(self, id):
        self.orderItems = filter(lambda x: x.id != id, self.orderItems)
    
    def getAll(self):
        return self.orderItems

