from flask import Flask ,render_template,request

app = Flask(__name__)
import pickle
with open("models.pkl", "rb") as f:
    dictname = pickle.load(f)
k=0
l=0
m=0
@app.route('/',methods=["GET","POST"])
def hello_world():
    global k,l,m
    if request.method=='POST':
        mydict=request.form
        fever=int(mydict['fever'])
        Age=int(mydict['Age'])
        BodyPain=mydict['BodyPain1']
        runnynose1=mydict['runnynose']
        print(runnynose1)
        diffBreath=mydict['diffbreath']
        if BodyPain=="option1":
            k=-1
        elif BodyPain=="option2":
            k=0
        else:
            k=1
        if runnynose1=="Yes":
            l=1
        elif runnynose1=="No":
            l=0
        if  diffBreath=="option1":
            m=-1
        elif diffBreath=="option2":
            m=0
        else:
            m=1 
        
        inputfeatures= [fever,k,Age,l,m]
        print([fever,k,Age,l,m])
        infProb= dictname.predict_proba([inputfeatures])[0][1]
    #return 'Hello, World!'+' '+str(infProb)
        print(infProb)
        return render_template('show.html',inf= round(infProb*100))
    return render_template('index.html')
    



if __name__ == "__main__":
         app.run(debug=True)
         hello_world()        #This method call is necessary for the server to start up. So don't forget to keep it.
         