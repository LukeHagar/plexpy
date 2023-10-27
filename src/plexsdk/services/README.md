# PlexSDK Services
A list of all services and services methods.
- Services

    - [Server](#server)

    - [Media](#media)

    - [Activities](#activities)

    - [Butler](#butler)

    - [Hubs](#hubs)

    - [Search](#search)

    - [Library](#library)

    - [Log](#log)

    - [Playlists](#playlists)

    - [Security](#security)

    - [Sessions](#sessions)

    - [Updater](#updater)

    - [Video](#video)
- [All Methods](#all-methods)


## Server

| Method    | Description|
| :-------- | :----------| 
| [get_server_capabilities](#get_server_capabilities) | Server Capabilities |
| [get_server_preferences](#get_server_preferences) | Get Server Preferences |
| [get_available_clients](#get_available_clients) | Get Available Clients |
| [get_devices](#get_devices) | Get Devices |
| [get_server_identity](#get_server_identity) | Get Server Identity |
| [get_my_plex_account](#get_my_plex_account) | Get MyPlex Account |
| [get_resized_photo](#get_resized_photo) | Get a Resized Photo |
| [get_server_list](#get_server_list) | Get Server List |


## Media

| Method    | Description|
| :-------- | :----------| 
| [mark_played](#mark_played) | Mark Media Played |
| [mark_unplayed](#mark_unplayed) | Mark Media Unplayed |
| [update_play_progress](#update_play_progress) | Update Media Play Progress |


## Activities

| Method    | Description|
| :-------- | :----------| 
| [get_server_activities](#get_server_activities) | Get Server Activities |
| [cancel_server_activities](#cancel_server_activities) | Cancel Server Activities |


## Butler

| Method    | Description|
| :-------- | :----------| 
| [start_all_tasks](#start_all_tasks) | Start all Butler tasks |
| [get_butler_tasks](#get_butler_tasks) | Get Butler tasks |
| [stop_all_tasks](#stop_all_tasks) | Stop all Butler tasks |
| [start_task](#start_task) | Start a single Butler task |
| [stop_task](#stop_task) | Stop a single Butler task |


## Hubs

| Method    | Description|
| :-------- | :----------| 
| [get_global_hubs](#get_global_hubs) | Get Global Hubs |
| [get_library_hubs](#get_library_hubs) | Get library specific hubs |


## Search

| Method    | Description|
| :-------- | :----------| 
| [perform_search](#perform_search) | Perform a search |
| [perform_voice_search](#perform_voice_search) | Perform a voice search |
| [get_search_results](#get_search_results) | Get Search Results |


## Library

| Method    | Description|
| :-------- | :----------| 
| [get_file_hash](#get_file_hash) | Get Hash Value |
| [get_recently_added](#get_recently_added) | Get Recently Added |
| [get_libraries](#get_libraries) | Get All Libraries |
| [get_library](#get_library) | Get Library Details |
| [delete_library](#delete_library) | Delete Library Section |
| [get_library_items](#get_library_items) | Get Library Items |
| [refresh_library](#refresh_library) | Refresh Library |
| [get_latest_library_items](#get_latest_library_items) | Get Latest Library Items |
| [get_common_library_items](#get_common_library_items) | Get Common Library Items |
| [get_metadata](#get_metadata) | Get Items Metadata |
| [get_metadata_children](#get_metadata_children) | Get Items Children |
| [get_on_deck](#get_on_deck) | Get On Deck |


## Log

| Method    | Description|
| :-------- | :----------| 
| [log_multi_line](#log_multi_line) | Logging a multi-line message |
| [log_line](#log_line) | Logging a single line message. |
| [enable_paper_trail](#enable_paper_trail) | Enabling Papertrail |


## Playlists

| Method    | Description|
| :-------- | :----------| 
| [create_playlist](#create_playlist) | Create a Playlist |
| [get_playlists](#get_playlists) | Get All Playlists |
| [get_playlist](#get_playlist) | Retrieve Playlist |
| [delete_playlist](#delete_playlist) | Deletes a Playlist |
| [update_playlist](#update_playlist) | Update a Playlist |
| [get_playlist_contents](#get_playlist_contents) | Retrieve Playlist Contents |
| [clear_playlist_contents](#clear_playlist_contents) | Delete Playlist Contents |
| [add_playlist_contents](#add_playlist_contents) | Adding to a Playlist |
| [upload_playlist](#upload_playlist) | Upload Playlist |


## Security

| Method    | Description|
| :-------- | :----------| 
| [get_transient_token](#get_transient_token) | Get a Transient Token. |
| [get_source_connection_information](#get_source_connection_information) | Get Source Connection Information |


## Sessions

| Method    | Description|
| :-------- | :----------| 
| [get_sessions](#get_sessions) | Get Active Sessions |
| [get_session_history](#get_session_history) | Get Session History |
| [get_transcode_sessions](#get_transcode_sessions) | Get Transcode Sessions |
| [stop_transcode_session](#stop_transcode_session) | Stop a Transcode Session |


## Updater

| Method    | Description|
| :-------- | :----------| 
| [get_update_status](#get_update_status) | Querying status of updates |
| [check_for_updates](#check_for_updates) | Checking for updates |
| [apply_updates](#apply_updates) | Apply Updates |


## Video

| Method    | Description|
| :-------- | :----------| 
| [start_universal_transcode](#start_universal_transcode) | Start Universal Transcode |
| [get_timeline](#get_timeline) | Get the timeline for a media item |




## All Methods


### **get_server_capabilities**
Server Capabilities
- HTTP Method: GET
- Endpoint: /

**Parameters**

This method has no parameters.

**Return Type**

[GetServerCapabilitiesResponse](/src/plexsdk/models/README.md#getservercapabilitiesresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_server_capabilities()

pprint(vars(results))

```

### **get_server_preferences**
Get Server Preferences
- HTTP Method: GET
- Endpoint: /:/prefs

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_server_preferences()

pprint(vars(results))

```

### **get_available_clients**
Get Available Clients
- HTTP Method: GET
- Endpoint: /clients

**Parameters**

This method has no parameters.

**Return Type**

[GetAvailableClientsResponse](/src/plexsdk/models/README.md#getavailableclientsresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_available_clients()

pprint(vars(results))

```

### **get_devices**
Get Devices
- HTTP Method: GET
- Endpoint: /devices

**Parameters**

This method has no parameters.

**Return Type**

[GetDevicesResponse](/src/plexsdk/models/README.md#getdevicesresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_devices()

pprint(vars(results))

```

### **get_server_identity**
Get Server Identity
- HTTP Method: GET
- Endpoint: /identity

**Parameters**

This method has no parameters.

**Return Type**

[GetServerIdentityResponse](/src/plexsdk/models/README.md#getserveridentityresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_server_identity()

pprint(vars(results))

```

### **get_my_plex_account**
Get MyPlex Account
- HTTP Method: GET
- Endpoint: /myplex/account

**Parameters**

This method has no parameters.

**Return Type**

[GetMyPlexAccountResponse](/src/plexsdk/models/README.md#getmyplexaccountresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_my_plex_account()

pprint(vars(results))

```

### **get_resized_photo**
Get a Resized Photo
- HTTP Method: GET
- Endpoint: /photo/:/transcode

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| width | float | Required | The width for the resized photo |
| height | float | Required | The height for the resized photo |
| opacity | int | Required | The opacity for the resized photo |
| blur | float | Required | The width for the resized photo |
| min_size | [MinSize](/src/plexsdk/models/README.md#minsize) | Required | images are always scaled proportionally. A value of '1' in minSize will make the smaller native dimension the dimension resized against. |
| upscale | [Upscale](/src/plexsdk/models/README.md#upscale) | Required | allow images to be resized beyond native dimensions. |
| url | str | Required | path to image within Plex |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_resized_photo(
	width = 110,
	height = 165,
	opacity = 100,
	blur = 4000,
	min_size = 1,
	upscale = 1,
	url = '/library/metadata/49564/thumb/1654258204'
)

pprint(vars(results))

```

### **get_server_list**
Get Server List
- HTTP Method: GET
- Endpoint: /servers

**Parameters**

This method has no parameters.

**Return Type**

[GetServerListResponse](/src/plexsdk/models/README.md#getserverlistresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.server.get_server_list()

pprint(vars(results))

```


### **mark_played**
Mark Media Played
- HTTP Method: GET
- Endpoint: /:/scrobble

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| key | float | Required | The media key to mark as played |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.media.mark_played(key = 59398)

pprint(vars(results))

```

### **mark_unplayed**
Mark Media Unplayed
- HTTP Method: GET
- Endpoint: /:/unscrobble

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| key | float | Required | The media key to mark as Unplayed |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.media.mark_unplayed(key = 59398)

pprint(vars(results))

```

### **update_play_progress**
Update Media Play Progress
- HTTP Method: POST
- Endpoint: /:/progress

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| key | str | Required | the media key |
| time | float | Required | The time, in milliseconds, used to set the media playback progress. |
| state | str | Required | The playback state of the media item. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.media.update_play_progress(
	key = 'key',
	time = -21007029.127889782,
	state = 'state'
)

pprint(vars(results))

```


### **get_server_activities**
Get Server Activities
- HTTP Method: GET
- Endpoint: /activities

**Parameters**

This method has no parameters.

**Return Type**

[GetServerActivitiesResponse](/src/plexsdk/models/README.md#getserveractivitiesresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.activities.get_server_activities()

pprint(vars(results))

```

### **cancel_server_activities**
Cancel Server Activities
- HTTP Method: DELETE
- Endpoint: /activities/{activityUUID}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| activity_uuid | str | Required | The UUID of the activity to cancel. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.activities.cancel_server_activities(activity_uuid = 'activityUUID')

pprint(vars(results))

```


### **start_all_tasks**
Start all Butler tasks
- HTTP Method: POST
- Endpoint: /butler

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.butler.start_all_tasks()

pprint(vars(results))

```

### **get_butler_tasks**
Get Butler tasks
- HTTP Method: GET
- Endpoint: /butler

**Parameters**

This method has no parameters.

**Return Type**

[GetButlerTasksResponse](/src/plexsdk/models/README.md#getbutlertasksresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.butler.get_butler_tasks()

pprint(vars(results))

```

### **stop_all_tasks**
Stop all Butler tasks
- HTTP Method: DELETE
- Endpoint: /butler

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.butler.stop_all_tasks()

pprint(vars(results))

```

### **start_task**
Start a single Butler task
- HTTP Method: POST
- Endpoint: /butler/{taskName}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| task_name | [TaskName](/src/plexsdk/models/README.md#taskname) | Required | the name of the task to be started. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.butler.start_task(task_name = 'BackupDatabase')

pprint(vars(results))

```

### **stop_task**
Stop a single Butler task
- HTTP Method: DELETE
- Endpoint: /butler/{taskName}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| task_name | [TaskName](/src/plexsdk/models/README.md#taskname) | Required | The name of the task to be started. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.butler.stop_task(task_name = 'GenerateAutoTags')

pprint(vars(results))

```


### **get_global_hubs**
Get Global Hubs
- HTTP Method: GET
- Endpoint: /hubs

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| count | float | Optional | The number of items to return with each hub. |
| only_transient | [OnlyTransient](/src/plexsdk/models/README.md#onlytransient) | Optional | Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added). |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.hubs.get_global_hubs(
	count = -25530716.436555773,
	only_transient = 1
)

pprint(vars(results))

```

### **get_library_hubs**
Get library specific hubs
- HTTP Method: GET
- Endpoint: /hubs/sections/{sectionId}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| section_id | float | Required | the Id of the library to query |
| count | float | Optional | The number of items to return with each hub. |
| only_transient | [OnlyTransient](/src/plexsdk/models/README.md#onlytransient) | Optional | Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added). |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.hubs.get_library_hubs(
	section_id = 89136618.25964785,
	count = -44116336.8194041,
	only_transient = 1
)

pprint(vars(results))

```


### **perform_search**
Perform a search
- HTTP Method: GET
- Endpoint: /hubs/search

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| query | str | Required | The query term |
| section_id | float | Optional | This gives context to the search, and can result in re-ordering of search result hubs |
| limit | float | Optional | The number of items to return per hub |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.search.perform_search(
	query = 'dylan',
	section_id = 69456479.38410482,
	limit = 5
)

pprint(vars(results))

```

### **perform_voice_search**
Perform a voice search
- HTTP Method: GET
- Endpoint: /hubs/search/voice

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| query | str | Required | The query term |
| section_id | float | Optional | This gives context to the search, and can result in re-ordering of search result hubs |
| limit | float | Optional | The number of items to return per hub |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.search.perform_voice_search(
	query = 'dead+poop',
	section_id = -89240370.29516296,
	limit = 5
)

pprint(vars(results))

```

### **get_search_results**
Get Search Results
- HTTP Method: GET
- Endpoint: /search

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| query | str | Required | The search query string to use |

**Return Type**

[GetSearchResultsResponse](/src/plexsdk/models/README.md#getsearchresultsresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.search.get_search_results(query = '110')

pprint(vars(results))

```


### **get_file_hash**
Get Hash Value
- HTTP Method: GET
- Endpoint: /library/hashes

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| url | str | Required | This is the path to the local file, must be prefixed by `file://` |
| type | float | Optional | Item type |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_file_hash(
	url = 'file://C:\Image.png&type=13',
	type = -93479594.8520502
)

pprint(vars(results))

```

### **get_recently_added**
Get Recently Added
- HTTP Method: GET
- Endpoint: /library/recentlyAdded

**Parameters**

This method has no parameters.

**Return Type**

[GetRecentlyAddedResponse](/src/plexsdk/models/README.md#getrecentlyaddedresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_recently_added()

pprint(vars(results))

```

### **get_libraries**
Get All Libraries
- HTTP Method: GET
- Endpoint: /library/sections

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_libraries()

pprint(vars(results))

```

### **get_library**
Get Library Details
- HTTP Method: GET
- Endpoint: /library/sections/{sectionId}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| section_id | float | Required | the Id of the library to query |
| include_details | [IncludeDetails](/src/plexsdk/models/README.md#includedetails) | Optional | Whether or not to include details for a section (types, filters, and sorts). <br>Only exists for backwards compatibility, media providers other than the server libraries have it on always.<br> |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_library(
	section_id = 1000,
	include_details = 42.1
)

pprint(vars(results))

```

### **delete_library**
Delete Library Section
- HTTP Method: DELETE
- Endpoint: /library/sections/{sectionId}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| section_id | float | Required | the Id of the library to query |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.delete_library(section_id = 1000)

pprint(vars(results))

```

### **get_library_items**
Get Library Items
- HTTP Method: GET
- Endpoint: /library/sections/{sectionId}/all

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| section_id | float | Required | the Id of the library to query |
| type | float | Optional | item type |
| filter | str | Optional | the filter parameter |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_library_items(
	section_id = -59611894.83078693,
	type = 61422299.35649505,
	filter = 'filter'
)

pprint(vars(results))

```

### **refresh_library**
Refresh Library
- HTTP Method: GET
- Endpoint: /library/sections/{sectionId}/refresh

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| section_id | float | Required | the Id of the library to refresh |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.refresh_library(section_id = -18672976.902678773)

pprint(vars(results))

```

### **get_latest_library_items**
Get Latest Library Items
- HTTP Method: GET
- Endpoint: /library/sections/{sectionId}/latest

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| section_id | float | Required | the Id of the library to query |
| type | float | Required | item type |
| filter | str | Optional | the filter parameter |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_latest_library_items(
	section_id = -58307061.73064084,
	type = 54395952.1588783,
	filter = 'filter'
)

pprint(vars(results))

```

### **get_common_library_items**
Get Common Library Items
- HTTP Method: GET
- Endpoint: /library/sections/{sectionId}/common

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| section_id | float | Required | the Id of the library to query |
| type | float | Required | item type |
| filter | str | Optional | the filter parameter |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_common_library_items(
	section_id = -96350957.04933052,
	type = -59684397.0411133,
	filter = 'filter'
)

pprint(vars(results))

```

### **get_metadata**
Get Items Metadata
- HTTP Method: GET
- Endpoint: /library/metadata/{ratingKey}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| rating_key | float | Required | the id of the library item to return the children of. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_metadata(rating_key = -75419040.74332453)

pprint(vars(results))

```

### **get_metadata_children**
Get Items Children
- HTTP Method: GET
- Endpoint: /library/metadata/{ratingKey}/children

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| rating_key | float | Required | the id of the library item to return the children of. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_metadata_children(rating_key = -1105110.1166751534)

pprint(vars(results))

```

### **get_on_deck**
Get On Deck
- HTTP Method: GET
- Endpoint: /library/onDeck

**Parameters**

This method has no parameters.

**Return Type**

[GetOnDeckResponse](/src/plexsdk/models/README.md#getondeckresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.library.get_on_deck()

pprint(vars(results))

```


### **log_multi_line**
Logging a multi-line message
- HTTP Method: POST
- Endpoint: /log

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.log.log_multi_line()

pprint(vars(results))

```

### **log_line**
Logging a single line message.
- HTTP Method: GET
- Endpoint: /log

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| level | [Level](/src/plexsdk/models/README.md#level) | Required | An integer log level to write to the PMS log with.  <br>0: Error  <br>1: Warning  <br>2: Info <br>3: Debug  <br>4: Verbose<br> |
| message | str | Required | The text of the message to write to the log. |
| source | str | Required | a string indicating the source of the message. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.log.log_line(
	level = 2,
	message = 'message',
	source = 'source'
)

pprint(vars(results))

```

### **enable_paper_trail**
Enabling Papertrail
- HTTP Method: GET
- Endpoint: /log/networked

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.log.enable_paper_trail()

pprint(vars(results))

```


### **create_playlist**
Create a Playlist
- HTTP Method: POST
- Endpoint: /playlists

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| title | str | Required | name of the playlist |
| type | [Type](/src/plexsdk/models/README.md#type) | Required | type of playlist to create |
| smart | [Smart](/src/plexsdk/models/README.md#smart) | Required | whether the playlist is smart or not |
| uri | str | Optional | the content URI for the playlist |
| play_queue_id | float | Optional | the play queue to copy to a playlist |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.create_playlist(
	title = 'title',
	type = 'photo',
	smart = 1,
	uri = 'uri',
	play_queue_id = 24795931.71901846
)

pprint(vars(results))

```

### **get_playlists**
Get All Playlists
- HTTP Method: GET
- Endpoint: /playlists/all

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| playlist_type | [PlaylistType](/src/plexsdk/models/README.md#playlisttype) | Optional | limit to a type of playlist. |
| smart | [Smart](/src/plexsdk/models/README.md#smart) | Optional | type of playlists to return (default is all). |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.get_playlists(
	playlist_type = 'video',
	smart = 1
)

pprint(vars(results))

```

### **get_playlist**
Retrieve Playlist
- HTTP Method: GET
- Endpoint: /playlists/{playlistID}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| playlist_id | float | Required | the ID of the playlist |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.get_playlist(playlist_id = 92652013.47806525)

pprint(vars(results))

```

### **delete_playlist**
Deletes a Playlist
- HTTP Method: DELETE
- Endpoint: /playlists/{playlistID}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| playlist_id | float | Required | the ID of the playlist |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.delete_playlist(playlist_id = 15166092.952776998)

pprint(vars(results))

```

### **update_playlist**
Update a Playlist
- HTTP Method: PUT
- Endpoint: /playlists/{playlistID}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| playlist_id | float | Required | the ID of the playlist |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.update_playlist(playlist_id = -13354153.8729752)

pprint(vars(results))

```

### **get_playlist_contents**
Retrieve Playlist Contents
- HTTP Method: GET
- Endpoint: /playlists/{playlistID}/items

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| playlist_id | float | Required | the ID of the playlist |
| type | float | Required | the metadata type of the item to return |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.get_playlist_contents(
	playlist_id = 72191503.82096133,
	type = -50585783.98957678
)

pprint(vars(results))

```

### **clear_playlist_contents**
Delete Playlist Contents
- HTTP Method: DELETE
- Endpoint: /playlists/{playlistID}/items

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| playlist_id | float | Required | the ID of the playlist |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.clear_playlist_contents(playlist_id = 8693313.65152806)

pprint(vars(results))

```

### **add_playlist_contents**
Adding to a Playlist
- HTTP Method: PUT
- Endpoint: /playlists/{playlistID}/items

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| playlist_id | float | Required | the ID of the playlist |
| uri | str | Required | the content URI for the playlist |
| play_queue_id | float | Required | the play queue to add to a playlist |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.add_playlist_contents(
	playlist_id = 41362150.74332705,
	uri = 'library://..',
	play_queue_id = 123
)

pprint(vars(results))

```

### **upload_playlist**
Upload Playlist
- HTTP Method: POST
- Endpoint: /playlists/upload

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| path | str | Required | absolute path to a directory on the server where m3u files are stored, or the absolute path to a playlist file on the server. <br>If the `path` argument is a directory, that path will be scanned for playlist files to be processed. <br>Each file in that directory creates a separate playlist, with a name based on the filename of the file that created it. <br>The GUID of each playlist is based on the filename. <br>If the `path` argument is a file, that file will be used to create a new playlist, with the name based on the filename of the file that created it. <br>The GUID of each playlist is based on the filename.<br> |
| force | [Force](/src/plexsdk/models/README.md#force) | Required | force overwriting of duplicate playlists. By default, a playlist file uploaded with the same path will overwrite the existing playlist. <br>The `force` argument is used to disable overwriting. If the `force` argument is set to 0, a new playlist will be created suffixed with the date and time that the duplicate was uploaded.<br> |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.playlists.upload_playlist(
	path = '/home/barkley/playlist.m3u',
	force = 1
)

pprint(vars(results))

```


### **get_transient_token**
Get a Transient Token.
- HTTP Method: GET
- Endpoint: /security/token

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| type | [SecurityType](/src/plexsdk/models/README.md#securitytype) | Required | `delegation` - This is the only supported `type` parameter. |
| scope | [Scope](/src/plexsdk/models/README.md#scope) | Required | `all` - This is the only supported `scope` parameter. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.security.get_transient_token(
	type = 'delegation',
	scope = 'all'
)

pprint(vars(results))

```

### **get_source_connection_information**
Get Source Connection Information
- HTTP Method: GET
- Endpoint: /security/resources

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| source | str | Required | The source identifier with an included prefix. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.security.get_source_connection_information(source = 'provider://provider-identifier')

pprint(vars(results))

```


### **get_sessions**
Get Active Sessions
- HTTP Method: GET
- Endpoint: /status/sessions

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.sessions.get_sessions()

pprint(vars(results))

```

### **get_session_history**
Get Session History
- HTTP Method: GET
- Endpoint: /status/sessions/history/all

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.sessions.get_session_history()

pprint(vars(results))

```

### **get_transcode_sessions**
Get Transcode Sessions
- HTTP Method: GET
- Endpoint: /transcode/sessions

**Parameters**

This method has no parameters.

**Return Type**

[GetTranscodeSessionsResponse](/src/plexsdk/models/README.md#gettranscodesessionsresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.sessions.get_transcode_sessions()

pprint(vars(results))

```

### **stop_transcode_session**
Stop a Transcode Session
- HTTP Method: DELETE
- Endpoint: /transcode/sessions/{sessionKey}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| session_key | str | Required | the Key of the transcode session to stop |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.sessions.stop_transcode_session(session_key = 'zz7llzqlx8w9vnrsbnwhbmep')

pprint(vars(results))

```


### **get_update_status**
Querying status of updates
- HTTP Method: GET
- Endpoint: /updater/status

**Parameters**

This method has no parameters.

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.updater.get_update_status()

pprint(vars(results))

```

### **check_for_updates**
Checking for updates
- HTTP Method: PUT
- Endpoint: /updater/check

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| download | [Download](/src/plexsdk/models/README.md#download) | Optional | Indicate that you want to start download any updates found. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.updater.check_for_updates(download = 'foo')

pprint(vars(results))

```

### **apply_updates**
Apply Updates
- HTTP Method: PUT
- Endpoint: /updater/apply

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| tonight | [Tonight](/src/plexsdk/models/README.md#tonight) | Optional | Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install |
| skip | [Skip](/src/plexsdk/models/README.md#skip) | Optional | Indicate that the latest version should be marked as skipped. The <Release> entry for this version will have the `state` set to `skipped`. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.updater.apply_updates(
	tonight = 1,
	skip = 1
)

pprint(vars(results))

```


### **start_universal_transcode**
Start Universal Transcode
- HTTP Method: GET
- Endpoint: /video/:/transcode/universal/start.mpd

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| has_mde | float | Required | Whether the media item has MDE |
| path | str | Required | The path to the media item to transcode |
| media_index | float | Required | The index of the media item to transcode |
| part_index | float | Required | The index of the part to transcode |
| protocol | str | Required | The protocol to use for the transcode session |
| fast_seek | float | Optional | Whether to use fast seek or not |
| direct_play | float | Optional | Whether to use direct play or not |
| direct_stream | float | Optional | Whether to use direct stream or not |
| subtitle_size | float | Optional | The size of the subtitles |
| subtites | str | Optional | The subtitles |
| audio_boost | float | Optional | The audio boost |
| location | str | Optional | The location of the transcode session |
| media_buffer_size | float | Optional | The size of the media buffer |
| session | str | Optional | The session ID |
| add_debug_overlay | float | Optional | Whether to add a debug overlay or not |
| auto_adjust_quality | float | Optional | Whether to auto adjust quality or not |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.video.start_universal_transcode(
	has_mde = -81137488.49360377,
	path = 'path',
	media_index = -77210832.41519478,
	part_index = -72229071.84453362,
	protocol = 'protocol',
	fast_seek = -34663937.278298415,
	direct_play = -65649475.52201366,
	direct_stream = -45808524.16842922,
	subtitle_size = -22927306.960050985,
	subtites = 'subtites',
	audio_boost = -27400291.423254773,
	location = 'location',
	media_buffer_size = 23155108.458466023,
	session = 'session',
	add_debug_overlay = 84869389.04259121,
	auto_adjust_quality = 36723992.04259604
)

pprint(vars(results))

```

### **get_timeline**
Get the timeline for a media item
- HTTP Method: GET
- Endpoint: /:/timeline

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| rating_key | float | Required | The rating key of the media item |
| key | str | Required | The key of the media item to get the timeline for |
| state | [State](/src/plexsdk/models/README.md#state) | Required | The state of the media item |
| has_mde | float | Required | Whether the media item has MDE |
| time | float | Required | The time of the media item |
| duration | float | Required | The duration of the media item |
| context | str | Required | The context of the media item |
| play_queue_item_id | float | Required | The play queue item ID of the media item |
| play_back_time | float | Required | The playback time of the media item |
| row | float | Required | The row of the media item |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from plexsdk import PlexSDK
sdk = PlexSDK()
sdk.set_api_key(getenv("PLEXSDK_API_KEY"))
results = sdk.video.get_timeline(
	rating_key = -59189022.367571995,
	key = 'key',
	state = 'paused',
	has_mde = 84394939.21690026,
	time = 76537742.6976276,
	duration = -90087270.61978817,
	context = 'context',
	play_queue_item_id = -71830087.03538291,
	play_back_time = 61930081.99176124,
	row = 23118864.63882491
)

pprint(vars(results))

```




