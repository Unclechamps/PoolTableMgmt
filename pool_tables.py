class PoolTable:
    def __init__(self,table_number, status):
        self.table_number = table_number
        self.status = status
        self.start_time = None
        self.start_time_stamp = None
        self.end_time = None
        self.end_time_stamp = None
        self.current_duration = None
        self.total_duration = None
        self.total_cost = None

    def __repr__(self):
        if status == "Open":
            return f"Table {self.table_number} is {self.status}"
        else:
            return f"Table {self.table_number} is {self.status} as of {self.start_time}"
 
