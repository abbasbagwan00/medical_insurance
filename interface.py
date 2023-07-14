from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import MedicalInsurance
import config
import traceback

app = Flask(__name__)

@app.route('/')
def home1():
    

    return render_template('index.html')

@app.route('/predict_charges', methods = ['GET','POST'])
def predict_charges():
    try:

        if request.method == 'GET':

            data = request.args.get

            print("Data : ", data)

            age      = int(data('age'))
            gender   = data('gender')
            bmi      = eval(data('bmi'))
            children = int(data('children'))
            smoker = data('smoker')
            region = data('region')

            obj = MedicalInsurance(age, gender, bmi, children, smoker, region)

            pred_price = obj.get_predicted_price()

            # return jsonify({"Result" : f"Predicted medical insurance charges == {pred_price}"})
            return render_template('index.html', prediction = pred_price)

        elif request.method == 'POST':
            data = request.form.get
            print("Data :",data)
            age = int(data('age'))
            gender = data('gender')
            bmi = eval(data('bmi'))
            children = int(data('children'))
            smoker = data('smoker')
            region = data('region')

            Obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
            pred_price = Obj.get_predicted_price()
            
            # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
            return render_template('index.html', prediction = pred_price)
        
       
    except:
        print(traceback.print_exc())
        return redirect(url_for('/'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
 