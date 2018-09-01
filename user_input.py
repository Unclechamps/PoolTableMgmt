from table_manager import TableManager

class Main:
    def __init__(self): 
        self.exit = False
        self.table_manager = TableManager()
        self.table_manager.add_tables()
        self.userOptions()

    def userOptions(self):
        if self.exit == False:
            table_choice = input("What would you like to do: \n 1 - Check-in a table \n 2 - Check-out a table \n 3 - Print status of all tables \n 4 - Quit \n Enter choice: ")
            if table_choice == '1':
                self.table_manager.check_in()
                self.userOptions()
            elif table_choice == '2':
                self.table_manager.check_out() #only works if I execute the add_task function and then this one.
                self.userOptions()
            elif table_choice == '3':
                self.table_manager.printList()
                self.userOptions()
            elif table_choice == '4':
                self.quit()
            else:
                print("Not sure what you are asking for!?")

    def quit(self):
        print("Goodbye!")
        self.exit = True
