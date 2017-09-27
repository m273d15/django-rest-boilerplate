<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<%@page import="de.bos_bremen.gov.autent.requester.samples.saml.SamlExampleHelper"%>
	<%@page import="java.net.URLEncoder"%>
		<%@page import="java.io.UnsupportedEncodingException"%>
			<%!String getProviderURL(HttpServletRequest request, String servletName) throws UnsupportedEncodingException
  {
    String link = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort()
                  + "/AutentSAMLDemo/" + servletName;
    return URLEncoder.encode(link, request.getCharacterEncoding() != null ? request.getCharacterEncoding()
      : "UTF-8");
  }%>
				<%!String getErrorURL(HttpServletRequest request) throws UnsupportedEncodingException
  {
    String link = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort()
                  + "/AutentSAMLDemo/error.html";
    return URLEncoder.encode(link, request.getCharacterEncoding() != null ? request.getCharacterEncoding()
      : "UTF-8");
  }%>
 

					<html lang="de">

					<head>

						<meta charset="utf-8">
						<meta http-equiv="X-UA-Compatible" content="IE=edge">
						<meta name="viewport" content="width=device-width, initial-scale=1">
						<meta name="description" content="">
						<meta name="author" content="">

						<title>Diensteanbieter werden in 15 Minuten</title>

						<!-- Bootstrap Core CSS -->
						<link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

						<!-- Custom Fonts -->
						<link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
						<link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
						<link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'>
						<link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
						<link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'>

						<!-- Theme CSS -->
						<link href="css/agency.css" rel="stylesheet">

					</head>

					<body id="page-top" class="index">

						<!-- Navigation -->
						<nav id="mainNav" class="navbar navbar-default navbar-custom navbar-fixed-top">
							<div class="container">
								<!-- Brand and toggle get grouped for better mobile display -->
								<div class="navbar-header page-scroll">
									<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span> Menu <i class="fa fa-bars"></i>
                </button>
									<a class="navbar-brand page-scroll" href="#page-top">Nach oben</a>
								</div>

								<!-- Collect the nav links, forms, and other content for toggling -->
								<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
									<ul class="nav navbar-nav navbar-right">
										<li class="hidden">
											<a href="#page-top"></a>
										</li>
										<li>
											<a class="page-scroll" href="#SAMLDemo">SAML Demo Anwendung</a>
										</li>

										<li>
											<a class="page-scroll" href="#about">Information</a>
										</li>
										<li>
											<a class="page-scroll" href="#contact">Kontakt</a>
										</li>
									</ul>
								</div>
								<!-- /.navbar-collapse -->
							</div>
							<!-- /.container-fluid -->
						</nav>

						<!-- Header -->
						<header>
							<div class="container">
								<div class="intro-text">
									<div class="intro-lead-in">Diensteanbieter werden in 15 Minuten</div>
									<div class="intro-heading">Viel Spa&szlig;!</div>
									<a href="#SAMLDemo" class="page-scroll btn btn-xl">Los geht's</a>
								</div>
							</div>
						</header>

						<!-- SAML Demo -->
						<section id="SAMLDemo">
							<div class="container">
								<div class="row">
									<div class="col-lg-12 text-center">
										<h2 class="section-heading">
											Starten Sie die Demo-Anwendung

										</h2>
										<h3 class="section-subheading text-muted">
											<p>
												Dieses Beispiel soll einen kurzen Eindruck vermitteln, wie einfach die technischen Aspekte f&uuml;r die Nutzung des Online-Ausweises
												umzustzen sind. Nutzen Sie die AusweisApp2 mit der
												<a href="https://persosim.de/">PersoSim</a> oder einem Testausweis.</p>
											<p>
												<a href="http://127.0.0.1:24727/eID-Client?tcTokenURL=<%=getProviderURL(request, "NewRequesterServlet")%>" class="page-scroll btn btn-xl">
                        Authentisierung starten</a> </p>
										</h3>
									</div>
								</div>
							</div>

						</section>


						<!-- About Section -->
						<section id="about">
							<div class="container">
								<div class="row">
									<div class="col-lg-12 text-center">
										<h2 class="section-heading">Information</h2>
										<h3 class="section-subheading text-muted">
											<p>Diese Demo basiert auf dem Autent SDK und einem freien Theme f&uuml;r Bootstrap (<a href="https://startbootstrap.com/template-overviews/agency/">link</a>).</p>
											<p>Hier folgen die ben&ouml;nigten Schritte:</p>
										</h3>
									</div>
								</div>
								<div class="row">
									<div class="col-lg-12">
										<ul class="timeline">
											<li>
												<div class="timeline-image">
													<img class="img-rounded img-responsive" src="img/about/1.png" alt="">
												</div>
												<div class="timeline-panel">
													<div class="timeline-heading">
														<h4>Laden Sie die DemoAnwendung herunter</h4>
														<h4 class="subheading"></h4>
													</div>
													<div class="timeline-body">
														<p class="text-muted">Der inkludierte Tomcat ist vorbereitet und kann sofort gestartet werden</p>
													</div>
												</div>
											</li>
											<li class="timeline-inverted">
												<div class="timeline-image">
													<img class="img-rounded img-responsive" src="img/about/2.png" alt="">
												</div>
												<div class="timeline-panel">
													<div class="timeline-heading">
														<h4>Passen Sie die Anwendung an Ihre Bed&uuml;rfnisse an.</h4>
														<h4 class="subheading"></h4>
													</div>
													<div class="timeline-body">
														<p class="text-muted">
															Bauen Sie die Anwendung mit dem folgenden Kommando neu <code>ant dist</code> und kopieren Sie das die neu
															entstandene AutentSAMLDemo.war in das Tomcat-Webapp Verzeichnis.
														</p>
													</div>
												</div>
											</li>

											<li class="timeline-inverted">
												<div class="timeline-image">
													<h4>Online-Ausweis
														<br>in
														<br>15 Minuten</h4>
												</div>
											</li>
											<li class="timeline-inverted">
												<div class="timeline-image">
													<img class="img-rounded img-responsive" src="img/about/3.png" alt="">
												</div>

											</li>

										</ul>
									</div>
								</div>
							</div>
						</section>


						<!-- Contact Section -->
						<section id="contact">
							<div class="container">
								<div class="row">
									<div class="col-lg-12 text-center">
										<h2 class="section-heading">Kontakt</h2>
										<h3 class="section-subheading text-muted"><a href="mailto:AusweisApp2@governikus.de">Schreiben Sie uns eine EMail</h3>
                </div>
            </div>
          
    </section>

    <footer>
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <span class="copyright">Copyright &copy; Governikus KG 2016</span>
                </div>
                
               
            </div>
        </div>
    </footer>

    
    <!-- jQuery -->
    <script src="vendor/jquery/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>

    <!-- Contact Form JavaScript -->
    <script src="js/jqBootstrapValidation.js"></script>
    <script src="js/contact_me.js"></script>

    <!-- Theme JavaScript -->
    <script src="js/agency.min.js"></script>

</body>

</html>