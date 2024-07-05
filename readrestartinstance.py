#from google.colab import files

from TaskList import TaskList

class ReadRestartInstance(TaskList) :
  def __init__(self):
    super().__init__()
    self.month = ''
    self.user = ''
    self.raw = []

  def input_month(self):
    self.month = input('Input bulan/tahun (BB/TTTT) : ')

  def get_date(self):
    self.date = self.row_split[1].split(' ')[0] + f'/{self.month}'

  def get_time(self):
    self.time_start = self.row_split[1].split(' ')[2]
    minute = int(self.time_start.split(':')[1])
    self.escalation = self.time_start.replace(str(minute),str(minute+1))
    self.respone_time = self.time_start.replace(str(minute),str(minute+2))
    self.time_end = self.time_start.replace(str(minute),str(minute+3))

  def get_user(self):
    self.raw = self.row_split[2].replace('Start - Restart Server [','')
    self.raw = self.raw.replace(' , Workspace [prod], User[','')
    self.raw = self.raw.replace(' , Workspace [pre], User[','')
    self.user = self.raw.split(']')[1]

  def get_instance(self):
    self.instance = self.raw.split(']')[0].split(' , ')

  def get_row_split(self, cell):
    self.row_split = cell.split('\n')

  def run(self):
      self.get_file_name()
      self.input_month()
      self.read_file()
      for i in self.data :
        self.get_row_split(i)
        self.get_user()
        if 'Luthfan Hilsan' not in(self.user):
          continue
        self.get_date()
        self.get_time()
        print('----------------------------------------------------------------')
        self.get_instance()
        print('Date\t\t:',self.date)
        print('Instance\t:',self.instance)
        self.input_df()
        print('----------------------------------------------------------------')
      self.create_excel()

