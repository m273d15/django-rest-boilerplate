FROM tomcat:8.5

ENV GRADLE_OPTS -Dorg.gradle.daemon=false

RUN apt-get update \
 && apt-get install -y default-jdk ant gradle maven \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
 
COPY DemoApp /DemoApp
COPY procbridge /procbridge

#RUN cd /DemoApp/saml \
RUN cd /procbridge \
 && gradle clean war \
 && cp build/libs/AutentSAMLDemo.war $CATALINA_HOME/webapps/ \
 && cd / \
 && rm -rf DemoApp

COPY DemoApp/saml/tls-ssl-commcert.p12 $CATALINA_HOME/conf/tls-ssl-commcert.p12
COPY server.xml $CATALINA_HOME/conf/server.xml
CMD ["catalina.sh", "run"]