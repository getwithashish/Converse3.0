dockerize -wait tcp://postgresql-db-service:5432 -timeout 1m

gunicorn -w 4 -b 0.0.0.0:8000 main:app
