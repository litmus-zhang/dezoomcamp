from python:3.10

RUN  pip install pandas

WORKDIR /app

COPY  load_data.py /app/
COPY requirements.txt /app/

ENTRYPOINT [ "python", "load_data.py" ]