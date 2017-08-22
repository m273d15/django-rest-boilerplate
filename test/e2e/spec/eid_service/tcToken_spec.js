describe("eID-Service: The tcToken generator", function() {

    var chakram = require('/usr/local/lib/node_modules/chakram/lib/chakram.js');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/getTcToken';

    before(function() {
        chakram.addProperty("tctoken", function(respObj) {
            let xml = respObj.body.replace(/\n/g, "").replace(/\r/g, "").replace(/ /g, "");
            expect(xml).to.match(/^<TCTokenType><ServerAddress>.*<\/Binding><\/TCTokenType>$/);
        });
    });

    it("returns a tc token", function() {
        var response = chakram.get('https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/getTcTokenUrl', { followRedirect: false });
        expect(response).to.have.status(302);
        return response.then(function(respObj) {
            let location = respObj.response.headers.location;
            let tcTokenUrl = location.split("?tcTokenUrl=")[1];
            var response = chakram.get(tcTokenUrl);
            expect(response).to.have.status(200);
            expect(response).to.be.tctoken;
            return chakram.wait();
        });
    });

    it("fails without a GET parameter", function() {
        var response = chakram.get(URL);
        return expect(response).to.have.status(400);
    });

    it("fails for invalid parameter", function() {
        var response = chakram.get(URL + "?tcTokenId=bla");
        return expect(response).to.have.status(400);
    });

    it("fails for random tcTokenId", function() {
        var response = chakram.get(URL + "?tcTokenId=8b99e301-3c96-4ebf-940d-9bb6506405e0");
        return expect(response).to.have.status(400);
    });

    it("fails for POST requests", function() {
        var response = chakram.post(URL);
        return expect(response).to.have.status(403);
    });
});