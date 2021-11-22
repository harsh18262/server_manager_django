FROM python:3.7-slim
#ADD . /code
RUN mkdir /code

ADD run.sh /
RUN \
  groupadd -r webssh && \
  useradd -r -s /bin/false -g webssh webssh && \
  chmod +x /run.sh && \
  pip install webssh

RUN apt-get update;apt-get install git -y;
RUN git clone https://github.com/harsh18262/server_manager_django.git ./code
RUN rm -r /code/.git
RUN chown -R webssh:webssh /code
WORKDIR /code
RUN pip install -r requirements.txt
 

EXPOSE 8000/tcp
EXPOSE 8080/tcp
USER webssh
#ENTRYPOINT['/bin/sh','/run.sh']

ENTRYPOINT ["/bin/sh","/run.sh"]
#CMD ["/run.sh"]
