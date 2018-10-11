# importing files
from flask import Flask, render_template, request

import firstyear
import fourthyear
import secondyear
import thirdyear

# app name

app = Flask(__name__)


# app route for main page
@app.route('/', methods=['GET', 'POST'])
def home():
    # deleting all file in the folder
    # folder = 'static/temp/'
    # for the_file in os.listdir(folder):
    # 	file_path = os.path.join(folder, the_file)
    # 	try:
    # 		if os.path.isfile(file_path):
    # 			os.unlink(file_path)
    # 	except Exception as e:
    # 		print(e)

    print('Method is ', request.method)
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':

        year = int(request.form.get('year'))
        batch = request.form.get('batch').upper()
        # returning dictionary from module
        if year == 1:
            tt_dict = firstyear.first(batch)
        elif year == 2:
            tt_dict = secondyear.second(batch)
        elif year == 3:
            tt_dict = thirdyear.third(batch)
        elif year == 4:
            tt_dict = fourthyear.fourth(batch)

    try:
        pass
    except Exception as e:
        return render_template("timetable.html", tt_dict=tt_dict)

    return render_template("timetable.html", tt_dict=tt_dict)


if (__name__ == '__main__'):
    app.run(debug=True, use_reloader=True)
