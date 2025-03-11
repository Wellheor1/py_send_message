FROM python:3.12.2-alpine3.19
LABEL authors="well"
WORKDIR /workspaces
COPY . /workspaces/
RUN pip3 install -r requirements.txt
CMD uvicorn main:app --reload --host 0.0.0.0