describe("eId OpenId: Login", function() {

    var chakram = require('chakram');
    var expect = chakram.expect;
    var URL = 'https://' + process.env.BOILERPLATE_DOMAIN + '/api/eidopenid/login/';

    it('fails for POSTs', function(){
        var response = chakram.post(URL);
        return expect(response).to.have.status(403);
    });

    it('fails for GET without or bad redirect uri', function(){
        var response = chakram.get(URL);
        return expect(response).to.have.status(400);
    });

    it('fails for GET without or malformed eid access token', function(){
        let access_token = 'eid_access_token=1234';
        let request = URL + '?next=/&' + access_token;
        var response = chakram.get(request);
        return expect(response).to.have.status(400);
    });

    it('does not redirect to redirect address when redirect uri and invalid eid access token is given', function(){
        let access_token = 'eid_access_token=6fe1a16c-42d0-452f-bd67-d299c8cf0067';
        let request = URL + '?next=/&' + access_token;
        var response = chakram.get(request);
        return expect(response).to.have.status(400);
    });
});
