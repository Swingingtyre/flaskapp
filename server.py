from flask import Flask, render_template
import base64
from io import BytesIO
from matplotlib import pyplot as plt
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/figure/')
def my_link():
  print ('Information Requested')
  with open('data.txt') as f:
    lines = f.readlines()
    x = [float(line.split(',')[0]) for line in lines]
    y = [float(line.split(',')[1]) for line in lines]
    x.sort()
    y.sort()
  fig = plt.figure(figsize=(5,5))

  plt.subplot(111,title='Amount of Stonks',yscale='linear',xscale='linear',ylabel='Stonks',xlabel='Time')

  plt.plot(x,y)
  plt.xlim((0,37))
  plt.ylim((0,37))
  tmpfile = BytesIO()
  fig.savefig(tmpfile, format='png')
  encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')


  html = f"<img src=\'data:image/png;base64,{encoded}\'>"

  with open('./templates/figure.html','w') as f:
      f.write(html) 

  return render_template('figureView.html')

if __name__ == '__main__':
  app.run(debug=True)