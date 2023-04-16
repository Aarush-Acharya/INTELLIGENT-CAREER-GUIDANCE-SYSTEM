from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

jobs_dict = {0:'AI ML Specialist',
                   1:'API Integration Specialist',
                   2:'Application Support Engineer',
                   3:'Business Analyst',
                   4:'Customer Service Executive',
                   5:'Cyber Security Specialist',
                   6:'Data Scientist',
                   7:'Database Administrator',
                   8:'Graphics Designer',
                   9:'Hardware Engineer',
                   10:'Helpdesk Engineer',
                   11:'Information Security Specialist',
                   12:'Networking Engineer',
                   13:'Project Manager',
                   14:'Software Developer',
                   15:'Software Tester',
                   16:'Technical Writer'}

@app.route('/check', methods = ['GET'])
def career():
    return jsonify({"Success": "Granted"})

@app.route('/predict', methods = ['POST'])
def result():
   if request.method == 'POST':
    
      result = request.form
      
      stuff = result.getlist("key")
      clean_stuff = [int(numeric_string) for numeric_string in stuff]
      print([clean_stuff])
      final = [clean_stuff]
      loaded_model = pickle.load(open("careerlast.pkl", 'rb'))

      predictions = loaded_model.predict(final)

      ans = str(predictions)
      print(ans)
      ans = ans.replace("[", "")
      ans = ans.replace("]", "")
      ans = ans.replace("'", "")
      pred = loaded_model.predict_proba(final)
    #   print(pred)
      count = 0
      prob = pred[0]
      print(prob)
      ls = []
      inn = []
      for i in prob:
        print(i)
        if(i > 0.0):
            ls.append(i)
            inn.append(count)
        count = count+1
      print(ls)
      print(inn)
      jobforya = []
      for i in inn:
        jobforya.append(jobs_dict[i])
      print(jobforya)
      return jsonify({"Your Recommended Job":jobforya})
      
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5675)
