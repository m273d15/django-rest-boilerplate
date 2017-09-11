describe("eID-Service: The refresh page", function() {
    
    var chakram = require('chakram');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/refresh';

    before(function() {
        chakram.addProperty('correctRefreshRedirect', function(respObj) {
            let location = respObj.response.headers.location;
            expect(location).to.match(/\/api\/eidopenid\/login\/?\?eid_access_token=.*[&]test=bla[&]foo=bar$/);
        });
    });

    it("fails without a GET parameter", function() {
        var response = chakram.get(URL);
        return expect(response).to.have.status(400);
    });

    it("fails for invalid parameter", function() {
        var response = chakram.get(URL + "?refreshId=bla");
        return expect(response).to.have.status(400);
    });

    it("fails for random refreshId", function() {
        var response = chakram.get(URL + "?refreshId=8b99e301-3c96-4ebf-940d-9bb6506405e0");
        return expect(response).to.have.status(400);
    });

    it("fails for POST requests", function() {
        var response = chakram.post(URL);
        return expect(response).to.have.status(403);
    });

    it("redirects correctly with GET parameters", function() {
        var response = chakram.get('https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/getTcTokenUrl?test=bla&foo=bar', { followRedirect: false });
        expect(response).to.have.status(302);
        return response.then(function(respObj) {
            let location = respObj.response.headers.location;
            let tcTokenUrl = location.split("?tcTokenUrl=")[1];
            var response = chakram.get(tcTokenUrl);
            expect(response).to.have.status(200);
            return response.then(function(respObj) {
                let body = respObj.body;
                let refreshUrl = body.split("<RefreshAddress> ")[1].split(" </RefreshAddress>")[0];
                var response = chakram.get(refreshUrl, { followRedirect: false });
                expect(response).to.have.status(302);
                expect(response).to.be.correctRefreshRedirect;
                return chakram.wait();
            });
        });
    });
});
