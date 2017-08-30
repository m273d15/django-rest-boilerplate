package de.bos_bremen.gov.autent.requester.samples.saml;

import java.io.IOException;
import java.security.GeneralSecurityException;
import java.security.PrivateKey;
import java.security.cert.X509Certificate;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.opensaml.xml.ConfigurationException;

import de.bos_bremen.gov.autent.common.Utils;
import de.bos_bremen.gov.autent.common.Utils.X509KeyPair;
import de.bos_bremen.gov.autent.requester.ReturnedAttributesNPA;
import de.bos_bremen.gov.autent.requester.ReturnedAttributesNPA.AgeVerificationResult;
import de.bos_bremen.gov.autent.requester.ReturnedAttributesNPA.Place;


/**
 * A helper and configuration store for the Autent SAML Service provider example. This stores the certificates
 * and URLs needed to communicate with the Autent and also provides some generic functions used in this
 * example.<br>
 * Currently this load some test keys and certificates for which the private keys are publicly known and not
 * private or secure any more, <b> replace all the private keys used here with your own when using this on a
 * productive system.</b>
 * <p>
 * Copyright &copy; 2011-2014 Governikus GmbH &amp; Co KG
 * </p>
 * 
 * @author hme
 */
public class SamlExampleHelper
{

  /**
   * this is not for SAML request but to show the error messages somewhere
   */
  private static final Log LOG = LogFactory.getLog(ReceiverServlet.class);

  /**
   * URL where the Governikus Autent SAML receiver is deployed - ask your server administrator for this url.
   */
  public static final String SERVER_SAML_RECEIVER_URL = "https://test.governikus-eid.de/gov_autent/async";

  /**
   * Signature certificate of Autent server.<br>
   * Obtain that value from Governikus Autent's administrator.<br>
   * This could also be fetched from the meta data which is available at URL
   * http://host:port/gov_autent/async?metadata=true
   */
  public static final X509Certificate SERVER_SIG_CERT;

  /**
   * Encryption certificate of Autent server.<br>
   * Obtain that value from Governikus Autent's administrator.<br>
   * This could also be fetched from the meta data which is available at URL
   * http://host:port/gov_autent/async?metadata=true
   */
  public static final X509Certificate SERVER_ENC_CERT;

  /**
   * URL where the Autent App is deployed, needed when using the AutentApp and not the AusweisApp.
   */
  public static final String SERVER_AUTENT_APPLET_URL = "https://appl.bos-asp.de/test/AutentApp/applet.html";

  /**
   * Configuration store for the service provider configuration. This example shows some ways to access the
   * Gvernikus Autent to read attributes from the German identity card, in a real application you would just
   * need one service provider configuration because you do not want to implement all possible ways the
   * Governikus Autent could be accessed.
   */
  static class ServiceProviderConfig
  {

    /**
     * EntityID of your service provider. The Autent server identifies you by this name. Normally this is the
     * URL of your service like "http://myservice.example.com/secureRegistration". You have to give this to
     * the Autent server administrator.
     */
    public final String name;

    /**
     * Your own signature certificate belonging to the {@link #signatureKey}.<br>
     * The SAML Requests are signed with the key belonging to this certificate. <br>
     * Give this certificate to the Autent Server administrator so the server can verify your requests. This
     * should be a signature certificate, but does not have to be issues by any special certificate authority,
     * it could be, a self signed certificate also fits the needs.<br>
     * You could just generate this certificate and a key with openssl or java keytool on your locale machine.
     */
    public X509Certificate signatureCertificate;

    /**
     * Private key matching your signature certificate <br>
     * You should not give this key to anyone including the Autent Server administrator.
     */
    public PrivateKey signatureKey;

    /**
     * Your own encryption certificate belonging to the {@link #encryptionKey}.<br>
     * The Autent Server can encrypt the SAML Responses with this certificate and they could only be decrypted
     * with the key belonging to this certificate. <br>
     * Give this certificate to the Autent Server administrator so the server can encrypt the SAML responses
     * for you personally. This should be a encryption certificate, but does not have to be issues by any
     * special certificate authority, it could be, a self signed certificate also fits the needs.<br>
     * You could just generate this certificate and a key with openssl or java keytool on your locale machine.
     */
    public X509Certificate encryptionCertificate;

    /**
     * Private key matching your encryption certificate <br>
     * You should not give this key to anyone including the Autent Server administrator.
     */
    public PrivateKey encryptionKey;


    public ServiceProviderConfig(String name)
    {
      this.name = name;
    }
  }

  /**
   * This is our default test service provider used for the old eID activation with the AutentApp and the
   * AusweisApp. This is configured to read out data from the Germany test identity card
   * (Testpersonalausweis).
   */
  public static final ServiceProviderConfig SERVICE_PROVIDER_OLD;

  /**
   * This is our default test service provider used for the new eID activation with the AutentApp and the
   * AusweisApp. This is configured to read out data from the Germany test identity card
   * (Testpersonalausweis).
   */
  public static final ServiceProviderConfig SERVICE_PROVIDER_NEW;

  /**
   * This is our default test service provider used for the old eID activation for dummy tests without using
   * any Germany test identity card (Personalausweis). This could be used to test your application against the
   * server while you do not have access to Germany test identity cards. This is just possible with the
   * AutentApp and not with the AusweisApp.
   */
  public static final ServiceProviderConfig SERVICE_PROVIDER_DUMMY;


  static
  {
    try
    {
      Utils.getInstance().initDefault();
    }
    catch (ConfigurationException e)
    {
      LOG.error("Problem while initialization of OpenSAML.", e);
    }
    X509Certificate serverSigCert = null;
    X509Certificate serverEncCert = null;
    try
    {
      serverSigCert = (X509Certificate)Utils.readCert(SamlExampleHelper.class.getResourceAsStream("/testKeys/test.governikus-eid.sign.crt"),
                                                      "x509");
      serverEncCert = (X509Certificate)Utils.readCert(SamlExampleHelper.class.getResourceAsStream("/testKeys/test.governikus-eid.encr.crt"),
                                                      "x509");
    }
    catch (GeneralSecurityException e)
    {
      LOG.error("Can not load the encryption key and certificate or signatrue certificate", e);
    }
    SERVER_SIG_CERT = serverSigCert;
    SERVER_ENC_CERT = serverEncCert;
    SERVICE_PROVIDER_OLD = createServiceProviderConfig("https://localhost:8443",
                                                       "bos-test.saml-sign",
                                                       "/testKeys/bos-test.saml-sign.p12",
                                                       "bos-test.saml-encr",
                                                       "/testKeys/bos-test.saml-encr.p12");
    SERVICE_PROVIDER_NEW = createServiceProviderConfig("https://localhost:8443/tcToken",
                                                       "bos-test-tctoken.saml-sign",
                                                       "/testKeys/bos-test-tctoken.saml-sign.p12",
                                                       "bos-test-tctoken.saml-encr",
                                                       "/testKeys/bos-test-tctoken.saml-encr.p12");
    SERVICE_PROVIDER_DUMMY = createServiceProviderConfig("demo_epa_dummy_applet",
                                                         "demo_epa_dummy_applet.saml-sign",
                                                         "/testKeys/demo_epa_dummy_applet.saml-sign.p12",
                                                         "demo_epa_dummy_applet.saml-encr",
                                                         "/testKeys/demo_epa_dummy_applet.saml-encr.p12");
  }

  /**
   * Create a configuration for this application for the given service provider.
   * 
   * @param name name of the service provider
   * @return a configuration
   * @throws IOException
   * @throws GeneralSecurityException
   */
  private static ServiceProviderConfig createServiceProviderConfig(String name,
                                                                   String sigAias,
                                                                   String sigFilename,
                                                                   String encAias,
                                                                   String encFilename)
  {
    ServiceProviderConfig provider = new ServiceProviderConfig(name);
    try
    {
      X509KeyPair pair = Utils.readKeyAndCert(SamlExampleHelper.class.getResourceAsStream(sigFilename),
                                              "PKCS12",
                                              "123456".toCharArray(),
                                              sigAias);
      provider.signatureKey = pair.getKey();
      provider.signatureCertificate = pair.getCert();
    }
    catch (IOException e)
    {
      LOG.error("Can not load the encryption key and certificate or signatrue certificate", e);
    }
    catch (GeneralSecurityException e)
    {
      LOG.error("Can not load the encryption key and certificate or signatrue certificate", e);
    }
    try
    {
      X509KeyPair pair = Utils.readKeyAndCert(SamlExampleHelper.class.getResourceAsStream(encFilename),
                                              "PKCS12",
                                              "123456".toCharArray(),
                                              encAias);
      provider.encryptionKey = pair.getKey();
      provider.encryptionCertificate = pair.getCert();
    }
    catch (IOException e)
    {
      LOG.error("Can not load the encryption key and certificate or signatrue certificate", e);
    }
    catch (GeneralSecurityException e)
    {
      LOG.error("Can not load the encryption key and certificate or signatrue certificate", e);
    }
    return provider;
  }

  /**
   * Fill the response such that the browser displays an appropriate error page
   * 
   * @param response
   * @param errorCode main code or status
   * @param details further information about the error
   * @throws IOException
   */
  public static void showErrorPage(HttpServletResponse response, String errorCode, String... details)
    throws IOException
  {
    StringBuilder builder = new StringBuilder();
    builder.append("<h3>");
    builder.append(errorCode);
    builder.append("</h3>");
    for ( String detail : details )
    {
      builder.append("<p>");
      builder.append(detail);
      builder.append("</p>");
    }
    String html = Utils.readFromStream(SamlExampleHelper.class.getResourceAsStream("error.html"))
                       .replace("${MESSAGE}", builder.toString());
    // status code 400 is needed for new eID activation as defined in TR-03130 version 2.0 and above.
    response.setStatus(400);
    response.getWriter().write(html);
  }

  /**
   * Returns a nicely formated string from the SAML response.
   * 
   * @param value
   * @param isNotOnChip true if this attribute is not on the nPA chip
   */
  private static String getStringInfo(String value, boolean isNotOnChip)
  {
    if (isNotOnChip)
    {
      return "auf dem Chip nicht vorhanden";
    }
    else if (value != null)
    {
      return value;
    }
    else
    {
      return "Auslesen nicht erlaubt";
    }
  }

  /**
   * Returns a nicely formated age verification result.
   * 
   * @param ageVerificationResult
   * @param isNotOnChip true if this attribute is not on the nPA chip
   */
  private static String getAgeVerification(AgeVerificationResult ageVerificationResult, boolean onNotChip)
  {
    if (onNotChip)
    {
      return "auf dem Chip nicht vorhanden";
    }
    else if (ageVerificationResult != null)
    {
      return ageVerificationResult.isResult() ? "Erf\u00fcllt (" + ageVerificationResult.getRequiredAge()
                                                + ")" : "nicht Erf\u00fcllt ("
                                                        + ageVerificationResult.getRequiredAge() + ")";
    }
    else
    {
      return "Auslesen nicht erlaubt";
    }
  }

  private static String replaceNull(String input)
  {
    return input == null ? "Auslesen nicht erlaubt" : input;
  }

  /**
   * Convert the Place to a String. There are three different types a place could be represented in the German
   * identity card. It could be a structured place, a free text place or no place info. The information you
   * get depends on the data stored in the identity card and your implementation should handle all.
   * 
   * @param place place to convert
   * @param this is set to true when this attribute is on the chip, some nPA from the first generations do not
   *        have all attributes
   * @return Place info as a String
   */
  private static String getPlaceInfo(Place place, boolean onNotChip)
  {
    if (onNotChip)
    {
      return "auf dem Chip nicht vorhanden";
    }
    else if (place != null)
    {
      switch (place.getType())
      {
        case STRUCTURED:
          StringBuilder builder = new StringBuilder();
          builder.append("Staat: ");
          builder.append(replaceNull(place.getCountry()));
          builder.append(", Land: ");
          builder.append(replaceNull(place.getState()));
          builder.append(", Stadt: ");
          builder.append(replaceNull(place.getZipCode()));
          builder.append(' ');
          builder.append(replaceNull(place.getCity()));
          builder.append(", Stra\u00dfe: ");
          builder.append(replaceNull(place.getStreet()));
          return builder.toString();
        case FREE_TEXT:
          return replaceNull(place.getFreeText());
        case NO_PLACE_INFO:
          return replaceNull(place.getNoPlaceInfo());
      }
      return "Fehler";
    }
    else
    {
      return "Auslesen nicht erlaubt";
    }
  }

  /**
   * Fill the response such that the browser eventually displays the secured page.
   * 
   * @param response
   * @param relayState
   * @param attribs
   * @throws IOException
   */
  public static void showSecuredPage(HttpServletResponse response,
                                     String relayState,
                                     ReturnedAttributesNPA attribs) throws IOException
  {
    String familyName = getStringInfo(attribs.getFamilyNames(), attribs.isFamilyNamesNotOnChip());
    String givenName = getStringInfo(attribs.getGivenNames(), attribs.isGivenNamesNotOnChip());
    String birthName = getStringInfo(attribs.getBirthName(), attribs.isBirthNameNotOnChip());
    String residencePermit = getStringInfo(attribs.getResidencePermitI(),
                                           attribs.isResidencePermitINotOnChip());
    String placeOfResidence = getPlaceInfo(attribs.getPlaceOfResidence(),
                                           attribs.isPlaceOfResidenceNotOnChip());

    // Get the age verification result and the requested age which was checked from the SAML response.
    String ageVerification = getAgeVerification(attribs.getAgeVerificationResult(),
                                                attribs.isAgeVerificationResultNotOnChip());

    String result = Utils.readFromStream(SamlExampleHelper.class.getResourceAsStream("result.html"))
                         .replace("#{GIVEN_NAME}", Utils.prepareHTMLOutput(givenName))
                         .replace("#{FAMILY_NAME}", Utils.prepareHTMLOutput(familyName))
                         .replace("#{BIRTH_NAME}", Utils.prepareHTMLOutput(birthName))
                         .replace("#{PLACE_OF_RESIDENCE}", Utils.prepareHTMLOutput(placeOfResidence))
                         .replace("#{RESIDENCE_PERMIT}", Utils.prepareHTMLOutput(residencePermit))
                         .replace("#{AGE_VERIFICATION}", Utils.prepareHTMLOutput(ageVerification))
                         .replace("#{RELAY_STATE}", Utils.prepareHTMLOutput(relayState));
    response.getWriter().println(result);
  }

  /**
   * Return URL prefix from http request.
   */
  public static String createOwnUrlPrefix(HttpServletRequest req)
  {
    return req.getScheme() + "://" + req.getServerName() + ":" + req.getServerPort();
  }
}
