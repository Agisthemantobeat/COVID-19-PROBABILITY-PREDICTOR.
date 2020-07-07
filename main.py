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
        fever=float(mydict['fever'])
        Age=int(mydict['Age'])
        Headache=mydict['headache']
        Cough=mydict['cough1']
        diffBreath=mydict['diffbreath']
        sorethroat=mydict['sorethroat']
        test=mydict['test']
        if test=='option1':
            t=0.5
        elif test=='option2':
            t=1
        else:
            t=0
        if Headache=="option1":
            k=1
     
        else:
             k=0
        if fever>100.4:
            f=1
        else:
            f=0
        if Cough=="Yes":
            l=1
        elif Cough=="No":
            l=0
        if  diffBreath=="option1":
            m=1  
        else:
            m=0 
        if Age>=60:
            a=1
        else:
            a=0
        if sorethroat=='option1':
                s=1
        else:
                s=0
        
        inputfeatures= [f,k,s,a,l,m,t]
        print([f,k,s,a,l,m,t])
        infProb= dictname.predict_proba([inputfeatures])[0][1]
        print(infProb)
        if infProb>0.01:
            infProb=0.009
        print(infProb)
        return render_template('show.html',inf= round(infProb*1000,2))
    return render_template('index.html')
    



if __name__ == "__main__":
         app.run(debug=True)
         hello_world()        #This method call is necessary for the server to start up. So don't forget to keep it.
         