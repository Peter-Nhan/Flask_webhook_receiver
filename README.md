# Changes
Made some changes from the fork please see https://peter-nhan.github.io/Webhook-Python-Curl-DNAC/
for more details.
* flask_rx.py - modified the original - flask webhook receiver, it will listen on active interface, will save webhook received to file and display it on the screen.
* flask_rx_web_view.py - improves on previous webhook receiver and adds a web portal to view the log - browse to https://x.x.x.x/log
* test_webhook.py - un-modified from fork - clients that fires webhook notification at the receiver. Modified config.py with IP address of webhook receiver.
* config.py - used variable WEBHOOK_URL is on used by test_webhook.py, all other variables are used by every python files.

# To use
To Send notifications.
```
$ python3 test_webhook.py
```
To use either 
```
$ python3 flask_rx.py
 * Serving Flask app 'flask_rx' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on https://172.16.1.16:5443/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 788-486-105
```
or 
```
$ python3 flask_rx_web_view.py
 * Serving Flask app 'flask_rx_web_view' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on https://172.16.1.16:5443/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 788-486-105

```
Browse to the receiver via web browser - use appropriate IP - https://x.x.x.x/log


---
# Cisco DNA Center Webhook Receiver

This repo is for a simple Flask application that will receive webhooks notifications. 
This app is to be used only in demo or lab environments, it is not written for production. Please follow these
 recommendations for production deployments: https://flask.palletsprojects.com/en/1.1.x/deploying/.

The "flask_receiver.py" will save the notification to a file, and it will not process the notification.

Users my continue the development of this application to parse the received event notification and take the next
 steps based on their use case.

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment to run the Flask App as a Webhook Receiver

**Usage**

 - Create a new Flask App to receive Cisco DNA Center notifications
 - "flask_receiver.py" - webhook receiver 
 - "config.py" - configure your lab environment
 - "test_webhook_receiver" - app to test the webhook receiver without Cisco DNA Center
 - The notifications received will be save to the file "all_webhooks_detailed.log"
 - Start the Flask App
 - Test by browsing to your receiver home page
 - Configure Cisco DNA Center Webhooks to send notifications to your new receiver
 - Trigger events for the configured webhooks
 - Verify the events are received by the webhook receiver
 - Sample Output:
   - from "test_webhook_receiver.py":
   
      Webhook notification status code:  202

      Webhook notification response:  Webhook notification received
   
   - from "flask_receiver.py":
        ```python
        WARNING: This is a development server. Do not use it in a production deployment.
           Use a production WSGI server instead.
         * Debug mode: on
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 764-976-195
        127.0.0.1 - - [17/Nov/2020 13:52:42] "POST /webhook HTTP/1.1" 202 -
        Webhook Received
        Payload: 
        {
            "version" : "" , 
            "instanceId" : "ea6e28c5-b7f2-43a4-9937-def73771c5ef" , 
            "eventId" : "NETWORK-NON-FABRIC_WIRED-1-251" , 
            "namespace" : "ASSURANCE" , 
            "name" : "" , 
            "description" : "" , 
            "type" : "NETWORK" , 
            "category" : "ALERT" , 
            "domain" : "Connectivity" , 
            "subDomain" : "Non-Fabric Wired" , 
            "severity" : 1 , 
            "source" : "ndp" , 
            "timestamp" : 1574457834497 , 
            "tags" : "" , 
            "details" : {
                "Type" : "Network Device" , 
                "Assurance Issue Priority" : "P1" , 
                "Assurance Issue Details" : "Interface GigabitEthernet1/0/3 on the following network device is down: Local Node: PDX-M" , 
                "Device" : "10.93.141.17" , 
                "Assurance Issue Name" : "Interface GigabitEthernet1/0/3 is Down on Network Device 10.93.141.17" , 
                "Assurance Issue Category" : "Connectivity" , 
                "Assurance Issue Status" : "active"
            } , 
            "ciscoDnaEventLink" : "https://10.93.141.35/dna/assurance/issueDetails?issueId=ea6e28c5-b7f2-43a4-9937-def73771c5ef" , 
            "note" : "To programmatically get more info see here - https://<ip-address>/dna/platform/app/consumer-portal/developer-toolkit/apis?apiId=8684-39bb-4e89-a6e4" , 
            "tntId" : "" , 
            "context" : "" , 
            "tenantId" : ""
        }
```

 
 This sample code is for proof of concepts and labs

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
