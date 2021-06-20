import ddb
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = b'aaa!111/'

# 메인
@app.route('/')
def index():
    return render_template("index.html")
# 회사소개
@app.route('/about')
def about():
    return render_template("about.html")   
     
# 차량소개
@app.route('/propertygrid')
def propertygrid():
    return render_template("property-grid.html")       

# 예약하기
@app.route('/bloggrid')
def bloggrid():
    if 'email' in session:
        return render_template("blog-grid.html")
    else:
        return redirect('/signin')      

# 로그인
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    else:
        email = request.form['email']
        pswd = request.form['pswd']
        ret = ddb.select_member(email, pswd)
        if ret != None:
            session['email'] = email
            return redirect('/')
        else:
            return redirect('/signin') 

# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/') # 메인으로            

# 회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        email = request.form['email']
        pswd = request.form['pswd']
        username = request.form['username']
        ddb.insert_member(email, pswd, username)
        return redirect('/')  

# if __name__ == '__main__': 
#   app.run(debug-True)  개인컴퓨터로 실행시 주석풀것
