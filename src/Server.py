from flask import Flask,request,render_template
import Driver
import json
import  os


def setup():
    Driver.Train()
    print("Training Comlplete")
    return

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("predictHome.html")


@app.route("/predict",methods=["GET","POST"])
def predictNextSubject():
    if(request.method=="POST"):
        try:
            data=request.get_json();
            student=[data["ID"],data["FI"]]
            student.extend([s for s in data["S"] ]); #it should not contain any none and undefined
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



if __name__ == '__main__':
    port=int(os.environ.get("PORT",5000));
    setup()
    app.run(host="0.0.0.0",port=port,debug=True)
