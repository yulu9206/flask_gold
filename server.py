from flask import Flask, render_template, session, request, redirect
import random
from datetime import datetime  
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'
                       
@app.route('/')          
def index(): 
  if session.get('gold') == None:
    session['gold'] = 0 
  if session.get('log') == None:
    session['log'] = ''
  return render_template('index.html', gold=session['gold'], log=session['log'])

@app.route('/process_money', methods=['POST'])
def process_money():
  building = request.form['building']
  earn = 0
  time = str(datetime.now())
  log = ''
  if building == 'farm':
    earn = random.randrange(10, 21)
  elif building == 'cave':
    earn = random.randrange(5, 11)
  elif building == 'house':
    earn = random.randrange(2, 6)
  elif building == 'casino':
    earn = random.randrange(-50, 51)
  session['gold'] += earn
  if earn >= 0:
    log = 'Earned ' + str(earn) + ' golds from the '+ building + '! (' + time + ' )'
  else:
    log = 'Entered a casino and lost ' + str(earn * -1) + ' golds...ouch.. (' + time + ' )'
  session['log'] += (log + '\n')
  return redirect('/')

app.run(debug=True)

# word color
# start new line


