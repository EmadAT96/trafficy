FROM ultrafunk/undetected-chromedriver

ENV DockerHome=/home/crawler/serp

RUN mkdir -p $DockerHome
WORKDIR $DockerHome

COPY requirements.txt .
RUN python -m venv env

RUN env/bin/python -m pip install --upgrade pip

RUN env/bin/python -m pip install -r requirements.txt

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get update && apt-get install -y google-chrome-stable

COPY chromedriver .
COPY main.py .

ENV PYTHONDONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN cat main.py

CMD ["env/bin/python3", "main.py"]