FROM python:3.6.15-slim-bullseye

# install environment dependencies
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        netcat \
    && apt-get -q clean

# set working directory
WORKDIR /app

# add requirements
COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY entrypoint.sh .

# add app
COPY . .

# # Provide execution right to the entrypoint.sh
# RUN sudo chmod +x entrypoint.sh 

# run server
CMD ["./entrypoint.sh"]