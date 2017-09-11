describe("Ngnix/django", function() {

    var chakram = require('chakram');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN;

    it("provides an index page", function() {
        var response = chakram.get(URL + '/');
        return expect(response).to.have.status(200);
    });

    it("provides an admin page", function() {
        var response = chakram.get(URL + '/api/admin', { followRedirect: true });
        return expect(response).to.have.status(200);
    });

    it("provides an admin login page", function() {
        var response = chakram.get(URL + '/api/admin/login/', { followRedirect: true });
        return expect(response).to.have.status(200);
    });
});
