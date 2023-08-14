FROM python:3.9.13
ADD . /
COPY . /app/
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]