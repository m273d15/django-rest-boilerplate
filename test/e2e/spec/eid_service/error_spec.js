describe("eID-Service: The error page", function() {

    var frisby = require('frisby');
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/error';
    
    it("is available", function(done) {
        frisby.get(URL)
            .expect('status', 200)
        .done(done);
    });
});
