FROM python:3.7.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
# RUN apt update && apt install -y curl procps vim --force-yes
COPY . /app/
CMD ["/usr/local/bin/uwsgi", "--ini", "/app/uwsgi.ini"]
