#BASE IMAGE
FROM python:latest

RUN echo "ASdas"
# set working directory
RUN mkdir -p /app
WORKDIR /app

#COPY the current scrits inside of the container
COPY . /app

#Install all the dependencies
RUN pip install -r dependencies.txt


ENTRYPOINT ["python3"]

EXPOSE 80