FROM python:3.10
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all local files to /app
COPY . .

# Ensure proper permissions
RUN chmod +x manage.py
RUN chmod -R 755 .

EXPOSE 9009

# Collect static files, apply migrations, and run the server
CMD ["bash", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:9009"]