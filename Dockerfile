FROM python:3   
LABEL maintainer="Zhifan Lan <zlan1@ualberta.ca>"
WORKDIR /app

ADD . /app
RUN pip install -r requirements.txt


EXPOSE 8080
ENTRYPOINT ["python", "src/app.py"]