# custom oidc token processing hook for adding user data to id_token
def idtoken_processing_hook(id_token, user):
    id_token['username'] = user.get_username()
    return id_token
