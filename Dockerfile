FROM python:3.10-slim-buster

# install headless firefox
RUN apt-get update && apt-get install -y \
  firefox-esr \
  && rm -rf /var/lib/apt/lists/*

# install pipenv and update pip
RUN pip install --upgrade pipenv pip

COPY . .

# install requirements to system
RUN pipenv install --system --deploy --ignore-pipfile

# run the app
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
