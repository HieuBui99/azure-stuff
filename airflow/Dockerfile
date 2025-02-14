FROM apache/airflow:2.10.5

USER root

# Install additional system dependencies if needed
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



RUN mkdir -p /home/airflow/.kaggle
COPY kaggle.json /home/airflow/.kaggle/kaggle.json
RUN chown -R airflow: /home/airflow/.kaggle

USER airflow

# Install additional Python packages if needed
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Copy your DAGs into the container
# COPY ./dags /opt/airflow/dags/