package de.bos_bremen.gov.autent.requester.samples.saml;

import java.io.IOException;
import java.security.GeneralSecurityException;
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

import de.bos_bremen.gov.autent.common.AttributeNameNPA;
import de.bos_bremen.gov.autent.common.HttpRedirectUtils;
import de.bos_bremen.gov.autent.requester.RequestGeneratorNPA;


/**
 * This is how to send a SAML Request in HTTP Redirect binding using the new eID binding defined in BSI
 * TR-03130 version 2.0 to the Governikus Autent.<br>
 * This servlet is called by the AutentApp or the AusweisApp which gets the URL to this Servlet in the
 * TcTokenUrl parameter. This Servlet generates a SAML Request and forward it to the Governikus Autent in a
 * HTTP redirect. <br>
 * The URL this Sevlet is deployed under must match the same origin of the subject URL in the CVC description
 * (Beschreibung des Berechtigungszertifikats).
 * <p>
 * Copyright &copy; 2011-2014 Governikus GmbH &amp; Co KG
 * </p>
 * 
 * @author hme
 */
public class NewRequesterServlet extends HttpServlet
{

  /**
   * This field has nothing to do with SAML: see JAVA doc for meaning
   */
  private static final long serialVersionUID = 1L;

  /**
   * this is not for SAML request but to show the error messages somewhere
   */
  private static final Log LOG = LogFactory.getLog(NewRequesterServlet.class);

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
    // get a request generator for your service provider name. Because we want to demonstrate how to get
    // attributes from an nPA, we use RequestGeneratorNPA instead of just RequestGenerator.
    RequestGeneratorNPA generator = new RequestGeneratorNPA(SamlExampleHelper.SERVICE_PROVIDER_NEW.name,
                                                            SamlExampleHelper.SERVER_SAML_RECEIVER_URL);


    // only if the request is signed, you may specify an assertion consumer URL in the request. Otherwise, the
    // assertion consumer URL is taken from the servers configuration. This step is optional.
    generator.setAssertionConsumerURL(SamlExampleHelper.createOwnUrlPrefix(request)
                                      + "/AutentSAMLDemo/NewReceiverServlet");


    // Encrypt the request. Do not add a XML signature to this SAML request just sign the http parameters.
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
    generator.addRequestedAttribute(AttributeNameNPA.BirthName, true);
    generator.addRequestedAttribute(AttributeNameNPA.PlaceOfResidence, true);
    generator.addRequestedAttribute(AttributeNameNPA.ResidencePermitI, true);
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
    // interpreted by the server but returned unchanged with the SAML response. It is for your use only. This
    // step is optional.
    String relayState = "State#" + System.currentTimeMillis();

    try
    {
      // Create the URL used for the HTTP redirect binding. This URL sends the SAML Request to the Governikus
      // Autent and contains a signature with the Service providers private key over this Request and an
      // additional parameter. The SAML request is base64 encoded any inflated.
      String query = HttpRedirectUtils.createQueryString(SamlExampleHelper.SERVER_SAML_RECEIVER_URL,
                                                         samlRequest,
                                                         true,
                                                         relayState,
                                                         SamlExampleHelper.SERVICE_PROVIDER_NEW.signatureKey,
                                                         "SHA256");
      // Set the URL and forward the AutentApp or AusweisApp to the Governikus Autent SAML receiver.
      response.setHeader("Cache-Control", "no-cache, no-store");
      response.setHeader("Pragma", "no-cache");
      response.sendRedirect(response.encodeRedirectURL(query));
    }
    catch (GeneralSecurityException e)
    {
      LOG.error("Can not create query URL", e);
      SamlExampleHelper.showErrorPage(response, "Can not create query URL", e.getMessage());
    }
  }

}
