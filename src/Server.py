from flask import Flask,request
import Driver
import json

def setup():
    Driver.Train()
    print("Training completed")
    return

app=Flask(__name__)

@app.route("/predict",methods=["GET","POST"])
def predictNextSubject():
    if(request.method=="POST"):
        try:
            data=request.get_json();
            student=[data["ID"],data["FI"]]
            student.extend([s for s in data["S"] ]); #it should not contai any none and undefined
            nextSubject, nextSubjectDifficulty, maxDifficultyStudent,allowableSubjects=Driver.PredictForServer(student);
            print("Next Subject",nextSubject);
            reply={
                "nextSubject":nextSubject,
                "status":0,
                "error":"None",
                "nextSubjectDifficulty":nextSubjectDifficulty,
                "maxDifficultyStudent":maxDifficultyStudent,
                "allowableSubjects":allowableSubjects
            }
            print(json)
            return json.dumps(reply)
        except Exception as e:
            print(e)
            reply={
                "status":1,
                "error":str(e)
            }
            if(str(e)=="MD"):
                reply["status"]=2
            return json.dumps(reply)

def setupDriver():
    Driver.Train()


if __name__ == '__main__':
    setupDriver()
    app.run(debug=True)
