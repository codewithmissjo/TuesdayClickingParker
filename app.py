from flask import Flask, render_template, redirect, request, make_response

app = Flask(__name__)

number = 0

@app.route('/')
def index():
  global number
  cookie_num = request.cookies.get('click_num')
  if cookie_num:
    number = int(cookie_num)
  return render_template("index.html", number_ph=number)

@app.route('/click')
def click_function():
  global number
  number += 1
  resp = make_response(redirect('/'))
  resp.set_cookie('click_num', str(number), max_age = 86400)
  return resp

if __name__ == '__main__':
  app.run()