from apiclient.discovery import build 

def get_media_url(player_name, google_api, search_engine_id):
    resource = build("customsearch", "v1", developerKey= google_api).cse()
    query = str(player_name) + " " + "football"
    result = resource.list(q=query, cx = search_engine_id, searchType='image', imgSize='medium', num = 1)
    url =  result['items'][0]['link']

    return  url