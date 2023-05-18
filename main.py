from flask import Flask,request,jsonify
import csv
app= Flask(__name__)

@app.route("/")

def sneha():
    return "hi iam sneha"

@app.route("/sneha")
def sneha2():
    return "iam learning flask module"

@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("u")
    email=request.json.get("e")
    password=request.json.get("p")
    with open("credintials.csv","a+") as f:
        writer=csv.writer(f)
        writer.writerow([username,email,password])


    return jsonify({
        "status":"sucess"
    }),201
    

    
app.run(debug=True)






















