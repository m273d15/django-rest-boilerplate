describe("OpenId: The OIDC Plugin", function() {
    var chakram = require('chakram');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/openid'

    describe("provides an openid-configuration", function() {

        it("as json", function() {
            var response = chakram.get(URL + '/.well-known/openid-configuration');
            return expect(response).to.have.header('Content-Type', 'application/json');
        });

        it("with provider information", function() {
            var response = chakram.get(URL + '/.well-known/openid-configuration');
            expect(response).to.have.json('issuer', URL);
            expect(response).to.have.json('authorization_endpoint', URL + '/authorize');
            expect(response).to.have.json('jwks_uri', URL + '/jwks');
            return chakram.wait();
        });
    });

    it("provides an JSON web key set", function() {
        var response = chakram.get(URL + '/jwks');
        return expect(response).to.have.status(200);
    });
});
