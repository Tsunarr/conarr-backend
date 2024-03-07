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
  npm install -g \
  '@usebruno/cli@1.9.2' \
  '@aws-sdk/credential-providers@<3.529.0' \
  '@aws-sdk/core@<3.529.0' \
  '@aws-sdk/client-sts@<3.529.0' \
  '@aws-sdk/client-cognito-identity@<3.529.0' \
  '@aws-sdk/client-sso@<3.529.0' \
  '@aws-sdk/credential-provider-cognito-identity@<3.529.0' \
  '@aws-sdk/credential-provider-env@<3.529.0' \
  '@aws-sdk/credential-provider-http@<3.529.0' \
  '@aws-sdk/credential-provider-ini@<3.529.0' \
  '@aws-sdk/credential-provider-node@<3.529.0' \
  '@aws-sdk/credential-provider-process@<3.529.0' \
  '@aws-sdk/credential-provider-sso@<3.529.0' \
  '@aws-sdk/credential-provider-web-identity@<3.529.0' \
  '@aws-sdk/types@<3.529.0' &&\
  groupmod -g 1337 docker && \
  usermod -aG docker vscode &&\
  usermod -aG root vscode &&\
  echo "alias ll='ls -l'" >> /home/vscode/.bashrc

USER vscode

HEALTHCHECK CMD [ "/bin/true" ]
