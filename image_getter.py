from apiclient.discovery import build 

def get_media_url(player_name, google_api, search_engine_id):
    resource = build("customsearch", "v1", developerKey= google_api).cse()
    query = str(player_name) + " " + "football"
    result = resource.list(q=query, cx = search_engine_id, searchType='image', imgSize='medium', num = 2).execute()
    print(result)
    for item in result:
        url = item["link"]   
    return  url