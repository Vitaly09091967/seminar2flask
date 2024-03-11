from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    
    resp = make_response(redirect('/welcome'))
    resp.set_cookie('user_data', f'{name}:{email}')
    
    return resp

@app.route('/welcome')
def welcome():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, _ = user_data.split(':')
        return render_template('welcome.html', name=name)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('user_data', '', expires=0)
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)

