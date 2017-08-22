describe("eID-Service: The error page", function() {

    var chakram = require('/usr/local/lib/node_modules/chakram/lib/chakram.js');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/error';

    it("is available", function() {
        var response = chakram.get(URL);
        return expect(response).to.have.status(200);
    });
});
