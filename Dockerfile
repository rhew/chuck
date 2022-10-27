FROM python:3
WORKDIR /usr/src/app
COPY setup.py .
COPY chuck.py .
COPY README.md .
RUN pip install --no-cache-dir .
CMD [ "chuck" ]
