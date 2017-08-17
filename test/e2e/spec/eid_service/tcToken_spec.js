describe("eID-Service: The tcToken generator", function() {

    var frisby = require('frisby');
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/getTcToken';

    beforeAll(function() {
        frisby.addExpectHandler('tc token', function(response) {
            let xml = response._body.replace(/\n/g, "").replace(/\r/g, "").replace(/ /g, "");

            expect(xml).toEqual(jasmine.stringMatching(/^<TCTokenType><ServerAddress>.*<\/Binding><\/TCTokenType>$/));
        });
    });

    it("returns a tc token", function(done) {
        frisby.get('https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/getTcTokenUrl', { redirect: 'manual' })
            .expect('status', 302)
            .then(function(response) {
                let location = response.headers._headers.location[0];
                let tcTokenUrl = location.split("?tcTokenUrl=")[1];
                return frisby.get(tcTokenUrl)
                    .expect('status', 200)
                    .expect('tc token');
            })
            .done(done);
    });

    it("fails without a GET parameter", function(done) {
        frisby.get(URL)
            .expect('status', 400)
        .done(done);
    });

        it("fails for invalid parameter", function(done) {
        frisby.get(URL + "?tcTokenId=bla")
            .expect('status', 400)
        .done(done);
    });

        it("fails for random tcTokenId", function(done) {
        frisby.get(URL + "?tcTokenId=8b99e301-3c96-4ebf-940d-9bb6506405e0")
            .expect('status', 400)
        .done(done);
    });

        it("fails for POST requests", function(done) {
        frisby.get(URL, { method: 'POST' })
            .expect('status', 403)
        .done(done);
    });
});