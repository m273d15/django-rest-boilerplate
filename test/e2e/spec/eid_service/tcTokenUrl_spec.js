describe("eID-Service: The tcTokenUrl generator", function() {

    var chakram = require('/usr/local/lib/node_modules/chakram/lib/chakram.js');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/getTcTokenUrl';

    before(function() {
        chakram.addProperty('correctRedirect', function(respObj) {
            let location = respObj.response.headers.location;
            expect(location).to.match(/^(http|eid):\/\/(localhost|127\.0\.0\.1):24727\/eID-Client\?tcTokenUrl=/);
        });
    });

    it("redirects by default", function() {
        var response = chakram.get(URL, { followRedirect: false });
        expect(response).to.have.status(302);
        expect(response).to.be.correctRedirect;
        return chakram.wait();
    });

    it("redirects according to hosts", function() {
        var localhost = chakram.get(URL + '?host=localhost', { followRedirect: false });
        expect(localhost).to.have.status(302);
        expect(localhost).to.be.correctRedirect;

        var alternative = chakram.get(URL + '?host=127.0.0.1', { followRedirect: false });
        expect(alternative).to.have.status(302);
        expect(alternative).to.be.correctRedirect;

        return chakram.wait();
    });

    it("redirects according to protocol", function() {
        var http = chakram.get(URL + '?protocol=http', { followRedirect: false });
        expect(http).to.have.status(302);
        expect(http).to.be.correctRedirect;

        var eid = chakram.get(URL + '?protocol=eid', { followRedirect: false });
        expect(eid).to.have.status(302);
        expect(eid).to.be.correctRedirect;

        return chakram.wait();
    });

    it("redirects according to host and protocol", function() {
        var httpLocalhost = chakram.get(URL + '?protocol=http&host=localhost', { followRedirect: false });
        expect(httpLocalhost).to.have.status(302);
        expect(httpLocalhost).to.be.correctRedirect;

        var eidAlternative = chakram.get(URL + '?protocol=eid&host=127.0.0.1', { followRedirect: false });
        expect(eidAlternative).to.have.status(302);
        expect(eidAlternative).to.be.correctRedirect;

        return chakram.wait();
    });

    it("fails for false arguments for host", function() {
        var response = chakram.get(URL + '?host=lol', { followRedirect: false });
        return expect(response).to.have.status(400);
    });

    it("fails for false arguments for protocol", function() {
        var response = chakram.get(URL + '?protocol=lol', { followRedirect: false });
        return expect(response).to.have.status(400);
    });

    it("fails for POST requests", function() {
        var response = chakram.post(URL, "post", { followRedirect: false });
        return expect(response).to.have.status(403);
    });
});
