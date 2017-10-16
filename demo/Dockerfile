FROM python:3.6

RUN apt-get update && apt-get install -y \
  vim \
  --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY eid_server /eid_server
WORKDIR /eid_server
COPY requirements.txt /eid_server/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt  

EXPOSE 8877
CMD ["python3", "run.py"]
