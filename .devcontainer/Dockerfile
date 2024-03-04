# kics-scan disable=d3499f6d-1651-41bb-a9a7-de925fea487b,e36d8880-3f78-4546-b9a1-12f0745ca0d5
FROM mcr.microsoft.com/vscode/devcontainers/base:alpine-3.19

COPY pip.conf /etc/pip.conf

RUN apk add --no-cache git \
  python3 \
  docker \
  py3-pip \
  go-task \
  py3-hatchling \
  npm &&\
  pip install --no-cache-dir poetry==1.7.1 &&\
  npm install -g @usebruno/cli@1.9.2 &&\
  groupmod -g 1337 docker && \
  usermod -aG docker vscode &&\
  usermod -aG root vscode &&\
  echo "alias ll='ls -l'" >> /home/vscode/.bashrc

USER vscode

HEALTHCHECK CMD [ "/bin/true" ]
