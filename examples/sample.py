from os import getenv
from pprint import pprint
from plexsdk import PlexSDK

sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))

results = sdk.server.get_server_capabilities()

pprint(vars(results))
