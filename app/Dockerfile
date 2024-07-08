FROM ubuntu:latest
LABEL authors="pranavvedma"

ENTRYPOINT ["top", "-b"]

# Use an official python runtime as a image
FROM python:3.9

# The Expose instruction indicates the ports on which a container
EXPOSE 8000

# Sets the working directory for following COPY and CMD instructions
WORKDIR /app

ADD . /app
RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt
ENV PYTHONPATH /app
# Run app.py when the container launches
CMD gunicorn -b 0.0.0.0:8000 app:app --workers=5

