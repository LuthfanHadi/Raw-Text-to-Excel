from TaskList import TaskList


class ReadZclean(TaskList):
  def __init__(self):
    super().__init__()

  def get_date(self):
    self.date = self.row_split[7].replace("Date: ","")

  def get_row_split(self, cell):
    self.row_split = cell.split('\n')

  def get_time(self):
    self.time_start = self.row_split[8].replace("Time: ","")
    print(self.time_start)
    minute = int(self.time_start.split(':')[1])
    self.escalation = self.time_start.replace(str(minute),str(minute+1))
    # print(time_1)
    self.respone_time = self.time_start.replace(str(minute),str(minute+2))
    # print(time_2)
    self.time_end = self.time_start.replace(str(minute),str(minute+3))

  def get_instance(self):
    self.instance = self.row_split[4].replace("Instance Name: ","").split(" ")

  def run(self):
    self.get_file_name()
    self.read_file()
    for i in self.data :
      try:
        self.get_row_split(i)
        self.get_date()
        self.get_time()
        print('----------------------------------------------------------------')
        self.get_instance()
        print('Date\t\t:',self.date)
        print('Instance\t:',self.instance)
        self.input_df()
        print('----------------------------------------------------------------')
      except:
        pass
    self.create_excel()
