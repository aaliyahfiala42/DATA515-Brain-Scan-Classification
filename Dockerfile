FROM python:3.8.1

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./brain_scan /app/brain_scan

ENTRYPOINT [ "python" ]

CMD [ "brain_scan/app.py" ]