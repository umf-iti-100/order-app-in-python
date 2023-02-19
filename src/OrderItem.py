
class OrderItem(object) :

    COUNTER_ID = 1

    id = 0
    amount = 0
    value = 0
    discount = 0.0

    def __init__(self, amount,  value,  discount):
        
        self.id = OrderItem.COUNTER_ID
        
        OrderItem.COUNTER_ID += 1
        
        self.amount = amount
        self.value = value
        self.discount = discount
        
    def  getFinalValue(self) :
        return (self.amount * self.value) * (1.0 - self.discount)
    
    def  toString(self) :
        return "id=" + str(self.id) + ", amount=" + str(self.amount) + ", value=" + str(self.value) + ", discount=" + str(self.discount) + ", finalValue=" + str(self.getFinalValue())
