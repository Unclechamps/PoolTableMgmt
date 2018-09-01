import datetime, time
import json
from pool_tables import PoolTable

class TableManager:
    def __init__(self):
        self.table_list = []
        self.current_status_list = []
        self.log_session_list = []
        self.cost_per_hour = 30

    def add_tables(self):
        #loop to add tables
        for index in range(1,13):
            table = PoolTable(index, "Open")
            self.addTable(table)

    def addTable(self,table):
        self.table_list.append(table)

    def printList(self):
        for table in self.table_list:
            if table.status == "Open":
                print(f"Table {table.table_number} is open")
            elif table.status == "Occupied":
                current_duration = round((time.time() - table.start_time)/60, 2)
                print (f"Table {table.table_number} is occupied since {datetime.datetime.now()} and has been occupied for {current_duration} minutes.")
        # self.userOptions()

    def check_in(self):
        open = int(input("Which table would you like to add a session: "))-1
        if open > len(self.table_list) or open < 0:
            print(f"Pick a table between 1 and {len(self.table_list)}.")
        elif self.table_list[open].status == "Occupied":
            print(f"Table {self.table_list[open].table_number} is already occupied.")
        else:
            self.table_list[open].status = "Occupied"
            self.table_list[open].start_time = time.time()
            self.table_list[open].start_time_stamp = str(datetime.datetime.now())
            self.current_status()

    def check_out(self):
        end = int(input("Which table would you like to close: "))-1
        if self.table_list[end].status == "Open":
                print(f"Table {end} is already open.")
        else:
            self.table_list[end].status = "Open"
            self.table_list[end].end_time = time.time()
            self.table_list[end].end_time_stamp = str(datetime.datetime.now())
            self.calculate_duration(end)
            self.calculate_cost(end)
            print(f"You closed table {self.table_list[end].table_number}. User played for {self.table_list[end].total_duration} minutes and owes ${self.table_list[end].total_cost}.")
            self.log_session(end)
            self.current_status()

    def calculate_duration(self,table_number):
        self.table_list[table_number].total_duration = round((self.table_list[table_number].end_time - self.table_list[table_number].start_time)/60,2)

    def calculate_cost(self, table_number):
        self.table_list[table_number].total_cost = round(self.table_list[table_number].total_duration * (self.cost_per_hour/60),2)

    def current_status(self):

        for index in range(0,len(self.table_list)):
            pool_table = self.table_list[index]
            self.current_status_list.append(pool_table.__dict__)
        with open('currentstatus.json','w') as file:
            file.write(json.dumps(self.current_status_list, indent = 2))

    def log_session(self, table_number):

        todays_date = (datetime.datetime.today().strftime('%m-%d-%Y'))
        file_name = todays_date + '.json'

        pool_table = self.table_list[table_number]
        self.log_session_list.append(pool_table.__dict__)

        with open(file_name,'w') as file:
            file.write(json.dumps(self.log_session_list, indent = 2))



# Still working on the pull of currentstatus.json

    # def crash_data(self):
    #     with open('currentstatus.json') as file:
    #         self.current_status_list = json.load(file)
