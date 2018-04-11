# Begin with the Python 3.4 image
FROM python:3.6.4

MAINTAINER Scott Numamoto <scott.numamoto@gmail.com>

# Set the working directory to /code
WORKDIR /website

# Add the local directory to the working dir, /website
ADD . .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Set the default command
CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:8000"] 
