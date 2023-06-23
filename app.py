import os

secret_key = os.urandom(24)
from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, session
import pickle
import pandas as pd
import pyfirmata
import time
from serial import Serial
from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = secret_key

pred=0
@app.route('/')
def Home():
  return render_template('Home.html')

@app.route('/predict', methods=['POST'])

def predict():
  csv_file = request.files['csv_file']
  test_data = pd.read_csv(csv_file)
  model = pickle.load(open('model.pkl', 'rb'))
  predictions = model.predict(test_data)
  pred=predictions
  
  
 
  


  servo_pin1 = 10
  servo_pin2 = 11
  servo_pin3 = 3
  servo_pin4 = 6
  servo_pin5 = 5
  board = pyfirmata.Arduino('COM4')
 
 
   # Replace with the appropriate port
  servo1 = board.get_pin('d:{}:s'.format(servo_pin1))
  servo2 = board.get_pin('d:{}:s'.format(servo_pin2))
  servo3 = board.get_pin('d:{}:s'.format(servo_pin3))
  servo4 = board.get_pin('d:{}:s'.format(servo_pin4))
  servo5 = board.get_pin('d:{}:s'.format(servo_pin5))

  if pred == 5:
          servo1.write(100)
          servo2.write(30)
          servo3.write(30)
          servo4.write(30)
          servo5.write(30)
          time.sleep(1)
          time.sleep(5)
          servo1.write(60)
          servo2.write(60)
          servo3.write(60)
          servo4.write(80)
          servo5.write(65)
            
  elif pred == 4:
          servo1.write(30)
          servo2.write(100)
          servo3.write(120)
          servo4.write(30)
          servo5.write(30)
          time.sleep(1)
          time.sleep(5)
          servo1.write(60)
          servo2.write(60)
          servo3.write(60)
          servo4.write(80)
          servo5.write(65)

  elif pred == 3:
          servo1.write(30)
          servo2.write(100)
          servo3.write(30)
          servo4.write(30)
          servo5.write(30)
          time.sleep(1)
          time.sleep(5)
          servo1.write(60)
          servo2.write(60)
          servo3.write(60)
          servo4.write(80)
          servo5.write(65)
  elif pred == 2:
          servo1.write(30)
          servo2.write(30)
          servo3.write(30)
          servo4.write(30)
          servo5.write(30)
          time.sleep(1)
          time.sleep(5)
          servo1.write(60)
          servo2.write(60)
          servo3.write(60)
          servo4.write(80)
          servo5.write(65)

  elif pred == 6:
          servo1.write(120)
          servo2.write(120)
          servo3.write(120)
          servo4.write(120)
          servo5.write(120)
          time.sleep(1)
          time.sleep(5)
          servo1.write(60)
          servo2.write(60)
          servo3.write(60)
          servo4.write(80)
          servo5.write(65)


  elif pred == 1:
        servo1.write(100)
        servo2.write(80)
        servo3.write(100)
        servo4.write(100)
        servo5.write(100)
        time.sleep(1)
        
        time.sleep(5)
        servo1.write(60)
        servo2.write(60)
        servo3.write(60)
        servo4.write(80)
        servo5.write(65)
        

      
  else:          
          servo1.write(60)
          servo2.write(60)
          servo3.write(60)
          servo4.write(80)
          servo5.write(65)
          time.sleep(1)
  return render_template('result.html', predictions=predictions)
@app.route('/back')
def back():
    session.clear()
    return redirect(url_for('Home'))


if __name__ == '__main__':
  app.run(debug=True)
