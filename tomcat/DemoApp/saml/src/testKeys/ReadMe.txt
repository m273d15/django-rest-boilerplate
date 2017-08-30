=================================================================
== ReadMe file for test keys                                   ==
=================================================================

In this directory, you find keys and certificates matching the 
Governikus Autent test server at https://test.governikus-eid.de.
These files are exclusively for testing, do not use any of these
keys for productive applications!The keys are matching some service
providers configured on the server https://test.governikus-eid.de.

PIN for all key stores and keys in this directory is "123456"

tls-ssl-commcert.p12
 - TLS/SSL key and certificate which was added to the certificate
   description of the CVC (Berechtigungszertificat) in use.

bos-test-tctoken.saml-encr.p12
bos-test-tctoken.saml-sign.p12
 - Encryption and signature keys and certificates used for SAML
   signature and encryption, the service provider is configured
   to use the new eID-activation with TcToken.

bos-test.saml-encr.p12
bos-test.saml-sign.p12
 - Encryption and signature keys and certificates used for SAML
   signature and encryption, the service provider is configured
   to use the old eID-activation with object tag.

demo_epa_dummy.saml-encr.p12
demo_epa_dummy.saml-sign.p12
 - Encryption and signature keys and certificates used for SAML
   signature and encryption, the service provider is configured
   to do a dummy authentication just looking like a nPA
   authentication, but without accessing the nPA.

test.governikus-eid.encr.crt
 - SAML encryption certificate of https://test.governikus-eid.de

test.governikus-eid.sign.crt
 - SAML signature certificate of https://test.governikus-eid.de

bos-test.ws-ssl.jks
 - TLS/SSL client key to do client authentication against
   https://test.governikus-eid.de:8444

test.governikus-eid.ws_ssl.crt
 - SSL/TLS server certificate used on the port with client
   authentication at https://test.governikus-eid.de:8444 and
   the certificate the server signs its webservice responses with.

=================================================================
== ReadMe file for test keys                                   ==
=================================================================
