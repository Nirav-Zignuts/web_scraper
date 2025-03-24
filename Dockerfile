FROM python:3.10

WORKDIR /app
COPY requirment.txt .
RUN pip install --no-cache-dir -r requirment.txt


COPY . .


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
