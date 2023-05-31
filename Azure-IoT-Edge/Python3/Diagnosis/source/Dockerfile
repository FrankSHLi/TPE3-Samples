FROM amd64/python:3.11-bullseye

COPY ./requirements.txt /app/
COPY ./*.py /app/

WORKDIR /app

#RUN apt-get update \
#    && apt-get install -y build-essential libssl-dev libffi-dev cargo \
#    && pip3 install --upgrade pip --no-cache-dir \
#    && pip3 install -r requirements.txt --no-cache-dir \
#    && apt-get remove -y build-essential libssl-dev libffi-dev cargo \
#    && apt-get autoremove -y \
#    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip --no-cache-dir \
    && pip3 install -r requirements.txt --no-cache-dir

CMD ["python", "-u", "/app/module.py"]
