FROM neosapience/appname-api:base

# RUN pip install --no-cache-dir \
#     gevent boto3 celery redis

COPY ./api .
ARG MYAPP_API_VERSION
ENV MYAPP_API_VERSION=$MYAPP_API_VERSION

EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD [ "gunicorn" ]
