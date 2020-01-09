from apiclient.discovery import build 

def get_media_url(player_name, google_api, search_engine_id):
    resource = build("customsearch", "v1", developerKey= google_api).cse()
    query = str(player_name) + " " + "football"
    result = resource.list(q=query, cx = search_engine_id, searchType='image', imgSize='medium', num = 1)
    result_search = result.json()
    print(result_search)
    for item in result_search['items']:
        url = item["link"]   
    return  url