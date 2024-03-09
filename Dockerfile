FROM alpine:3.19

ARG PYCONARR_VERSION

RUN apk update --no-cache &&\
  apk add --no-cache \
  python3 \
  py3-pip &&\
  pip install --break-system-packages pyconarr==${PYCONARR_VERSION}

COPY config/pyconarr.yml.sample /config/pyconarr.yml

ENTRYPOINT [ "uvicorn", "pyconarr.main:app" ]
