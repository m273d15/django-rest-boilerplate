describe("eID-Service: The refresh page", function() {

    var frisby = require('frisby');
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/refresh';
    
    it("is available", function(done) {
        frisby.get(URL)
            .expect('status', 400)
        .done(done);
    });
});
