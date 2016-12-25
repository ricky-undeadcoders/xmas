from jazzdd/alpine-flask
MAINTAINER Ricky Whitaker

EXPOSE 80

# application folder
ENV APP_DIR /app

VOLUME [${APP_DIR}]
WORKDIR ${APP_DIR}

ENTRYPOINT ["/entrypoint.sh"]
