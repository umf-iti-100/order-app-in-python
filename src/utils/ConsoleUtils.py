import os

class ConsoleUtils:

    @staticmethod
    def askString(prefix):

        print(prefix, end="")

        # Ask the user for any string
        text = input()

        if text == None:
            return None
        
        #A good approach would be removing all leading and trailing spaces before returning it
        return text.strip()
    
    @staticmethod
    def askInteger(field):

        text = ConsoleUtils.askString(field)

        return float(text)
    
    @staticmethod
    def askFloat(field):

        text = ConsoleUtils.askString(field)

        return float(text)

    @staticmethod
    def cls():
        """! This method clears the screen. It takes 
        into account the operating system that this app
        is running
        """
        # clear the screen
        os.system('cls' if os.name=='nt' else 'clear')
