FROM jupyter/minimal-notebook
ARG TOKEI_VERSION=v12.0.4
ADD . work/
USER root
# sub optimal
RUN apt update && \
      apt install -y curl vim && \
      curl -LO https://github.com/XAMPPRocky/tokei/releases/download/$TOKEI_VERSION/tokei-x86_64-unknown-linux-gnu.tar.gz && \
      tar xvz -C /usr/local/bin -f tokei-x86_64-unknown-linux-gnu.tar.gz && \
      pip install -r work/requirements.txt
USER jovyan
