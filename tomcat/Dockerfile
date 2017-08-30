FROM tomcat:8.5

RUN apt-get update \
 && apt-get install -y default-jdk ant \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
 
COPY DemoApp /DemoApp

RUN cd /DemoApp/saml \
 && ant \
 && cp dist/AutentSAMLDemo.war $CATALINA_HOME/webapps/ \
 && cd / \
 && rm -rf DemoApp

COPY DemoApp/saml/tls-ssl-commcert.p12 $CATALINA_HOME/conf/tls-ssl-commcert.p12
COPY server.xml $CATALINA_HOME/conf/server.xml
CMD ["catalina.sh", "run"]