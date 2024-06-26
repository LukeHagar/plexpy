"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from plex_api import utils
from typing import Optional

GET_TOKEN_SERVERS = [
	"https://plex.tv/api/v2",
]


@dataclasses.dataclass
class GetTokenGlobals:
    x_plex_client_identifier: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Plex-Client-Identifier', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)
    """
    



@dataclasses.dataclass
class GetTokenRequest:
    pin_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pinID', 'style': 'simple', 'explode': False }})
    r"""The PinID to retrieve an access token for"""
    x_plex_client_identifier: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Plex-Client-Identifier', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the client application
    This is used to track the client application and its usage
    (UUID, serial number, or other number unique per device)
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTokenLocation:
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    european_union_member: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('european_union_member'), 'exclude': lambda f: f is None }})
    continent_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('continent_code'), 'exclude': lambda f: f is None }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    time_zone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_zone'), 'exclude': lambda f: f is None }})
    postal_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postal_code'), 'exclude': lambda f: f is None }})
    in_privacy_restricted_country: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('in_privacy_restricted_country'), 'exclude': lambda f: f is None }})
    subdivisions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdivisions'), 'exclude': lambda f: f is None }})
    coordinates: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('coordinates'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTokenResponseBody:
    r"""Access Token"""
    id: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""PinID for use with authentication"""
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    product: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product'), 'exclude': lambda f: f is None }})
    trusted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trusted'), 'exclude': lambda f: f is None }})
    qr: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('qr'), 'exclude': lambda f: f is None }})
    r"""a link to a QR code hosted on plex.tv
    The QR code redirects to the relevant `plex.tv/link` authentication page
    Which then prompts the user for the 4 Digit Link Pin
    """
    client_identifier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientIdentifier'), 'exclude': lambda f: f is None }})
    location: Optional[GetTokenLocation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    expires_in: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiresIn'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiresAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    auth_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authToken'), 'exclude': lambda f: f is None }})
    new_registration: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newRegistration'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetTokenResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[GetTokenResponseBody] = dataclasses.field(default=None)
    r"""Access Token"""
    

