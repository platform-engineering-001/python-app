FROM python:3.10-alpine 

WORKDIR /app  

COPY ./requirements.txt . 
RUN pip install -r requirements.txt --no-cache-dir 

COPY ./src /src 

CMD python /src/app.py 