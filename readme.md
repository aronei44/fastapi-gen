# Fastapi-Gen

## Pre Requirement

- python 3.9 or above
- docker-desktop (unnecesary if you have your own database)

## Installation

- clone this project
```
git clone https://github.com/aronei44/fastapi-gen.git
```
- copy env file
```
cp .env.example .env
```
- build with desktop (skip this if you not using docker)
```
docker-compose up --build
```
- run app (skip this if you using docker)
```
pip install -r requirements.txt
uvicorn main:app --reload
```

## Command

you can do command by:

```
py gen.py {command:subcommand} {name}
```

available commands:

- ```make:controller nameController``` `: for generating basic controller

- ```make:model nameModel```            : for generating basic model

- ```make:route nameRoute```            : for generating basic route

- ```help```                            : for hints
