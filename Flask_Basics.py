## Flask App Routing

from flask import Flask,render_template,request,redirect,url_for


## create a Simple Flask Application

app=Flask(__name__)

# @app.route("/",methods=["GET"])
# def welcome():
#     return "<h1>Welcome to my Flask App</h1>"

# @app.route("/index",methods=["GET"])
# def index():
#     return "<h2>Welcome to the Index Page</h2>"

## Variable Rule
# @app.route("/success/<int:score>")
# def  success(score):
#     if score >= int("50"):
#         return f"<h1>Congratulations, your score is {score}</h1>"
#     else:
#         return f"<h1>Sorry!!! You Are Failll , your score is {score}</h1>"

@app.route("/",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result=""
        if average_marks>50:
            result="success"
        else:
            result="fail"
        
        return redirect(url_for(result,score=average_marks))
        # return render_template('form.html',score=average_marks)


@app.route("/success/<int:score>",)
def success(score):
    return f"<h1>Congratulations, your score is {score}</h1>"

@app.route("/fail/<int:score>")
def fail(score):
    return f"<h1>Sorry!!  You Are Failll, your score is {score}</h1>"




if __name__=="__main__":
    app.run(debug=True)