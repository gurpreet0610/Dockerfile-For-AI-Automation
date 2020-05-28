FROM centos
USER root
RUN yum install -y java-1.8.0-openjdk
RUN yum install -y wget \
&& wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo \
&& rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key \
&& yum install -y jenkins
RUN yum install -y yum-utils device-mapper-persistent-data lvm2 \
&& yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo \
&& dnf install -y docker-ce --nobest
RUN curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
&& chmod +x /usr/local/bin/docker-compose && docker-compose --version
RUN yum install -y git && yum install -y python3
RUN yum install python3-pip && pip3 install pipreqs
RUN usermod -aG docker jenkins
EXPOSE 8080
CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war"]