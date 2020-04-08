from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

# @app.route('/<username>')
# def hello_world(name=username):
#     return 'name'


@app.route('/')
def myhome():
	return render_template('index.html')

@app.route('/<string:page_name>')
def htmlp_page(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return render_template('/thankyou.html',data=data)
		except:
			return 'did not save to database'
	else:
		return 'something went wrong try again'


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject =  data['subject']
		message =  data['message']
		file = database.write(f'\n Email: {email} , Subject: {subject} , Message: {message}')


def write_to_csv(data):
	with open('database.csv',newline='' , mode='a') as database2:
		email = data['email']
		subject =  data['subject']
		message =  data['message']
		csv_writer = csv.writer(database2,delimiter=',' , quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

# @app.route('/<username>/<int:post_id>')
# def home_page(username = None,post_id = 0):
# 	return render_template('./index.html',name=username,post_id = post_id)

# @app.route('/about')
# def about():
# 	return render_template('./about.html')

# @app.route('/favicon.ico')
# def blog():
# 	return 'this is my dog'