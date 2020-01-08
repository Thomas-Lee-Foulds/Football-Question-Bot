from google_images_download import google_images_download 
import sys


def get_media_url(player_name):
    orig_stdout = sys.stdout
    f = open('URLS.txt', 'w')
    sys.stdout = f
    response = google_images_download.googleimagesdownload()  
    query = str(player_name) + " " + "football"
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":1, 
                 "print_urls":True, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic"} 
    paths = response.download(arguments)
    sys.stdout = orig_stdout
    

    with open('URLS.txt') as f:
        content = f.readlines()
    f.close()

    urls = []
    for j in range(len(content)):
        if content[j][:9] == 'Completed':
            urls.append(content[j-1][11:-1]) 
    return urls[0]