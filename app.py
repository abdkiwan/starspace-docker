
from flask import Flask
import os

app = Flask(__name__)
@app.route("/publications")
def run_publications():

    fun_output = ''
    command = './Starspace/starspace test -label __label__ -trainMode 0 -testFile publications_test_1.csv -model ' \
              'publications_model ' \
              '-predictionFile publications_preds_1.txt'
    stream = os.popen(command)
    cmd_output = stream.read()
    cmd_output = cmd_output.split('Evaluation Metrics :')[1]
    fun_output += 'Evaluation of publications test 1 : \n'
    fun_output += cmd_output
    fun_output += '\n'

    command = './Starspace/starspace test -label __label__ -trainMode 0 -testFile publications_test_2.csv -model ' \
              'publications_model ' \
              '-predictionFile publications_preds_2.txt'
    stream = os.popen(command)
    cmd_output = stream.read()
    cmd_output = cmd_output.split('Evaluation Metrics :')[1]
    fun_output += 'Evaluation of publications test 2 : \n'
    fun_output += cmd_output
    fun_output += '\n'

    return fun_output


@app.route("/patents")
def run_patents():

    fun_output = ''
    command = './Starspace/starspace test -label __label__ -trainMode 0 -testFile patents_test_1.csv -model ' \
              'patents_model ' \
              '-predictionFile patents_preds_1.txt'
    stream = os.popen(command)
    cmd_output = stream.read()
    cmd_output = cmd_output.split('Evaluation Metrics :')[1]
    fun_output += 'Evaluation of patents test 1 : \n'
    fun_output += cmd_output
    fun_output += '\n'

    command = './Starspace/starspace test -label __label__ -trainMode 0 -testFile patents_test_2.csv -model ' \
              'patents_model ' \
              '-predictionFile patents_preds_2.txt'
    stream = os.popen(command)
    cmd_output = stream.read()
    cmd_output = cmd_output.split('Evaluation Metrics :')[1]
    fun_output += 'Evaluation of patents test 2 : \n'
    fun_output += cmd_output
    fun_output += '\n'

    return fun_output


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)