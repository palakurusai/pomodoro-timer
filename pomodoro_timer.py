import time
import json
import os
Focus_time=25*60
Break_time=5*60
data_file='sessions.json'

def load_data():
  if os.path.exists(data_file):
    with open(data_file,'r') as f:
      return json.load(f)
  return {'sessions':0}

def save_data(data):
  with open(data_file,'w') as f:
    json.dump(data,f)
  
def countdown(seconds,label):
  while seconds:
    mins,sec=divmod(seconds,60)
    timer=f'{label} Time: {mins:02d}:{sec:02d}'
    print(timer,end='\r')
    time.sleep(1)
    seconds-=1
  print(f'\n{label} completed!')
  print('\a')

def pomodoro():
    data = load_data()

    while True:
        print("\n--- Pomodoro Menu ---")
        print("1. Start Default Session (25/5)")
        print("2. Custom Timer")
        print("3. Show Stats")
        print("4. Exit")

        choice=int(input('Enter your choice: '))

        if choice==1:
          countdown(Focus_time,'Focus')
          data['sessions']+=1
          save_data(data)

          countdown(Break_time,'Break')
        elif choice==2:
          f=int(input('Enter the focus time(min): '))*60
          b=int(input('Enter the Break time(min): '))*60
          countdown(f,'Focus')
          data['sessions']+=1
          save_data(data)

          countdown(b,'Break')
        elif choice==3:
          print(f"Total sessions completed today: {data['sessions']}")
        elif choice==4:
          print('Goodbye! Stay productive')
          break
        else:
          print('Invalid input')
if __name__=='__main__':
  pomodoro()
