from django.core.management.base import BaseCommand, CommandError
from oidc_provider.models import Client


class Command(BaseCommand):
    help = 'Register a client at the openid provider'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs=1, type=str)
        parser.add_argument('client_id', nargs=1, type=str)
        parser.add_argument('response_type', nargs=1, type=str)
        parser.add_argument('redirect_uris', nargs='+', type=str)
        parser.add_argument('client_secret', nargs='?', type=str, default='')
        parser.add_argument('client_type', nargs='?', type=str, default='public')
        parser.add_argument('reuse_consent', nargs='?', type=bool, default=False)
        parser.add_argument('require_consent', nargs='?', type=bool, default=False)

    def handle(self, *args, **options):
        name = options['name'][0]
        client_id = options['client_id'][0]
        client_secret = options['client_secret']
        client_type = options['client_type']
        response_type = options['response_type'][0]
        redirect_uris = options['redirect_uris']
        reuse_consent = options['reuse_consent']
        require_consent = options['require_consent']

        c = Client(name=name, client_id=client_id, client_secret=client_secret, client_type=client_type, response_type=response_type, redirect_uris=redirect_uris, reuse_consent=reuse_consent, require_consent=require_consent)
        c.save()
