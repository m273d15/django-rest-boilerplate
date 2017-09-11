#!/bin/bash

function source_env() {
    env_file=.env.test

    while IFS= read -r var
    do
        cleaned=$(echo "$var" | tr -d "[:space:]")
        [ -z "$cleaned" ] && continue

        v_name=$(echo "$var" | cut -d= -f1)
        v_value=$(echo "$var" | cut -d= -f2-)

        export "$v_name"="$v_value"
    done < "$env_file"
}

source_env

docker-compose exec api python manage.py creatersakey
docker-compose exec api python manage.py registerclient "test client" $OIDC_CLIENT_ID "$OIDC_RESPONSE_TYPE" $OIDC_REDIRECT_URI
echo "INSERT INTO eid_service_authenticationrequest (tctokenid, sessionid, refreshid, accesstoken, openidparameter, restrictedid) VALUES (\"$OIDC_TCTOKEN_ID\", \"$OIDC_SESSION_ID\", \"$OIDC_REFRESH_ID\", \"$OIDC_ACCESS_TOKEN\", \"$OIDC_OPENID_PARAMETER\", \"$OIDC_RESTRICTED_ID\");" | docker-compose exec db mysql -u root api
echo "INSERT INTO eid_server_servicerequest (sessionid, restrictedid) VALUES (\"$OIDC_SESSION_ID\", \"$OIDC_RESTRICTED_ID\");" | docker-compose exec db mysql -u root api

exit 0
