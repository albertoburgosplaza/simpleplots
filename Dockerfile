FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    cmake \
    curl \
    gcc \
    git \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libgtk2.0-dev \
    locales \
    net-tools \
    wget \
    zsh
	
RUN rm -rf /var/lib/apt/lists/*

ENV ZSH_THEME agnoster
RUN locale-gen en_US.UTF-8
RUN /bin/sh -c chsh -s /bin/zsh

ENV SHELL /bin/zsh
ENV LANG=en_US.UTF-8

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda create -y -n ml python=3.7

COPY requirements.txt /
RUN /bin/zsh -c "source activate ml && pip install -r requirements.txt"
RUN rm -f requirements.txt

RUN echo "source activate ml" >> /root/.zshrc