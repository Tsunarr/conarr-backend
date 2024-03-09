FROM alpine:3.19

RUN apk update --no-cache &&\
  apk add --no-cache \
  python3 \
  py3-pip
