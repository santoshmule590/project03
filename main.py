
from Models.utils import MedicalInsurance
from flask import Flask,jsonify,render_template,request
import config



app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")

@app.route("/Predict_charges",methods=["POST"])
def get_predicted():

    age = int(request.form.get('age'))
    sex = request.form.get("sex")
    bmi = float(request.form.get("bmi"))
    children = int(request.form.get("children"))
    smoker = request.form.get("smoker")
    region = request.form.get("region")

    print("age,sex,bmi,children,smoker,region\n",age,sex,bmi,children,smoker,region)



    Obj=MedicalInsurance(age,sex,bmi,children,smoker,region)
    result1= Obj.get_predicted_price()
    #print(f"The Insurance of claim is Rs. {result1}/- Only ") 
    return render_template("index.html",prediction=result1) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",port =config.PORT_NUMBER, debug=True)
