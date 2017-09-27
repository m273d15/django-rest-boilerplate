package de.bos_bremen.gov.autent.requester.samples.saml;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import de.bos_bremen.gov.autent.common.ErrorCode;
import de.bos_bremen.gov.autent.common.ErrorCodeException;
import de.bos_bremen.gov.autent.common.HttpRedirectUtils;
import de.bos_bremen.gov.autent.common.Utils;
import de.bos_bremen.gov.autent.requester.ParsedResponse;
import de.bos_bremen.gov.autent.requester.ResponseParser;
import de.bos_bremen.gov.autent.requester.ReturnedAttributesNPA;


/**
 * This is how to receive a SAML response in HTTP Redirect binding using the new eID binding defined in BSI
 * TR-03130 version 2.0 to access the Germany identity card.<br>
 * The AutentApp or the AusweisApp first calls this Servlet with the SAML response and we parse it and store
 * the results in something like a session {@link #results}. Then this Servlet answers the HTTP get request
 * with a HTTP 302 forward. The AutentApp or AusweisApp interpret this and are shut down and will forward the
 * Browser to the url provided in the HTTP Location header attribute.<br>
 * The URL this Sevlet is deployed under must match the same origin of the subject URL in the CVC description
 * (Beschreibung des Berechtigungszertifikats).
 * <p>
 * Copyright &copy; 2011-2014 Governikus GmbH &amp; Co KG
 * </p>
 * 
 * @author hme
 */
public class NewReceiverServlet extends HttpServlet
{

  /**
   * Class to store the result of a SAML response.
   */
  static class ResultData
  {

    private String relayState;

    private ReturnedAttributesNPA attribs;

    private String errorCode;

    private String[] errorDetails;

    public String getRelayState()
    {
      return relayState;
    }

    public void setRelayState(String relayState)
    {
      this.relayState = relayState;
    }

    public ReturnedAttributesNPA getAttribs()
    {
      return attribs;
    }

    public void setAttribs(ReturnedAttributesNPA attribs)
    {
      this.attribs = attribs;
    }

    public String getErrorCode()
    {
      return errorCode;
    }

    public void setErrorCode(String errorCode)
    {
      this.errorCode = errorCode;
    }

    public String[] getErrorDetails()
    {
      return errorDetails;
    }

    public void setErrorDetails(String[] errorDetails)
    {
      this.errorDetails = errorDetails;
    }
  }

  private static final long serialVersionUID = 1L;

  /**
   * this is not for SAML request but to show the error messages somewhere
   */
  private static final Log LOG = LogFactory.getLog(NewReceiverServlet.class);

  /**
   * Stores the session Data. For a productive system you should at least implement some method of removing
   * old sessions or better use the application server own session implementation, but be aware that the SAML
   * response is provided by the AutentApp or AusweisApp in their own context, which is often different from
   * the context used by the browser and result in a different session.
   */
  private static Map<String, ResultData> results = new HashMap<String, ResultData>();


  /**
   * Called when the Get request arrives.
   * 
   * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
   */
  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,
    IOException
  {
    // if this request contains a session parameter there is already a response in our sesion store.
    String sessionID = request.getParameter("sessionID");
    if (sessionID == null)
    {
      try
      {
        // This code will be accessed by the AutentApp or the AusweisApp in their own contect.

        // get the parameter value
        String samlResponseBasee64 = request.getParameter(HttpRedirectUtils.RESPONSE_PARAMNAME);

        // if the request was accompanied by a relay state, you find it here:
        String relayState = request.getParameter(HttpRedirectUtils.RELAYSTATE_PARAMNAME);

        // check the signature of the SAML response. There is no XML signature in this response but the
        // parameter are signed.
        if (!HttpRedirectUtils.checkQueryString(request.getQueryString(), SamlExampleHelper.SERVER_SIG_CERT))
        {
          storeError(request, response, "Signaturpr&uuml;fung der SAML-Response fehlgeschlagen!");
          return;
        }

        // inflate and base64 decode the SAML response to get the xml.
        byte[] samlResponse = HttpRedirectUtils.inflate(samlResponseBasee64);

        // get a parser
        ResponseParser parser = new ResponseParser();

        // give service provider key and certificates for decryption, this is never XML singed when using SAML
        // redirect bindung.
        parser.enableDecryption(SamlExampleHelper.SERVICE_PROVIDER_NEW.encryptionKey,
                                SamlExampleHelper.SERVICE_PROVIDER_NEW.encryptionCertificate);

        // parse the SAML Response.
        ParsedResponse parsed = parser.parse(samlResponse);
        if (!parsed.isStatusSuccess())
        {
          // this is the information about the status received from the server:
          String statusCode = parsed.getStatusCode();
          String additionalStatusInfo = parsed.getStatusMessage();

          storeError(request, response, statusCode, additionalStatusInfo);
          return;
        }

        String assertionConsumerURL = SamlExampleHelper.createOwnUrlPrefix(request) + "/AutentSAMLDemo"
                                      + request.getServletPath();
        // you should check that the recipient matches your SAML assertion consumer URL
        if (!assertionConsumerURL.equals(parsed.getRecipient()))
        {
          storeError(request, response, "wrong recipent, got " + parsed.getRecipient() + " expected: "
                                        + assertionConsumerURL);
          return;
        }

        // you may use a wrapper to access the nPA attributes:
        ReturnedAttributesNPA attribs = new ReturnedAttributesNPA(parsed);
        // this class has get-methods for all supported attributes

        // generate a session ID and store the result in our session
        sessionID = Utils.getInstance().generateUniqueID();

        ResultData result = new ResultData();
        result.setRelayState(relayState);
        result.setAttribs(attribs);
        results.put(sessionID, result);

        // forward the browser to the result page. at this position a HTTP 302 is needed you are not allowed
        // to do a HTTP 200 and show the results you want to show. The URL this forward shows to will be
        // opened by the web browser.
        forwardtoURL(request, response, sessionID);
        return;
      }
      catch (ErrorCodeException e)
      {
        // that exception provides a pre-defined code together with additional information
        ErrorCode errorCode = e.getCode();
        String[] details = e.getDetails();
        // or the same information in a human-readable sentence:
        // String message = e.getMessage();

        LOG.error("got error code from SAML Server", e);
        storeError(request, response, errorCode.toString(), details);
      }
      catch (Throwable t)
      {
        LOG.error("Something went wrong", t);
        storeError(request, response, "ec.internal.error");
      }
    }
    else
    {
      // This will be accessed by the web browser after the AutehtApp or the AusweisApp finished their work.

      // fetch the session Data with the given session ID
      ResultData result = results.get(sessionID);

      // Show error page in case a error occurred
      if (result.getErrorCode() != null)
      {
        SamlExampleHelper.showErrorPage(response, result.getErrorCode(), result.getErrorDetails());
        return;
      }
      if (result.getAttribs() == null)
      {
        SamlExampleHelper.showErrorPage(response, "no attributes found");
        return;
      }

      // show results in case everything went ok.
      SamlExampleHelper.showSecuredPage(response, result.getRelayState(), result.getAttribs());
    }
  }

  /**
   * This stores an error in our Session and makes the AutentApp or AusweisApp forward the Browser to the
   * result page.
   * 
   * @param request
   * @param response
   * @param errorCode
   * @param details
   * @throws IOException
   */
  private void storeError(HttpServletRequest request,
                          HttpServletResponse response,
                          String errorCode,
                          String... details) throws IOException
  {

    String sessionID = Utils.getInstance().generateUniqueID();

    ResultData result = new ResultData();
    result.setErrorCode(errorCode);
    result.setErrorDetails(details);
    results.put(sessionID, result);

    forwardtoURL(request, response, sessionID);
  }

  /**
   * Makes the AutentApp or AusweisApp forward the browser to the result or error page.
   * 
   * @param request
   * @param response
   * @param sessionID
   * @throws IOException
   */
  private void forwardtoURL(HttpServletRequest request, HttpServletResponse response, String sessionID)
    throws IOException
  {
    response.setHeader("Cache-Control", "no-cache, no-store");
    response.setHeader("Pragma", "no-cache");
    response.sendRedirect(response.encodeRedirectURL(SamlExampleHelper.createOwnUrlPrefix(request)
                                                     + request.getRequestURI() + "?sessionID=" + sessionID));
  }
}
