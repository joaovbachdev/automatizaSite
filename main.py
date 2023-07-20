import flask, json
import banco
from flask_cors import CORS
import subprocess

app = flask.Flask("automatiza")
CORS(app)

@app.route("/teste",methods=['GET','POST'])
def teste():
    return json.dumps(banco.relatorio)

@app.route("/testePost",methods=['GET'])
def testPost():
    result = subprocess.run(['python3', 'playMain.py'], capture_output=True, text=True).stdout
    banco.relatorio.append(result)
    return banco.relatorio





app.debug=True

app.run()