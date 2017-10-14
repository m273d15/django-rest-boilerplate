# End to End Tests

The end-to-end tests are located in this container, which mocks a user and executes the defined tests. The tests are arranged as components in the `spec` directory. Within each component directory, the tests are grouped by type with defining the test in one `*_spec.js` file.  

All these tests are implemented with the [chakram REST API test framework](http://dareid.github.io/chakram/jsdoc/index.html).

Additionally, the scripts `init_ci.sh`, `run_ci.sh`, `setup_testenvironment.sh` and `.env.test`, which are located in the root directory of the project, are important for setting up the environment and database for testing.


## Execution

To run the tests, use
```
docker-compose up --build
./setup_testenvironment.sh
```
to first set up the stack (allow some time for database initialization, if needed) and set all necessary environment variables. Then, 
```
docker-compose -f docker-compose.yml -f docker-compose.test.yml up --build test-e2e
```
to run the tests.

Local testing is also possible after installing node with
```
cd test/e2e
npm install
export BOILERPLATE_DOMAIN=eid.local
./node_modules/mocha/bin/mocha --recursive ./spec
```

## Manually reproduce testing the interface between provider and service
The provided links demonstrate the whole authentication process. Therefore, the `setup_testenvironment` script sets up the environment variables and enters a testuser in the database.  
Each step is defined in the description of the __Software Architecture#eid service__ section in the WIKI.
```
docker-compose up --build
./setup_testenvironment.sh
```
__Note: The script will throw two errors, but that is fine!__

### 1. Step: Client (KVV) --> OpenID Plugin
Link: http://eid.local/api/eidopenid/auth?response_type=id_token%20token&scope=openid&client_id=123456&state=b80525634e3e416b869fd421b76d087c&nonce=a8ebe80b194240f8ae301e2f3df8b43d&redirect_uri=http://localhost:3000

Redirects to: https://eid.local/api/openid/authorize?response_type=id_token%20token&scope=openid&client_id=123456&state=b80525634e3e416b869fd421b76d087c&nonce=a8ebe80b194240f8ae301e2f3df8b43d&redirect_uri=http://localhost:3000

### 2. Step: OpenID Plugin --> OpenID Provider
Link: https://eid.local/api/openid/authorize?response_type=id_token%20token&scope=openid&client_id=123456&state=b80525634e3e416b869fd421b76d087c&nonce=a8ebe80b194240f8ae301e2f3df8b43d&redirect_uri=http://localhost:3000

Redirects to: https://eid.local/api/eidopenid/auth?next=/api/openid/authorize%3Fresponse_type%3Did_token%2520token%26scope%3Dopenid%26client_id%3D123456%26state%3Db80525634e3e416b869fd421b76d087c%26nonce%3Da8ebe80b194240f8ae301e2f3df8b43d%26redirect_uri%3Dhttp%3A//localhost%3A3000

### 3. Step: OpenID Provider --> eID Service
Link: https://eid.local/api/eidopenid/auth?next=/api/openid/authorize%3Fresponse_type%3Did_token%2520token%26scope%3Dopenid%26client_id%3D123456%26state%3Db80525634e3e416b869fd421b76d087c%26nonce%3Da8ebe80b194240f8ae301e2f3df8b43d%26redirect_uri%3Dhttp%3A//localhost%3A3000

Redirects to: https://eid.local/api/eIdService/init?next=%2Fapi%2Fopenid%2Fauthorize%3Fresponse_type%3Did_token%2520token%26scope%3Dopenid%26client_id%3D123456%26state%3Db80525634e3e416b869fd421b76d087c%26nonce%3Da8ebe80b194240f8ae301e2f3df8b43d%26redirect_uri%3Dhttp%3A%2F%2Flocalhost%3A3000

### eID-Service Magic
**_After that, the authentication with the eid server happens and the AusweisApp redirects back to the eID-Service, finally._** The following shows the details:

**Checker (click on continue anyway...):**
https://eid.local/check/?next=%2Fapi%2Fopenid%2Fauthorize%3Fresponse_type%3Did_token%2520token%26scope%3Dopenid%26client_id%3D123456%26state%3Db80525634e3e416b869fd421b76d087c%26nonce%3Da8ebe80b194240f8ae301e2f3df8b43d%26redirect_uri%3Dhttp%3A%2F%2Flocalhost%3A3000

**eID-Service returns tc token url:**
http://127.0.0.1:24727/eID-Client?tcTokenUrl=https://eid.local/api/eIdService/getTcToken?tcTokenId=d454e1bd5757450bca0b4b9bd99a0a48

**Tc Token** (open https://eid.local/api/eIdService/getTcToken?tcTokenId=d454e1bd5757450bca0b4b9bd99a0a48):
```
<TCTokenType>
  <ServerAddress>https://eid.local/api/eID</ServerAddress>
  <SessionIdentifier>000e8018-1f0b-41ed-bd95-d1fac39cff25</SessionIdentifier>
  <RefreshAddress>
    https://eid.local/api/eIdService/refresh?refreshId=cd55df0f-4a7d-4a94-b9ab-59c3e04c1ead
  </RefreshAddress>
  <CommunicationErrorAddress>https://eid.local/api/eIdService/error</CommunicationErrorAddress>
  <Binding>urn:liberty:paos:2006-08</Binding>
</TCTokenType>
```
**Refresh Address**:
https://eid.local/api/eIdService/refresh?refreshId=cd55df0f-4a7d-4a94-b9ab-59c3e04c1ead

### 4. Step: eID Service --> OpenID Provider
Link: https://eid.local/api/eIdService/refresh?refreshId=cd55df0f-4a7d-4a94-b9ab-59c3e04c1ead

Redirects to: https://eid.local/api/eidopenid/login/?eid_access_token=6818aaab-e4f0-41d6-a4bf-a03b30424cab&next=%2Fapi%2Fopenid%2Fauthorize%3Fresponse_type%3Did_token%2520token%26scope%3Dopenid%26client_id%3D123456%26state%3Db80525634e3e416b869fd421b76d087c%26nonce%3Da8ebe80b194240f8ae301e2f3df8b43d%26redirect_uri%3Dhttp%3A%2F%2Flocalhost%3A3000

### 5. Step: OpenID Provider <--> eID Service
OpenID Provider gets userID from eID-Service by calling python function, no test provided.

### 6. Step: OpenID Provider --> Client (KVV)
Link: https://eid.local/api/eidopenid/login/?eid_access_token=6818aaab-e4f0-41d6-a4bf-a03b30424cab&next=%2Fapi%2Fopenid%2Fauthorize%3Fresponse_type%3Did_token%2520token%26scope%3Dopenid%26client_id%3D123456%26state%3Db80525634e3e416b869fd421b76d087c%26nonce%3Da8ebe80b194240f8ae301e2f3df8b43d%26redirect_uri%3Dhttp%3A%2F%2Flocalhost%3A3000

Redirects to: http://localhost:3000/#access_token=36e4583e06ae4f918483e050deacf3ca&id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImM2NzJiZWQ5OTgyZWI4MDMzODJmNmYxNzdjMDI3MGYwIn0.eyJpc3MiOiJodHRwczovL2VpZC5sb2NhbC9hcGkvb3BlbmlkIiwic3ViIjoiMSIsImF1ZCI6IjEyMzQ1NiIsImV4cCI6MTUwNjU5MDkxNSwiaWF0IjoxNTA2NTkwMzE1LCJhdXRoX3RpbWUiOjE1MDY1OTAzMTQsIm5vbmNlIjoiYThlYmU4MGIxOTQyNDBmOGFlMzAxZTJmM2RmOGI0M2QiLCJhdF9oYXNoIjoidU1fSWVKZV9KTjI3UFR0ekMzVXlEdyIsInVzZXJuYW1lIjoiYidkZWFkYmVlZicifQ.PHYIeT9a94vhJaxpxBix8AeM296zfOHiTHBo5977xk3ggUGhhqKQIzNz7T1dEEmDmFRb3rWSbl6oxblegNxke4VkzuqNOfA7l7xAzQ6XcMVVOqTMAIxLdDex9LgFD7yIX1yvMo2pwQx8AuSy8eNiJAjEGXYm9sIrijTSQpfVThM&token_type=bearer&expires_in=3600&state=b80525634e3e416b869fd421b76d087c

### [Optional] Read id token
Open https://jwt.io/ and paste the id token. The username can be read from the payload. The signature cannot be verified using this website. See the tests for information about verifying a token.

**ID Token:**
```
eyJhbGciOiJSUzI1NiIsImtpZCI6ImM2NzJiZWQ5OTgyZWI4MDMzODJmNmYxNzdjMDI3MGYwIn0.eyJpc3MiOiJodHRwczovL2VpZC5sb2NhbC9hcGkvb3BlbmlkIiwic3ViIjoiMSIsImF1ZCI6IjEyMzQ1NiIsImV4cCI6MTUwNjU5MDkxNSwiaWF0IjoxNTA2NTkwMzE1LCJhdXRoX3RpbWUiOjE1MDY1OTAzMTQsIm5vbmNlIjoiYThlYmU4MGIxOTQyNDBmOGFlMzAxZTJmM2RmOGI0M2QiLCJhdF9oYXNoIjoidU1fSWVKZV9KTjI3UFR0ekMzVXlEdyIsInVzZXJuYW1lIjoiYidkZWFkYmVlZicifQ.PHYIeT9a94vhJaxpxBix8AeM296zfOHiTHBo5977xk3ggUGhhqKQIzNz7T1dEEmDmFRb3rWSbl6oxblegNxke4VkzuqNOfA7l7xAzQ6XcMVVOqTMAIxLdDex9LgFD7yIX1yvMo2pwQx8AuSy8eNiJAjEGXYm9sIrijTSQpfVThM
```
**Payload:**
```
{
  "iss": "https://eid.local/api/openid",
  "sub": "1",
  "aud": "123456",
  "exp": 1506590915,
  "iat": 1506590315,
  "auth_time": 1506590314,
  "nonce": "a8ebe80b194240f8ae301e2f3df8b43d",
  "at_hash": "uM_IeJe_JN27PTtzC3UyDw",
  "username": "b'deadbeef'"
}
```