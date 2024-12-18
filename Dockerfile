# kics-scan disable=d3499f6d-1651-41bb-a9a7-de925fea487b,02d9c71f-3ee8-4986-9c27-1a20d0d19bfc
FROM alpine:3.21

ARG PYCONARR_VERSION
EXPOSE 8000

RUN apk upgrade --no-cache &&\
  apk add --no-cache \
  python3 \
  py3-pip \
  py3-virtualenv &&\
  adduser -D pyconarr

WORKDIR /home/pyconarr/

COPY config/pyconarr.yml.sample config/pyconarr.yml
COPY config/log.yaml config/log.yaml
COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

USER pyconarr
RUN virtualenv .venv &&\
  .venv/bin/pip install --no-cache-dir --upgrade pip &&\
  .venv/bin/pip install --no-cache-dir pyconarr==${PYCONARR_VERSION}

ENTRYPOINT [ "./entrypoint.sh" ]
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD [ "nc", "localhost", "8000" ]
