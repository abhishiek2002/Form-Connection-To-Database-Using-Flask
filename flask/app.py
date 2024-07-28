from flask import Flask,render_template,url_for,request
import mysql.connector as mc


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('service.html')

@app.route('/contacts')
def contacts():
    return render_template('contact.html')

@app.route('/query')
def query():
    return render_template('query.html')

@app.route('/user_query',methods=['GET','POST'])
def user_query():
    if request.method == "POST":
        # connecting to database


        conn = mc.connect(host='localhost' , user = 'root' ,password = 'Abhishek@2002', database = 'userdata')


        name=request.form['name']
        age=int(request.form['age'])
        address=request.form['address']
        college=request.form['college']
        query=request.form['query']

        user_data = (name,age,address,college,query)
    

        insert_data_query = """
        insert into user_record (name,age,address,college,query) values 
        (%s,%s,%s,%s,%s)
        """

        cur = conn.cursor()


        cur.execute(insert_data_query,user_data)

        print("You have successfully inserted")
        conn.commit()

        cur.close()
        conn.close()


        return "Your data is submitted!"
    

if __name__=="__main__":
    app.run(debug=True)
