from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


todo = []


@app.route("/")
def index():
    return render_template("index.html", todos=todo)

@app.route("/add", methods=['POST'])
def add():
    todoS = request.form['todo']
    
    if len(todoS) != 0:
        todo.append({"task":todoS, "done":False})
        
        return redirect(url_for("index"))
    else:
        
        
    
        
        # todo.append({"task":todoS, "done":False})
        return redirect(url_for("index"))

@app.route("/edit/<int:indeX>", methods=['GET',"POST"])
def edit(indeX):
    todos = todo[indeX]
    if request.method == "POST":
        todos['task'] = request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todos, indeX=indeX)
        
    
@app.route("/check/<int:indeX>")
def check(indeX):
    todo[indeX]['done'] = not todo[indeX]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:indeX>")
def delete(indeX):
    del todo[indeX]
    return redirect(url_for("index"))

@app.route("/reset", methods=['POST'])
def reset():
    
    todo.clear()
    
    return redirect(url_for("index"))
        
        # return redirect(url_for("index"))
        
    #     if len(todo)< 1:
    #         print("fix it")
    #         return redirect(url_for("index"))
    #     else:
            
    #         del todo
            
    #         return redirect(url_for("index"))
    # else:
    #     render_template('index.html')        
        
    

    
if __name__ == "__main__":
    app.run(debug=True)