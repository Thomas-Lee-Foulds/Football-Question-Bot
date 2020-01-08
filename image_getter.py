from google_images_download import google_images_download 

def get_media_url(player_name):
    response = google_images_download.googleimagesdownload()  
    query = player_name + " " + "football"
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":1, 
                 "print_urls":True, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic"} 
    path = response.download(arguments)
    return path