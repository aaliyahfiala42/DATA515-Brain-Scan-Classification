FROM python:3.8.1

COPY ./brain_scan /app/brain_scan

COPY README.md /app/README.md

COPY setup.py app/setup.py

WORKDIR /app

RUN pip install -e .

RUN pip install 'h5py==2.10.0' --force-reinstall

ENV FLASK_APP=brain_scan/app.py

CMD [ "flask", "run", "--host", "0.0.0.0" ]