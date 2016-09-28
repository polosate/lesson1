import requests   
import urllib   
import json as m_json     

link = "https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=10\
&hl=en&prettyPrint=false&source=gcsc&gss=.ru&sig=aaf08f6785d79163717330afd4116c8f\
&cx=014978777049465661165:o-yqacq6xg4&sort=&googlehost=www.google.com\
&nocache=1475091919307"                                                                                                                                                                                         

def googlesearch(query):    
    payload = {'q': query}   
                                                                                                                                                                                    
    r = requests.get(link, params=payload) 

    json = m_json.loads ( r.text )
    # print(json)
    try:
    	title = json ['results'][0]['titleNoFormatting']
    	url = json ['results'][0]['unescapedUrl']
    	return (title + '; ' + url)
    except IndexError:
    	return "Даже гугл этого не знает!"
    
    
if __name__ == "__main__":
	query = input("Что хотели? >> ")
	print(googlesearch(query))