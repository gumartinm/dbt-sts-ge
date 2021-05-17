FROM debian:stretch

LABEL maintainer="Gustavo Martin Morcuende"

ENV SPARK_VERSION        3.1.1
ENV HADOOP_VERSION       3.2.0
ENV SPARK_DIST_MIRROR    http://archive.apache.org/dist/spark
ENV SPARK_HOME           /opt/spark
ENV SPARK_CONF_DIR       /etc/spark/conf
ENV JAVA_HOME            /usr/lib/jvm/java-8-openjdk-amd64/jre

RUN mkdir -p ${SPARK_CONF_DIR} && \
    mkdir -p ${SPARK_HOME} && \
    apt-get update && \
    apt-get install -y wget unzip && \
    apt-get install -y openjdk-8-jdk python3 procps && \
    rm -rf /usb/bin/python && ln -s /usr/bin/python3 /usr/bin/python && \
    wget -qO- ${SPARK_DIST_MIRROR}/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION%.*}.tgz | tar xvz -C ${SPARK_HOME} --strip-components=1

COPY spark-defaults.conf ${SPARK_CONF_DIR} 
COPY log4j.properties ${SPARK_CONF_DIR}

EXPOSE 4040 10000

CMD ["java", "-cp", "/etc/spark/conf/:/etc/hadoop/conf/:/opt/spark/jars/*", "-Xmx4096m", "org.apache.spark.deploy.SparkSubmit", "--class", "org.apache.spark.sql.hive.thriftserver.HiveThriftServer2", "--name", "Spark Thrift Server DBT-GE", "spark-internal"]
