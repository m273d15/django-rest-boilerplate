describe("eId OpenId: A json webtoken", function () {

    var chakram = require('chakram');
    var r = require('jsrsasign');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eidopenid/login/';

    it("can be verified", function () {
        let token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImZlMDA4M2MwYWZlYWE4MTY0MmRmNjA2MDA1NDhjYjkwIn0.eyJpc3MiOiJodHRwczovL2VpZC5sb2NhbC9hcGkvb3BlbmlkIiwic3ViIjoiMiIsImF1ZCI6IjEyMzQ1NiIsImV4cCI6MTUwNDUwOTk0NSwiaWF0IjoxNTA0NTA5MzQ1LCJhdXRoX3RpbWUiOjE1MDQ1MDkzNDMsIm5vbmNlIjoiMjkzZjg1NzIwOWJjNDdhODhlODU0Njk2NjQ1MTFhY2EiLCJhdF9oYXNoIjoiSFNWb1l6aGRpVUFtbm44Wlp4NC1aQSIsInVzZXJuYW1lIjoiYicnIn0.mzFEHAuYahzMlGlj620JVLgFAzfjkEO_JAeqA4cfGzkxeZ5r9e7i8HGMiV9iI9gtRq34kBoESKWm6cWwNQJ3RnIYmhuOW60sfkzOnafk4joRmgMi15YsfdZsZukoKX_BQJdsglXsNzivo-ORE8tHSLDyzyqSnL2Rumcz6FoGtTM';
        let publicKey = r.KEYUTIL.getKey({
            kty: "RSA",
            "alg": "RS256",
            "use": "sig",
            "kid": "fe0083c0afeaa81642df60600548cb90",
            e: 'AQAB',
            n: 'sVb-WvR824t96MVFB8KefvmVk6hzBr4kJKG0vghp4Ze-18UDnSvoRGcuWjmbtIsEN3Sseu7wb9Ef7SgDe5TjPwglbfjtBeQ2OO0Fx5y0sCxJw9OJZ1HMDd3tn7x9dHMKnbJgSkGPrYNcQK0XqR3Oj9Hy-BT0y9YpopWuEkP4OxE'
        });
        let jwt = r.jws.JWS.parse(token);
        expect(r.jws.JWS.verify(token, publicKey)).to.be.true;
    });
});
