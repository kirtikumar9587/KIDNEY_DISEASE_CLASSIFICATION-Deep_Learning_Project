#in this write thr docker command # then install python and then install awscli because going to deploy app to aws app 
#thencreating one directory app and copying all the source code inside this app and install allrequirements
#then run app.py because it is end point

FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]