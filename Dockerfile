FROM python:3.9 as requirements-stage

WORKDIR /tmp
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes



FROM python:3.9 as deploy-stage

COPY --from=requirements-stage /tmp/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

WORKDIR /meter_app

COPY . /meter_app

EXPOSE 5000

CMD [ "python3", "app.py"]