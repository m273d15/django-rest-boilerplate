package de.bos_bremen.gov.autent.requester.samples.saml;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.xml.security.utils.Base64;

import de.bos_bremen.gov.autent.common.ErrorCode;
import de.bos_bremen.gov.autent.common.ErrorCodeException;
import de.bos_bremen.gov.autent.common.HttpRedirectUtils;
import de.bos_bremen.gov.autent.requester.ParsedResponse;
import de.bos_bremen.gov.autent.requester.ResponseParser;
import de.bos_bremen.gov.autent.requester.ReturnedAttributesNPA;
import de.bos_bremen.gov.autent.requester.samples.saml.SamlExampleHelper.ServiceProviderConfig;


/**
 * This is how to receive a SAML response in HTTP POST binding. This is only how to receive the response, not
 * the implementation of the service provider! To make it work, you will need to implement some service
 * provider and create responses which take the user to the correct pages. *
 * <p>
 * Copyright &copy; 2011-2014 Governikus GmbH &amp; Co KG
 * </p>
 * 
 * @author hme
 */
public class ReceiverServlet extends HttpServlet
{

  private static final long serialVersionUID = 1L;

  /**
   * this is not for SAML request but to show the error messages somewhere
   */
  private static final Log LOG = LogFactory.getLog(ReceiverServlet.class);

  /**
   * Called when the POST request arrives.
   * 
   * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
   */
  @Override
  protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException,
    IOException
  {
    // Get the service provider configuration depending on the Servlet name used. This is just done to support
    // the normal and the dummy service provider in one Servlet.
    ServiceProviderConfig serviceProviderConfig = null;
    if (request.getServletPath().contains("/DummyReceiverServlet"))
    {
      serviceProviderConfig = SamlExampleHelper.SERVICE_PROVIDER_DUMMY;
    }
    else if (request.getServletPath().contains("/ReceiverServlet"))
    {
      serviceProviderConfig = SamlExampleHelper.SERVICE_PROVIDER_OLD;
    }

    try
    {
      // if the request was accompanied by a relay state, you find it here:
      String relayState = request.getParameter(HttpRedirectUtils.RELAYSTATE_PARAMNAME);

      // get the parameter value
      byte[] samlResponse = Base64.decode(request.getParameter(HttpRedirectUtils.RESPONSE_PARAMNAME));

      // get a parser
      ResponseParser parser = new ResponseParser();

      // give key and certificates for decryption and signature check
      parser.enableDecryption(serviceProviderConfig.encryptionKey,
                              serviceProviderConfig.encryptionCertificate);
      parser.enableSignatureCheck(SamlExampleHelper.SERVER_SIG_CERT);

      ParsedResponse parsed = parser.parse(samlResponse);
      if (!parsed.isStatusSuccess())
      {
        // this is the information about the status received from the server:
        String statusCode = parsed.getStatusCode();
        String additionalStatusInfo = parsed.getStatusMessage();

        SamlExampleHelper.showErrorPage(response, statusCode, additionalStatusInfo);
        return;
      }

      String assertionConsumerURL = SamlExampleHelper.createOwnUrlPrefix(request) + "/AutentSAMLDemo"
                                    + request.getServletPath();
      // you should check that the recipient matches your SAML assertion consumer URL
      if (!assertionConsumerURL.equals(parsed.getRecipient()))
      {
        SamlExampleHelper.showErrorPage(response, "wrong recipent, got " + parsed.getRecipient()
                                                  + " expected: " + assertionConsumerURL);
        return;
      }

      // you may use a wrapper to access the nPA attributes:
      ReturnedAttributesNPA attribs = new ReturnedAttributesNPA(parsed);
      // this class has get-methods for all supported attributes

      // access OK!
      SamlExampleHelper.showSecuredPage(response, relayState, attribs);
    }
    catch (ErrorCodeException e)
    {
      // that exception provides a pre-defined code together with additional information
      ErrorCode errorCode = e.getCode();
      String[] details = e.getDetails();
      // or the same information in a human-readable sentence:
      // String message = e.getMessage();

      LOG.error("got error code from SAML Server", e);
      SamlExampleHelper.showErrorPage(response, errorCode.toString(), details);
    }
    catch (Throwable t)
    {
      LOG.error("Something went wrong", t);
      SamlExampleHelper.showErrorPage(response, "ec.internal.error");
    }
  }

  /**
   * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
   */
  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,
    IOException
  {
    LOG.error("Get requests are not supported.");
    response.setStatus(403);
  }
}
