# Use the Python 3.6.9 image
FROM python:3.6.9-stretch

WORKDIR /client

# Copy current directory contents into the container at /client
ADD . /client

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y fonts-liberation
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN rm chromedriver_linux64.zip
RUN wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver 

# start uWSGI
CMD ["uwsgi", "app.ini"]
