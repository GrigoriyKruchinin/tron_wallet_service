FROM python:3.12

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y wait-for-it

COPY . .

EXPOSE 8000

CMD ["/bin/bash", "run.sh"]