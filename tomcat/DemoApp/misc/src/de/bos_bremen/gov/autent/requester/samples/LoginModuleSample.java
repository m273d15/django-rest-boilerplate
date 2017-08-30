package de.bos_bremen.gov.autent.requester.samples;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.security.Principal;

import javax.security.auth.Subject;
import javax.security.auth.callback.Callback;
import javax.security.auth.callback.CallbackHandler;
import javax.security.auth.callback.NameCallback;
import javax.security.auth.callback.PasswordCallback;
import javax.security.auth.callback.UnsupportedCallbackException;
import javax.security.auth.login.LoginContext;
import javax.security.auth.login.LoginException;

import de.bos_bremen.gov.autent.common.Utils;


/**
 * This demonstrates how to use the AutentLoginModule which implements
 * {@link javax.security.auth.spi.LoginModule} in an application with sync authentication. This could be used
 * to add authentication with user name and password to a Java application using the default Java
 * authentication system. This could be used to authenticate users in JBoss or Tomcat.
 * <p>
 * Copyright &copy; 2011-2014 Governikus GmbH &amp; Co KG
 * </p>
 */
public class LoginModuleSample
{

  /**
   * This runs the sample and loads its configuration from LoginModuleSample.cnf. Normally your application or
   * the application you are using like JBoss or Tomcat are implementing this.
   * 
   * @param args Nothing
   * @throws LoginException
   * @throws IOException
   */
  public static void main(String[] args) throws LoginException, IOException
  {
    URL conf = LoginModuleSample.class.getResource("LoginModuleSample.cnf");
    // Fix some paths in the config, just needed for this sample.
    fixPath(conf.getFile());
    // Set the config as the default Java authentication config
    System.setProperty("java.security.auth.login.config", conf.getFile());
    // Set the callback handler to provide the user name and the password
    MyCallbackhandler handler = new MyCallbackhandler();
    LoginContext loginctx = new LoginContext("Demo", handler);
    // try to login with the credentials provided by the callback handler.
    loginctx.login();
    Subject sub = loginctx.getSubject();
    // Just print the principals we got from the Autent.
    for ( Principal prin : sub.getPrincipals() )
    {
      System.out.println(prin.toString()); // NOPMD this is the main method of a sample
    }
  }

  /**
   * Replace the path to the ssl certificate with a valid one.
   * 
   * @param path
   * @throws IOException
   */
  private static void fixPath(String path) throws IOException
  {
    InputStream iStream = null;
    String configFile = null;
    try
    {
      iStream = new FileInputStream(path);
      configFile = Utils.readFromStream(iStream);
    }
    finally
    {
      if (iStream != null)
      {
        iStream.close();
      }
    }
    URL certPath = LoginModuleSample.class.getResource("/testKeys/governikus_ssl_cert.crt");
    configFile = configFile.replaceAll("sslCertName=\"([^\"]*)\"", "sslCertName=\"" + certPath.getPath()
                                                                   + "\"");
    certPath = LoginModuleSample.class.getResource("/testKeys/identityProvider-sig.crt");
    configFile = configFile.replaceAll("trustedAnchor=\"([^\"]*)\"", "trustedAnchor=\"" + certPath.getPath()
                                                                     + "\"");
    FileOutputStream fout = null;
    try
    {
      fout = new FileOutputStream(path);
      fout.write(configFile.getBytes("UTF-8"));
    }
    finally
    {
      if (fout != null)
      {
        fout.close();
      }
    }
  }

  /**
   * Callback handler providing the user name and the password to login with.
   */
  static class MyCallbackhandler implements CallbackHandler
  {

    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException
    {
      for ( Callback callback : callbacks )
      {
        if (callback instanceof NameCallback)
        {
          ((NameCallback)callback).setName("Mustermann");
        }
        else if (callback instanceof PasswordCallback)
        {
          ((PasswordCallback)callback).setPassword("geheim".toCharArray());
        }
      }
    }
  }
}
