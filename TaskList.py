import pandas as pd


class TaskList:
  def __init__(self):
    self.df = pd.DataFrame(columns = ['date', 'task_action_list', 'task_item','description','start_time','response_time','escalation_time','end_time','status'])
    self.file_name = ''
    self.data = []
    self.row_split = []
    self.date = ''
    self.time_start = ''
    self.escalation = ''
    self.respone_time = ''
    self.time_end = ''
    self.instance = []

  def get_file_name(self):
    self.file_name = input('Masukkan nama file : ')

  def read_file(self):
    with open(self.file_name, 'r') as f :
      self.data = f.read().split("\n\n")

  def get_row_split(self, cell):
    self.row_split = cell.split('\n')

  def input_df(self):
    for i in self.instance :
      if len(i) > 0 :
        self.df = self.df._append({'date' : self.date , 'task_action_list': 'Z-Clean', 'task_item':i,'description':'High disk usage','start_time' : self.time_start, 'response_time' : self.respone_time ,'escalation_time' : self.escalation ,'end_time' : self.time_end ,'status' : 'Success'},ignore_index = True)

  def create_excel(self):
    self.df = self.df.reset_index(drop=True)
    self.df.to_excel('Template_task_list_v2.xlsx',index=False)