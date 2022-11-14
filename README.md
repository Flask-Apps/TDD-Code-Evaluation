# TDD

![example workflow](https://github.com/Flask-Apps/TDD-Code-Evaluation/actions/workflows/docker-image.yml/badge.svg)
<br>
![example event parameter](https://github.com/Flask-Apps/TDD-Code-Evaluation/actions/workflows/docker-image.yml/badge.svg?event=push)
<br>
![example branch parameter](https://github.com/Flask-Apps/TDD-Code-Evaluation/actions/workflows/docker-image.yml/badge.svg?branch=main)

## Important Terms

### Code coverage

- it is the process of finding areas of our code that aren't exercised by tests.
- this however doesn't measure the overall effectiveness of the test suite.

## things to remember

- change the permission of the
  - entrypoint.sh on host `chmod +x services/users/entrypoint.sh`
  - `chmod +x services/users/entrypoint-prod.sh`
- if users relation doesn't exist pop up then run the recreate-db command

## Getting docker-machine

- [Setting up docker machine](https://blog.knoldus.com/how-to-launch-ec2-instance-in-aws-using-docker-machine/)
- [Why to use docker-machine?](https://docker-docs.netlify.app/machine/overview/#why-should-i-use-it)
- [docker-machine autocomplete for zsh](https://docker-docs.netlify.app/machine/completion/#zsh)

## Create a new host on ec2

- `docker-machine create --driver amazonec2 \
  --amazonec2-instace-type "t2.micro" \
  --amazonec2-region "ap-south-1" \
  --amazonec2-open-port 5001 \
  tdd-prod`

## RUN THESE

- run
  - `docker-compose build`
  - `docker-compose up`
  - `make recreate`
  - enter into the users-db and connect `\c users_dev` and check `\dt`
