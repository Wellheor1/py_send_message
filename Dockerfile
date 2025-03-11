FROM python:3.12.2-alpine3.19
LABEL authors="well"
WORKDIR /workspaces
COPY . /workspaces/
RUN pip3 install -r requirements.txt
CMD uvicorn main:app --reload --host 0.0.0.0
#RUN python3 -m venv .v
#RUN poetry install
#RUN /bin/sh -c pip3 install poetry && python3 -m venv .venv && source .venv/bin/activate && poetry install
#RUN ["poetry", "install"]
#CMD ["uvicorn", "main:app", "--reload"]