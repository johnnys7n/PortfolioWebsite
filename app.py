from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('./index.html')


@app.route("/<string:page_name>", methods=['POST','GET'])
def html_page(page_name):
    if request.method == 'POST':
        return render_template(form=form)
    else:
        return render_template(page_name)

# # Code to save contact form information to csv then later database
# def contacts_to_csv(data):
#     with open('database.csv', 'a', newline ='') as database:
#         name = data['name']
#         email = data['email']
#         subject = data['subject']
#         message = data['message']

#         csv_writer = csv.writer(database, delimiter =',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email, subject, message])

# @app.route('/index.html#contact', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             contacts_to_csv(data)
#             return redirect('/thankyou.html')
#         except:
#             return 'did not save to database'
#     else: 
#         return 'something went wrong. Try again'

if __name__ == '__main__':
    app.run()
