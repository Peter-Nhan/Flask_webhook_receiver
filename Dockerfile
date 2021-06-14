FROM python:slim
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt
CMD [ "python3", "flask_rx_web_view.py"]
