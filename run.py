from flask import Flask,request, render_template
import subprocess

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def index():
    data = {
            'py_code': '# Write your Python Code Hear',
            'py_output': ''
        }
    if request.method == "POST":
        print("Post request: ")
        py_code = request.form.get("pycode")
        f = open('file.py','w+')
        f.write(py_code)
        f.close()
        command = f'python3 file.py'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        py_output = output.decode()
        data['py_output'] = py_output
        data['py_code'] = py_code
        
        #return render_template('index.html',data=data)
    return render_template('index.html',data=data)


if __name__ == "__main__":
    app.debug = True
    app.run()