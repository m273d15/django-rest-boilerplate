describe("eID-Service: The error page", function() {

    var chakram = require('chakram');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/error';

    before(function() {
        chakram.addProperty('correctErrorRedirect', function(respObj) {
            let location = respObj.response.headers.location;
            expect(location).to.match(/\/api\/openid\/login$/);
        });
    });

    it("redirects correct", function() {
        var response = chakram.get(URL, { followRedirect: false });
        expect(response).to.have.status(302);
        expect(response).to.be.correctErrorRedirect;
        return chakram.wait();
    });
});
