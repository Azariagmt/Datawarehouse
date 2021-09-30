FROM puckel/docker-airflow

WORKDIR /usr/local/airflow/
COPY requirements.txt .
RUN echo "break arg"
RUN pip install apache-airflow-backport-providers-mysql
RUN pip install apache-airflow-backport-providers-mysql
RUN pip install --user -r requirements.txt

