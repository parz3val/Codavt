# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Make and build stuff
RUN apk add -no-cache --virtual .build-deps gcc postgresql-dev musl-dev python3-dev
RUN apk add libpq

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

#Build dependencies
RUN apk del --no-cache .build-deps

RUN mkdir -p /src
COPY src/ /src/
RUN pip2 install -e /src
COPY tests/ /tests/

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

WORKDIR /src
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.allocation.entrypoints.star_app:app"]
