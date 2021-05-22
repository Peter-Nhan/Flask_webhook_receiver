import urllib3
import json
import os
import time


from flask import Flask, request, abort, send_from_directory
from flask_basicauth import BasicAuth

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings


os.environ['TZ'] = 'Australia/Sydney'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

from config import WEBHOOK_URL, WEBHOOK_USERNAME, WEBHOOK_PASSWORD


def pprint(json_data):
    """
    Pretty print JSON formatted data
    :param json_data:
    :return:
    """
    print(json.dumps(json_data, indent=4, separators=(' , ', ' : ')))


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = WEBHOOK_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = WEBHOOK_PASSWORD
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)


@app.route('/')  # create a page for testing the flask framework
@basic_auth.required
def index():
    return '<h1>Flask Receiver App is Up!</h1>', 200


@app.route('/webhook', methods=['POST'])  # create a route for /webhook, method POST
@basic_auth.required
def webhook():
    if request.method == 'POST':
        print('Webhook Received')
        request_json = request.json

        # print the received notification
        print('Payload: ')
        pprint(request_json)

        # save as a file, create new file if not existing, append to existing file
        # full details of each notification to file 'all_webhooks_detailed.json'

        with open('all_webhooks_detailed.json', 'a') as filehandle:
            filehandle.write('%s\n' % json.dumps(request_json))

        # steps required by the notification
        notification = request_json

        return 'Webhook notification received', 202
    else:
        return 'POST Method not supported', 405


if __name__ == '__main__':
    # HTTPS enable - toggle on eby un-commenting
    app.run(ssl_context='adhoc', host='0.0.0.0', port=5443, debug=True)
    # HTTP ONLY enable - toggle on eby un-commenting
    # app.run(host='0.0.0.0', port=5443, debug=True)
# make sure firewall is not block 5443
# $ sudo ufw allow 5443
# if 'inactive' response means firewall is not on.
# 
# Use the following to see if the port is listen for flask.
# $ sudo lsof -i -P -n | grep LISTEN
#
# Test with:
# $ curl --user "username:password" --header "Content-Type: application/json" --request POST --data '{"emailAddress":"pnhan@cisco.com"}' http://10.66.69.22:5443/webhook
# OR
# $ python3 test_webhook.py
