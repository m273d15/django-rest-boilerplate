package de.bos_bremen.gov.autent.requester.samples.saml;

import java.io.IOException;
import java.security.KeyException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.CertificateEncodingException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactoryConfigurationError;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.opensaml.xml.encryption.EncryptionException;
import org.opensaml.xml.io.MarshallingException;
import org.opensaml.xml.signature.SignatureException;
import org.opensaml.xml.util.Base64;

import de.bos_bremen.gov.autent.common.AttributeNameNPA;
import de.bos_bremen.gov.autent.common.Utils;
import de.bos_bremen.gov.autent.requester.RequestGeneratorNPA;
import de.bos_bremen.gov.autent.requester.samples.saml.SamlExampleHelper.ServiceProviderConfig;


/**
 * This is how you create and send a SAML request with HTTP POST binding as suitable if the eID-Server is
 * used. Alternatively, see ExampleRedirectRequestServlet to send the request via HTTP redirect. *
 * <p>
 * Copyright &copy; 2011-2014 Governikus GmbH &amp; Co KG
 * </p>
 * 
 * @author hme
 */
public class RequesterServlet extends HttpServlet
{

  /**
   * This field has nothing to do with SAML: see JAVA doc for meaning
   */
  private static final long serialVersionUID = 1L;

  /**
   * this is not for SAML request but to show the error messages somewhere
   */
  private static final Log LOG = LogFactory.getLog(RequesterServlet.class);

  /**
   * This method is called when a get request for this servlet arrives at the server. It creates a SAML
   * request and sends it to the server.
   * 
   * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
   */
  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,
    IOException
  {
    // Get the service provider configuration depending on the Servlet name used. This is just done to support
    // the normal and the dummy service provider in one Servlet.
    ServiceProviderConfig serviceProviderConfig = null;
    if (request.getServletPath().contains("/DummyRequesterServlet"))
    {
      serviceProviderConfig = SamlExampleHelper.SERVICE_PROVIDER_DUMMY;
    }
    else if (request.getServletPath().contains("/RequesterServlet"))
    {
      serviceProviderConfig = SamlExampleHelper.SERVICE_PROVIDER_OLD;
    }
    // get a request generator for your service provider name. Because we want to demonstrate how to get
    // attributes from an nPA, we use RequestGeneratorNPA instead of just RequestGenerator.
    RequestGeneratorNPA generator = new RequestGeneratorNPA(serviceProviderConfig.name,
                                                            SamlExampleHelper.SERVER_SAML_RECEIVER_URL);

    // enable signing the request - this is mandatory for using eID server, for other authentication methods
    // it may be optional
    generator.setSigner(true,
                        serviceProviderConfig.signatureKey,
                        serviceProviderConfig.signatureCertificate,
                        "SHA256");

    // only if the request is signed, you may specify an assertion consumer URL in the request. Otherwise, the
    // assertion consumer URL is taken from the servers configuration. This step is optional.
    generator.setAssertionConsumerURL(SamlExampleHelper.createOwnUrlPrefix(request)
                                      + "/AutentSAMLDemo"
                                      + request.getServletPath().replace("RequesterServlet",
                                                                         "ReceiverServlet"));

    // Encrypt the request
    try
    {
      generator.setEncrypter(SamlExampleHelper.SERVER_ENC_CERT);
    }
    catch (NoSuchAlgorithmException e)
    {
      LOG.error("Can not set the encryption certificate for the SAML Request", e);
      SamlExampleHelper.showErrorPage(response, "Here should be some exception handling", e.getMessage());
      return;
    }
    catch (KeyException e)
    {
      LOG.error("Can not set the encryption certificate for the SAML Request", e);
      SamlExampleHelper.showErrorPage(response, "Here should be some exception handling", e.getMessage());
      return;
    }

    // another optional step: specify which attributes you want from the server. If you skip this step, the
    // server will use its configuration to get that list of attributes, your request will not be accepted if
    // you select more attributes than allowed in your Berechtigungszertifikat.
    generator.addRequestedAttribute(AttributeNameNPA.GivenNames, false);
    generator.addRequestedAttribute(AttributeNameNPA.FamilyNames, true);
    generator.addRequestedAttribute(AttributeNameNPA.PlaceOfResidence, true);
    generator.addRequestedAttribute(AttributeNameNPA.ResidencePermitI, true);
    generator.addRequestedAttribute(AttributeNameNPA.BirthName, true);
    generator.setMinAgeVerification(21, true);

    // Add this to insert additional client parameter for application data checking by the end user. The
    // content of these parameters will be shown in the AutentApp and the user has to manually approve then.
    // This does not work with the AusweisApp.

    // generator.addAdditionalParameter("applicationTransactionInfo",
    // "Interne Autent-Demoanwendung (keine Session)", "client");
    // generator.addAdditionalParameter("applicationTransactionInfoName", "Aufrufender Process", "client");


    // Add this to use TransactionInfo parameter as per TR-03112-7
    // generator.addAdditionalParameter("TransactionInfo", "this is a test for TransactionInfo", "server");

    // now create the request and handle the exceptions
    byte[] samlRequest = null;
    try
    {
      samlRequest = generator.createSAMLRequest();
    }
    catch (TransformerFactoryConfigurationError e)
    {
      LOG.error("problem inside OpenSAML", e);
      SamlExampleHelper.showErrorPage(response, "problem inside OpenSAML", e.getMessage());
      return;
    }
    catch (TransformerException e)
    {
      LOG.error("Cannot create XML", e);
      SamlExampleHelper.showErrorPage(response, "Cannot create XML", e.getMessage());
      return;
    }
    catch (MarshallingException e)
    {
      LOG.error("Cannot create DOM structure", e);
      SamlExampleHelper.showErrorPage(response, "Cannot create DOM structure", e.getMessage());
      return;
    }
    catch (CertificateEncodingException e)
    {
      LOG.error("Problem with signature certificate", e);
      SamlExampleHelper.showErrorPage(response, "Problem with signature certificate", e.getMessage());
      return;
    }
    catch (SignatureException e)
    {
      LOG.error("Cannot sign request", e);
      SamlExampleHelper.showErrorPage(response, "Cannot sign request", e.getMessage());
      return;
    }
    catch (EncryptionException e)
    {
      LOG.error("Cannot encrypt request extension", e);
      SamlExampleHelper.showErrorPage(response, "Cannot encrypt request extension", e.getMessage());
      return;
    }

    // You may specify a free String of length at most 80 characters called RelayState. This value is not
    // interpreted by the server but returned unchanged with the SAML response. It is for your use only.
    String relayState = "State#" + System.currentTimeMillis();

    String base64EncodedRequest = Base64.encodeBytes(samlRequest);
    // Some base64 encoders will insert line breaks which is OK but leads to problems with the
    // AusweisApp. The AusweisApp will check a hash value of the request but it does hash neither the SAML
    // request nor the given parameter value but rather some value derived from it. Avoid these problems by
    // making sure there are no ignorable characters of any kind in this value:
    base64EncodedRequest = base64EncodedRequest.replace("\n", "").replace(" ", "");

    // now the request must be sent as HTTP post from the browser to the ID Manager. We enter the
    // request into a HTML form and return the page to the browser:
    String html = Utils.readFromStream(RequesterServlet.class.getResourceAsStream("forward.html"))
                       .replace("${ACTION}", SamlExampleHelper.SERVER_SAML_RECEIVER_URL)
                       .replace("${SAML}", base64EncodedRequest)
                       .replace("${RELAY_STATE}", relayState);
    response.getWriter().write(html);

    // make sure the browser does not cache this page:
    response.setHeader("Cache-Control", "no-cache, no-store");
    response.setHeader("Pragma", "no-cache");

    // The further proceedings of POST binding are described in the SAML bindings specification.
    // Finally, the ID Manager will (cause the browser to) send the SAML response via POST to the assertion
    // consumer URL specified in the request or in the configuration.
  }
}
