# Use an official Python runtime as a parent image
FROM python:3.6-stretch

RUN git clone https://github.com/enibeni/OTUS_HW.git /opt/app

# Set the working directory to /app
WORKDIR /opt/app

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt