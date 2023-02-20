
class OrderItem(object) :
    """! This represents a Order Item
    """

    COUNTER_ID = 1

    id = 0
    """! This field represents the id of the items"""
    
    """! This field represents the amount of items"""
    amount = 0
    
    """! This field represents the value of the item"""
    value = 0
    
    """! This field represents the discount of the item"""
    discount = 0.0

    def __init__(self, amount,  value,  discount):
        """!Constructor
        @param amount This represents the amount
        @param value This represents the value
        @param discount This represents the discount
        """
        
        self.id = OrderItem.COUNTER_ID
        
        OrderItem.COUNTER_ID += 1
        
        self.amount = amount
        self.value = value
        self.discount = discount
        
    def  getFinalValue(self) :
        return (self.amount * self.value) * (1.0 - self.discount)
    
    def  toString(self) :
        return "id=" + str(self.id) + ", amount=" + str(self.amount) + ", value=" + str(self.value) + ", discount=" + str(self.discount) + ", finalValue=" + str(self.getFinalValue())

    def isValid(self):
        """! This method ensures an order is valid or not
        If the amount and value fields are negative, the item is invalid. 
        if the discount is negative or more than 1, the item is also invalid.
        @return True, if the order item is valid. False, otherwise.
        """
        
        if self.amount < 0.0: 
            return False
        
        # it verifies a negative
        if self.value < 0.0: 
            return False
        
        if self.discount < 0.0 or self.discount > 1.0:
            return False
        
        return True