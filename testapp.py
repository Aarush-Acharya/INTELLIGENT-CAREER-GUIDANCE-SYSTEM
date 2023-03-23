from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)


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
      print(pred)
      return jsonify({"Your Recommended Job":ans})

      
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5675)
