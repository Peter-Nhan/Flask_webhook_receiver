import urllib3
import json
import os
import time
import cryptography
from flask import Flask, render_template, request, abort, send_from_directory
from flask_basicauth import BasicAuth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings
from config import WEBHOOK_USERNAME, WEBHOOK_PASSWORD
save_webhook_output_file = "all_webhooks_detailed.json"

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = WEBHOOK_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = WEBHOOK_PASSWORD

# If true, then site wide authentication is needed
# otherwise if false - authentication is used only where @basic_auth.required configured
# only used for app.route is "/" and "webhook"
app.config['BASIC_AUTH_FORCE'] = False

basic_auth = BasicAuth(app)

@app.route("/")   # create a route for / - just to test server is up.
@basic_auth.required   # Authenticate this request
def index():
    return '<h1>Flask Receiver App is Up!</h1>', 200

# Access the logs via the Web 
@app.route("/log", methods=['GET'])  # create a route for /log, method GET
def log():
    with open('all_webhooks_detailed.json', "r") as f: 
        content_of_file = f.read() 
    return render_template('bootstrap.html', content_var = content_of_file, filename_var = "all_webhooks_detailed.json")

@app.route('/webhook', methods=['POST'])  # create a route for /webhook, method POST
@basic_auth.required   # Authenticate this request
def webhook():
    if request.method == 'POST':
        print('Webhook Received')
        request_json = request.json

        # print the received notification
        print('Payload: ')
        # Change from original - remove the need for function to print
        print(json.dumps(request_json,indent=4))

        # save as a file, create new file if not existing, append to existing file
        # full details of each notification to file 'all_webhooks_detailed.json'
        # Change above save_webhook_output_file to a different filename

        with open(save_webhook_output_file, 'a') as filehandle:
            # Change from original - we output to file so that the we page works better with the newlines.
            filehandle.write('%s\n' % json.dumps(request_json,indent=4))
            filehandle.write('= - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - \n')

        return 'Webhook notification received', 202
    else:
        return 'POST Method not supported', 405

if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0', port=5443, debug=True)
    # Set to use HTTPS with port 5443
