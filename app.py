from flask import Flask, render_template, request, session, redirect, url_for
from questions.questions1 import level1
from questions.questions2 import level2
from questions.questions3 import level3
from questions.questions4 import level4
from questions.questions5 import level5
import os
app = Flask(__name__)
app.secret_key = os.urandom(73)
current_question = 0
score = 0



@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method== "POST" :
     session["name"]= request.form["username"]
     return redirect(url_for('pt1'))
     
    return render_template("index.html")

@app.route("/pt1", methods=["GET", "POST"])
def pt1():
    name = session.get('name')
    global current_question, score
    if request.method== "POST":
        selected = request.form.get("option")
        correct_answer = level1[current_question]["answer"]
        if  selected == correct_answer:
            score = score + 1
        current_question += 1
        if current_question >= len(level1) and 2<score<6 :
            final_score = score
            session["score1"] = final_score
            session["tlev1"] = 5
            current_question = 0
            score = 0
            return render_template("rst1.html", niveau =1)
        
        if current_question >= len(level1) and score < 3:
            final_score = score
            current_question = 0
            score = 0
            return render_template("lose1.html", niveau=1, score = final_score, total = len(level1), mini = 3)
    question_data = level1[current_question]
    return render_template("pt1.html",name = name, question=question_data, niveau=1, question_number=current_question + 1)
@app.route("/pt2", methods=["GET", "POST"])
def pt2():
    global current_question, score
    name = session.get('name')

    if request.method== "POST":
        selected = request.form.get("option")
        correct_answer = level2[current_question]["answer"]
        if  selected == correct_answer:
            score = score + 1
        current_question += 1
        if current_question >= len(level2) and 4<score <8 :
            final_score = score
            session["score2"] = final_score
            session["tlev2"] = 7
            current_question = 0
            score = 0
            return render_template("rst2.html", niveau =2)
        
        if current_question >= len(level2) and score < 5:
            final_score = score
            current_question = 0
            score = 0
            return render_template("lose2.html", niveau=2, score = final_score, total = len(level2), mini = 5)
    
    question_data = level2[current_question]
    return render_template("pt2.html", name = name, question=question_data, niveau=2, question_number=current_question + 1)
@app.route("/pt3", methods=["GET", "POST"])
def pt3():
    global current_question, score
    name = session.get('name')

    if request.method== "POST":
        selected = request.form.get("option")
        correct_answer = level3[current_question]["answer"]
        if  selected == correct_answer:
            score = score + 1
        current_question += 1
        if current_question >= len(level3) and 6<score <10 :
            final_score = score
            session["score3"] = final_score
            session["tlev3"] = 9
            current_question = 0
            score = 0
            return render_template("rst3.html", niveau =3)
        
        if current_question >= len(level3) and score < 7:
            final_score = score
            current_question = 0
            score = 0
            return render_template("lose3.html", niveau=3, score = final_score, total = len(level3), mini = 7)
    
    question_data = level3[current_question]
    return render_template("pt3.html", name = name, question=question_data, niveau=3, question_number=current_question + 1)
@app.route("/pt4", methods=["GET", "POST"])
def pt4():
    global current_question, score
    name = session.get('name')

    if request.method== "POST":
        selected = request.form.get("option")
        correct_answer = level4[current_question]["answer"]
        if  selected == correct_answer:
            score = score + 1
        current_question += 1
        if current_question >= len(level4) and 8<score <12 :
            final_score = score
            session["score4"] = final_score
            session["tlev4"] = 11
            current_question = 0
            score = 0
            return render_template("rst4.html", niveau =4)
        
        if current_question >= len(level4) and score < 9:
            final_score = score
            current_question = 0
            score = 0
            return render_template("lose4.html", niveau=4, score = final_score, total = len(level4), mini = 9)
    
    question_data = level4[current_question]
    return render_template("pt4.html", name = name, question=question_data, niveau=4, question_number=current_question + 1)
@app.route("/pt5", methods=["GET", "POST"])
def pt5():
    global current_question, score
    name = session.get('name')

    if request.method== "POST":
        selected = request.form.get("option")
        correct_answer = level5[current_question]["answer"]
        if  selected == correct_answer:
            score = score + 1
        current_question += 1
        if current_question >= len(level5) and 10<score <14:
            final_score = score
            session["score5"] = final_score
            session["tlev5"] = 13
            current_question = 0
            score = 0
            return redirect(url_for('thk'))
        
        if current_question >= len(level5) and score < 11:
            final_score = score
            current_question = 0
            score = 0
            return render_template("lose5.html", niveau=5, score = final_score, total = len(level5), mini = 10)
    
    question_data = level5[current_question]
    return render_template("pt5.html", name = name, question=question_data, niveau=5, question_number=current_question + 1)
@app.route("/thk", methods=["GET", "POST"])
def thk():
    session["tscore"] = sum( [session.get('score1', 0),session.get('score2', 0), session.get('score3', 0), session.get('score4', 0), session.get('score5', 0)]) 
    session["ttotal"] = sum( [session.get('tlev1', 0),session.get('tlev2', 0), session.get('tlev3', 0), session.get('tlev4', 0), session.get('tlev5', 0)]) 
    tscore = session.get('tscore')
    ttotal = session.get('ttotal')
    return render_template("thk.html", score = tscore, total = ttotal)
if __name__ == "__main__":
   app.run(debug = True)
