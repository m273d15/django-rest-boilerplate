describe("OpenId: JWKS", function () {

    var chakram = require('chakram');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/openid/jwks';

    it("does not provide JWK for invalid key id", function () {
        var kid = "c79009497df978f22foobard9ac74b43732"
        return chakram.get(URL)
            .then(function (respObj) {
                let key = respObj.body.keys
                    .filter(function (n, i) {
                        return n.kid === kid;
                    });
                return expect(key).to.be.empty;
            });
    });
});
