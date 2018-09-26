from flask import Flask,request
import Driver


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
            nextSubject=Driver.PredictForServer(student);
            print("Next Subject",nextSubject);
            returnString="{"+ "\"nextSubject\":\" "+"{}".format(nextSubject)+"\"}";
            return returnString
        except:
            return 'Error'
    return "Working"

def setupDriver():
    Driver.Train()


if __name__ == '__main__':
    setupDriver()
    app.run(debug=True)
