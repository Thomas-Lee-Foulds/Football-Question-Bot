from apiclient.discovery import build 

def get_media_url(player_name, google_api, search_engine_id):
    resource = build("customsearch", "v1", developerKey= google_api)
    query = str(player_name) + " " + "football profile"
    result = resource.cse().list(q=query, cx = search_engine_id, searchType='image', imgType='photo',imgSize='medium', fileType='jpg', safe= 'off', num = 1).execute()
    print(result)
    print("Addiction")
    for item in result['items']:
        url = item['link']   
    return  url