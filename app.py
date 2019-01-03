#importing files
from flask import Flask,render_template,request,redirect,url_for,send_from_directory,jsonify,abort
import os
import imgkit
import secondyear
import thirdyear
import firstyear
import fourthyear


#app name
app=Flask(__name__)


#app route for main page
@app.route('/', methods=['GET', 'POST'])
def home():
	#deleting all file in the folder
	# folder = 'static/temp/'
	# for the_file in os.listdir(folder):
	# 	file_path = os.path.join(folder, the_file)
	# 	try:
	# 		if os.path.isfile(file_path):
	# 			os.unlink(file_path)
	# 	except Exception as e:
	# 		print(e)
	if request.method == 'GET':
		return render_template("index.html")
	elif request.method == 'POST':
		
		year=int(request.form.get('year'))
		batch=request.form.get('batch').upper()
		#returning dictionary from module
		if year==2:
			tt_dict=secondyear.second(batch)
		elif year==3:
			tt_dict=thirdyear.third(batch)
		elif year==1:
			tt_dict=firstyear.first(batch)
		elif year==4:
			tt_dict=fourthyear.fourth(batch)

		try:


			pass
		except Exception as e:
			return render_template("timetable.html",tt_dict=tt_dict)


			
			
	
	return render_template("timetable.html",tt_dict=tt_dict)

@app.route('/api/<int:year>/<batch>', methods=['GET'])
def get_task(year,batch):
	batch=batch.upper()
	if year==2:
		tt_dict=secondyear.second(batch)
	elif year==3:
		tt_dict=thirdyear.third(batch)
	elif year==1:
		tt_dict=firstyear.first(batch)
	elif year==4:
		tt_dict=fourthyear.fourth(batch)
	return jsonify(tt_dict)


if(__name__=='__main__'):
	app.run(debug=True,use_reloader=True)
