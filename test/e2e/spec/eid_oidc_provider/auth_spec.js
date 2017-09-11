describe("eId OpenId - Authorization:", function () {

    var chakram = require('chakram');
    var rsa = require('jsrsasign');
    var expect = chakram.expect;
    var env = process.env;
    var URL = 'https://' + env.BOILERPLATE_DOMAIN + '/api';

    var createParams = function (params = {}) {
        usedParams = {
            'response_type' : env.OIDC_RESPONSE_TYPE,
            'scope' : env.OIDC_SCOPE,
            'client_id' : env.OIDC_CLIENT_ID,
            'state' : env.OIDC_STATE,
            'nonce' : env.OIDC_NONCE,
            'redirect_uri' : env.OIDC_REDIRECT_URI
        };
        for (var pName in params) { if (pName in usedParams) usedParams[pName] = params[pName]; }

        return encodeURI(Object.keys(usedParams).map(function(key){
            return key + '=' + usedParams[key];
        }).join('&'));
    };

    var parseUuid = function (uuid) {
        return uuid.slice(0, 8).concat(
            "-", uuid.slice(8, 12), "-", uuid.slice(12, 16), "-", uuid.slice(16, 20), "-", uuid.slice(20)
        );
    };

    var makeRequest = function(relativeUrl, parameters, method = 'get') {
        url = URL + relativeUrl;
        if (parameters)
            url += '?' + parameters;
        return chakram[method](url);
    };

    var makeOpenidInitRequest = function (params = createParams()) {
        return makeRequest('/openid/authorize', params);
    };

    var makeAfterAuthenticationEidServiceRequest = function (paramsString, method) {
        return makeRequest('/eIdService/refresh', paramsString, method);
    };

    var makeAfterAuthenticationValidEidServiceRequest = function (method) {
        return makeAfterAuthenticationEidServiceRequest('refreshId=' + env.OIDC_REFRESH_ID, method);
    };

    var makeAfterAuthenticationMalformedEidServiceRequest = function () {
        return makeAfterAuthenticationEidServiceRequest('refreshId=xxx');
    };

    var makeAfterAuthenticationIncompleteEidServiceRequest = function () {
        return makeAfterAuthenticationEidServiceRequest('');
    };

    var makeAfterAuthenticationValidEidServiceRequestWithUnknownId = function () {
        return makeAfterAuthenticationEidServiceRequest('refreshId=12345678123456781234567812345678');
    };

    var makeAfterAuthenticationValidEndpointRequest = function (method) {
        parameters = 'eid_access_token=' + parseUuid(env.OIDC_ACCESS_TOKEN) + '&' + env.OIDC_OPENID_PARAMETER;
        return makeRequest('/eidopenid/login/', parameters, method);
    };

    var makeAfterAuthenticationEndpointRequestWithoutToken = function () {
        return makeRequest('/eidopenid/login/', env.OIDC_OPENID_PARAMETER);
    };

    var makeFinalAuthenticationRequest = function (endpointRespObj) {
        return makeRequest('/../' + endpointRespObj.response.headers.location);
    };

    var expectRequestToHave = function(chakramResponsePromise, statusCode, locationPattern) {
        return chakramResponsePromise.then(function (respObj) {
            expect(respObj).to.have.status(statusCode);
            if (locationPattern) {
                expect(respObj).to.have.header('Location', locationPattern);
            }
            return chakram.wait();
        });
    };

    before(function () {
        chakram.setRequestDefaults({
            jar: true,
            followRedirect: false
        });
    });


    describe("The authorization endpoint", function () {

        it("redirects to eidopenid init", function () {
            return expectRequestToHave(makeOpenidInitRequest(), 302, /^..\/eidopenid\/auth\?/);
        });

        it('redirects all given parameters', function () {
            return makeOpenidInitRequest().then(function (respObj) {
                let regex = new RegExp(createParams().replace(/\s/, "%20"));
                expect(respObj).to.have.header('Location', function (location) {
                    return expect(decodeURIComponent(location)).to.match(regex);
                });
                return chakram.wait();
            });
        });

        it("does not redirect when client_id missing or invalid", function () {
            return makeOpenidInitRequest(createParams({'client_id': '1'})).then(function (respObj) {
                expect(respObj).to.have.status(200);
                expect(respObj.response.body).to.match(/The client identifier \(client_id\) is missing or invalid/);
                return chakram.wait();
            });
        });

        it("does not redirect when redirect uri does not match to client_id", function () {
            return makeOpenidInitRequest(createParams({'redirect_uri': 'http://foo.com'})).then(function (respObj) {
                expect(respObj).to.have.status(200);
                expect(respObj.response.body).to.match(/Redirect URI Error/);
                return chakram.wait();
            });
        });

        it("redirects to redirect uri with error when scope is malformed", function () {
            let redirectUri = env.OIDC_REDIRECT_URI;
            let regex = new RegExp(redirectUri.replace(/(^\w+:|^)\/\//, '') + "#error=invalid_scope");
            params = createParams({'scope': 'foo'});

            return expectRequestToHave(makeOpenidInitRequest(params), 302, regex);
        });

        it("redirects to redirect uri with error when nonce is malformed", function () {
            let redirectUri = env.OIDC_REDIRECT_URI;
            let regex = new RegExp(redirectUri.replace(/(^\w+:|^)\/\//, '') + "#error=invalid_request");
            params = createParams({'nonce' : ''});

            return expectRequestToHave(makeOpenidInitRequest(params), 302, regex);
        });
    });

    describe("The eId-Service after authentication", function () {

        it("redirects to openid provider", function () {
            locationPattern = ('/api/eidopenid/login/?eid_access_token=' + parseUuid(env.OIDC_ACCESS_TOKEN) +
                    '&' + env.OIDC_OPENID_PARAMETER);
            return expectRequestToHave(makeAfterAuthenticationValidEidServiceRequest(), 302, locationPattern);
        });

        it("does not redirect with malformed refreshid", function () {
            return expectRequestToHave(makeAfterAuthenticationMalformedEidServiceRequest(), 400);
        });

        it("does not redirect without refreshid", function () {
            return expectRequestToHave(makeAfterAuthenticationIncompleteEidServiceRequest(), 400);
        });

        it("does not redirect if refreshid is unknown", function () {
            return expectRequestToHave(makeAfterAuthenticationValidEidServiceRequestWithUnknownId(), 400);
        });

        it("does not redirect valid post", function () {
            return expectRequestToHave(makeAfterAuthenticationValidEidServiceRequest('post'), 403);
        });
    });

    describe("The authorization endpoint after authentication", function () {

        it("redirects to open id plugin", function () {
            return expectRequestToHave(makeAfterAuthenticationValidEndpointRequest(), 302);
        });

        it("does not redirect without access token", function () {
            return expectRequestToHave(makeAfterAuthenticationEndpointRequestWithoutToken(), 400);
        });

        it("does not redirect valid post", function () {
            return expectRequestToHave(makeAfterAuthenticationValidEndpointRequest('post'), 403);
        });
    });

    describe("The openid plugin after authentication", function () {

        var finalAuthRespObj;

        before(function () {
            return makeAfterAuthenticationValidEndpointRequest().then(function (endpointRespObj) {
                return makeFinalAuthenticationRequest(endpointRespObj).then(function (respObj) {
                    finalAuthRespObj = respObj;
                    return chakram.wait();
                });
            });
        });

        it("redirects to the client", function () {
            expect(finalAuthRespObj).to.have.status(302);
            expect(finalAuthRespObj).to.have.header('Location', /#access_token=[0-9a-f]*&id_token=[0-9A-z.-]*&token_type=bearer&expires_in=3600&state=[0-9a-f]*$/);
            return chakram.wait();
        });

        it("returns a valid id token containing the correct username", function () {
            let idtoken = finalAuthRespObj.response.headers.location.split('id_token=')[1].split('&')[0];
            let jwt = rsa.jws.JWS.parse(idtoken);
            let kid = jwt.headerObj.kid;
            return chakram.get(URL + '/openid/jwks').then(function (respObj) {
                let key = respObj.body.keys
                    .filter(function (n, i) {
                        return n.kid === kid;
                    });
                expect(key).to.not.be.empty;
                let publicKey = rsa.KEYUTIL.getKey(key[0]);
                expect(rsa.jws.JWS.verify(idtoken, publicKey)).to.be.true;
                expect(jwt.payloadObj.username).to.equal('b\'' + env.OIDC_RESTRICTED_ID + '\'');
                return chakram.wait();
            });
        });

        it("does not redirect if endpoint request is invalid", function () {
            return makeAfterAuthenticationValidEndpointRequest('post').then(function (endpointRespObj) {
                expect(endpointRespObj.response.headers.location).to.be.undefined;
                return chakram.wait();
            });
        });
    });
});
