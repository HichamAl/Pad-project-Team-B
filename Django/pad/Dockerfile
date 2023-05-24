# base image 
FROM python:3.8-buster

# setup environment variable  
ENV PYTHONBUFFERED=1 

# where your code lives  
WORKDIR /website

# copy whole project to your docker home directory. 
COPY requirements.txt requirements.txt

# run this command to install all dependencies  
RUN pip install -r requirements.txt  

COPY . .

# start server  
CMD python manage.py runserver 

# port where the Django app runs  
EXPOSE 8000 
