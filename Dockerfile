FROM python:3.12.2-alpine3.19
LABEL authors="well"
WORKDIR /workspaces
COPY . /workspaces/
RUN ["pip3", "install", "poetry"]
RUN ["poetry", "install"]
#CMD ["uvicorn", "main:app", "--reload"]