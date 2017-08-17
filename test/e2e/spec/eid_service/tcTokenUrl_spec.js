describe("eID-Service: The tcTokenUrl generator", function() {

    var frisby = require('frisby');
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eIdService/getTcTokenUrl';

    beforeAll(function() {
        frisby.addExpectHandler('correct redirect', function(response) {
            let header = response.headers._headers;
            expect(header.location[0]).toEqual(jasmine.stringMatching(/^(http|eid):\/\/(localhost|127\.0\.0\.1):24727\/eID-Client\?tcTokenUrl=/));
        });
    });

    it("redirects by default", function(done) {
        frisby.get(URL, { redirect: 'manual' })
          .expect('status', 302)
          .expect('correct redirect')
        .done(done);
    });

    it("redirects according to hosts", function(done) {
        frisby.get(URL + '?host=localhost', { redirect: 'manual' })
          .expect('status', 302)
          .expect('correct redirect')
        .done(done);

        frisby.get(URL + '?host=127.0.0.1', { redirect: 'manual' })
          .expect('status', 302)
          .expect('correct redirect')
        .done(done);
    });

    it("redirects according to protocol", function(done) {
        frisby.get(URL + '?protocol=http', { redirect: 'manual' })
          .expect('status', 302)
          .expect('correct redirect')
        .done(done);

        frisby.get(URL + '?protocol=eid', { redirect: 'manual' })
          .expect('status', 302)
          .expect('correct redirect')
        .done(done);
    });

    it("redirects according to host and protocol", function(done) {
        frisby.get(URL + '?protocol=http&host=localhost', { redirect: 'manual' })
          .expect('status', 302)
          .expect('correct redirect')
        .done(done);

        frisby.get(URL + '?protocol=eid&host=127.0.0.1', { redirect: 'manual' })
          .expect('status', 302)
          .expect('correct redirect')
        .done(done);
    });

    it("fails for false arguments for host", function(done) {
        frisby.get(URL + '?host=lol')
          .expect('status', 400)
        .done(done);
    });

    it("fails for false arguments for protocol", function(done) {
        frisby.get(URL + '?protocol=lol')
          .expect('status', 400)
        .done(done);
    });

    it("fails for POST requests", function(done) {
        frisby.get(URL, { method: 'POST' })
          .expect('status', 403)
        .done(done);
    });
});
