FROM node:16
ARG USER_ID=0
RUN groupmod -g 1001 node \
  && usermod -u 1001 -g 1001 node
RUN mkdir -p /home/appuser
RUN chown -R ${USER_ID}:${USER_ID} /home/appuser
RUN groupadd -r appuser
RUN useradd -r -u ${USER_ID} -g appuser appuser
USER appuser
RUN npm config set prefix '/home/appuser/.npm-global'
RUN npm install -g @vue/cli
RUN export PATH=$PATH:~/.npm-global/bin
WORKDIR /code