FROM python:3.11.3-alpine3.18
LABEL maintainer="railsonp560@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add libffi-dev

COPY djangoapp /djangoapp
COPY scripts /scripts

WORKDIR /djangoapp
EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /djangoapp/templates && \
    mkdir -p /djangoapp/static && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /djangoapp/templates && \
    chown -R duser:duser /djangoapp/static && \
    chmod -R 755 /djangoapp/templates && \
    chmod -R 755 /djangoapp/static && \
    chmod -R +x /scripts

RUN apk del build-deps

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh"]

