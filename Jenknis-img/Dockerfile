FROM debian:bullseye-slim

USER root

RUN apt-get update && apt-get install -y \
    gnupg2 \
    wget \
    ca-certificates \
    lsb-release \
    openjdk-11-jdk \
    git \
    sudo
    
RUN wget --no-check-certificate -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    
RUN echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" > /etc/apt/sources.list.d/jenkins.list
    
RUN apt-get update && apt-get install -y jenkins
    
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

EXPOSE 8080 50000

USER jenkins

CMD ["jenkins"]
