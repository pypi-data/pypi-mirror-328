
Pexels API Python
-------------------------

This Python API wrapper provides easy access to the Pexels API, allowing you to search and retrieve high-quality photos and videos for your projects.

Features
--------

- Search for photos and videos

- Access curated and popular content

- Retrieve specific photos and videos by ID

- Explore featured collections

- Manage your personal collections


Installation
------------

bash


`pip install pexels-apis `


Usage
-----

python

- `from pexels_apis import PexelsAPI`
- `pexels = PexelsAPI("YOUR_API_KEY")`
- `photos = pexels.search_photos({"query": "nature", "per_page": 10})  # Search for photos photos`
- `curated_photos = pexels.get_curated_photos({"per_page": 15}) # Get curated photos`
- `photo = pexels.get_photo(id=44315}) # Get photos by ID`  
- `videos = pexels.search_videos({"query": "ocean", "per_page": 5}) # Search for videos`
- `popular_videos = pexels.get_popular_videos({"per_page": 20}) # Get popular videos `
- `video = pexels.get_video(id=44315}) # Get vidoe by ID`  
- `collections = pexels.get_featured_collections({"per_page": 10}) # Get featured`
- `my_collections = pexels.get_my_collections({"per_page": 10}) # Get featured`

  

Available Methods
-----------------

Photos

------

-  `pexels.search_photos(params)`: Search for photos. Parameters in dict {} includes
	- query string | required The search query. Ocean, Tigers, Pears, etc.
	- orientation string | optional. Desired photo orientation. The current supported orientations are: landscape, portrait or square.
	- size string | optional. Minimum photo size. The current supported sizes are: large(24MP), medium(12MP) or small(4MP).
	- color string | optional. Desired photo color. Supported colors: red, orange, yellow, green, turquoise, blue, violet, pink, brown, black, gray, white or any hexidecimal color code (eg. #ffffff).
	- locale string | optional. The locale of the search you are performing. The current supported locales are: 'en-US' 'pt-BR' 'es-ES' 'ca-ES' 'de-DE' 'it-IT' 'fr-FR' 'sv-SE' 'id-ID' 'pl-PL' 'ja-JP' 'zh-TW' 'zh-CN' 'ko-KR' 'th-TH' 'nl-NL' 'hu-HU' 'vi-VN' 'cs-CZ' 'da-DK' 'fi-FI' 'uk-UA' 'el-GR' 'ro-RO' 'nb-NO' 'sk-SK' 'tr-TR' 'ru-RU'.
	- page integer | optional. The page number you are requesting. Default: 1
	- per_page integer | optional. The number of results you are requesting per page. Default: 15 Max: 80

Response:  {"status_code": 200|401|412|500, "status": "success", "data": {'x':'y'}} or {"status_code": 200|401|412|500,"status": "error", "error": "error message"}

-  `pexels.curated_photos(params)`: Get curated photos. Parameters in dict {} includes
	- page integer | optional. The page number you are requesting. Default: 1
	- per_page integer | optional. The number of results you are requesting per page. Default: 15 Max: 80

-  `pexels.get_photos(id)`: Retrieve a specific photo by ID. Parameters as id
	- id integer | required

Videos

------

-  `pexels.search_videos(params)`: Search for videos. Parameters in dict {} includes
	- query string | required The search query. Ocean, Tigers, Pears, etc.
	- orientation string | optional. Desired photo orientation. The current supported orientations are: landscape, portrait or square.
	- size string | optional. Minimum photo size. The current supported sizes are: large(24MP), medium(12MP) or small(4MP).
	- locale string | optional. The locale of the search you are performing. The current supported locales are: 'en-US' 'pt-BR' 'es-ES' 'ca-ES' 'de-DE' 'it-IT' 'fr-FR' 'sv-SE' 'id-ID' 'pl-PL' 'ja-JP' 'zh-TW' 'zh-CN' 'ko-KR' 'th-TH' 'nl-NL' 'hu-HU' 'vi-VN' 'cs-CZ' 'da-DK' 'fi-FI' 'uk-UA' 'el-GR' 'ro-RO' 'nb-NO' 'sk-SK' 'tr-TR' 'ru-RU'.
	- page integer | optional. The page number you are requesting. Default: 1
	- per_page integer | optional. The number of results you are requesting per page. Default: 15 Max: 80

-  `pexels.get_popular_videos(params)`: Get popular videos
	- min_width integer | optional. The minimum width in pixels of the returned videos.
	- min_height integer | optional. The minimum height in pixels of the returned videos.
	- min_duration integer | optional. The minimum duration in seconds of the returned videos.
	- max_duration integer | optional. The maximum duration in seconds of the returned videos.
	- page integer | optional. The page number you are requesting. Default: 1
	- per_page integer | optional. The number of results you are requesting per page. Default: 15 Max: 80

-  `pexels.get_video(id)`: Retrieve a specific video by ID
	- id integer | required
  

Collections

-----------

-  `pexels.get_featured_collections(params)`: Get featured collections
	-  page integer | optional. The page number you are requesting. Default: 1
	- per_page integer | optional. The number of results you are requesting per page. Default: 15 Max: 80

-  `pexels.get_my_collections(params)`: Get your personal collections
	- page integer | optional. The page number you are requesting. Default: 1
	- per_page integer | optional. The number of results you are requesting per page. Default: 15 Max: 80
	
-  `pexels.get_collection_media(params)`: Get media from a specific collection
	- type string | optional. The type of media you are requesting. If not given or if given with an invalid value, all media will be returned. Supported values are photos and videos.
	- sort string | optional. The order of items in the media collection. Supported values are: asc, desc. Default: asc
	- page integer | optional. The page number you are requesting. Default: 1
	- per_page integer | optional. The number of results you are requesting per page. Default: 15 Max: 80
  

Parameters
----------
Most methods accept a dictionary of parameters. Common parameters include:

-  `query`: Search query (required for search methods)
-  `page`: Page number (default: 1)
-  `per_page`: Results per page (default: 15, max: 80)
-  `orientation`: Photo/video orientation (landscape, portrait, square)
-  `size`: Minimum size (large, medium, small)
-  `locale`: Search locale (e.g., 'en-US', 'fr-FR')
-  `color`:  Desired photo color. Supported colors: red, orange, yellow, green, turquoise, blue, violet, pink, brown, black, gray, white or any hexidecimal color code (eg. #ffffff).

  

Response
--------

The API returns JSON responses containing relevant data such as:

- Arrays of Photo or Video objects
- Pagination information
- Total results
- Next/previous page URLs
  

Error Handling
--------------
The API wrapper includes basic error handling for invalid parameters and API responses. Always check the returned data for any error messages or unexpected results.

Guidelines
----------
Please adhere to the [Pexels API Guidelines](https://www.pexels.com/api/documentation/#guidelines) when using this wrapper and the content provided by Pexels.

Links
----------
[PYPI](https://pypi.org/project/pexels-apis)
[Github](https://github.com/mymi14s/pexels_apis)