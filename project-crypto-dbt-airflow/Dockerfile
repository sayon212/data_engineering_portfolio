FROM python:3.10-slim

# Install Postgres server, nano, gcc
RUN apt-get update && apt-get install -y \
    postgresql \
    postgresql-contrib \
    nano \
    gcc \
    libpq-dev \
    git \
    curl \
    unzip

# Set up environment variables for Postgres
ENV POSTGRES_USER=airflow
ENV POSTGRES_PASSWORD=airflow
ENV POSTGRES_DB=crypto

# Install Python dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install dbt
RUN pip install dbt-postgres python-dotenv psycopg2-binary sqlalchemy pandas requests

# Create work folders
WORKDIR /opt/scripts

CMD ["bash"]