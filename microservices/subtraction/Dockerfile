FROM python:3.8-alpine
COPY  ./app/requirements.txt /app/requirements.txt 
WORKDIR /app
RUN apk add --update \
    && pip install --upgrade pip  \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*
COPY ./app /app
CMD python app.py


# From : create this layer
# COPY : adding files from the client current directory
# WORKDIR : client directory
# RUN : builds application with make
# CMD : specifies the command run within the contaier