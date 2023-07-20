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
    final = []
    result = subprocess.run(['python3', 'playMain.py'], capture_output=True, text=True).stdout
    
    with open("relatorio.txt","r+") as f:
        f.write(result)
        f.close()
    with open("relatorio.txt","r+") as f:
        for line in (f.readlines() [-2:]):
            banco.relatorio.append(line)

    
    #banco.relatorio.append(final)
    return banco.relatorio

app.debug=True

app.run()