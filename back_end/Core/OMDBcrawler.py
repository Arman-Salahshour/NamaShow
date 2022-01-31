import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://www.omdbapi.com/?'
apikey = '&apikey=ac4f22e8'


def print_json(json_data):
    list_keys=['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 
               'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Ratings', 
               'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'Response']
    print("-"*50)
    for k in list_keys:
        if k in list(json_data.keys()):
            print(f"{k}: {json_data[k]}")
    print("-"*50)


def save_poster(json_data):
    import os
    title = json_data['Title'] + ' ' + json_data['Year'][:4]
    poster_url = json_data['Poster']
    # Splits the poster url by '.' and picks up the last string as file extension
    poster_file_extension=poster_url.split('.')[-1]
    # Reads the image file from web
    poster_data = urllib.request.urlopen(poster_url).read()
        
    savelocation=os.getcwd()+'/'+ 'Core' + '/' + 'Posters'+'/'
    # Creates new directory if the directory does not exist. Otherwise, just use the existing path.
    if not os.path.isdir(savelocation):
        os.mkdir(savelocation)
    
    filename=savelocation+str(title)+'.'+poster_file_extension
    f=open(filename,'wb')
    f.write(poster_data)
    f.close()
    return filename

def search_omdb(title):
    if len(title) < 1 or title=='quit': 
        print("Goodbye now...")
        return None

    search_params = title.rsplit(' ', 1)


    try:
        if len(search_params)>1 and search_params[1].isdigit():
            url = serviceurl + urllib.parse.urlencode({'t': search_params[0]}) + '&' + urllib.parse.urlencode({'y': search_params[1]}) + apikey
        else:
            url = serviceurl + urllib.parse.urlencode({'t': title})+apikey
        print(f'Retrieving the data of "{title}" now... ')
        uh = urllib.request.urlopen(url)
        data = uh.read()
        json_data=json.loads(data)
        
        if json_data['Response']=='True':
            if json_data['Poster']!='N/A':
                filename = save_poster(json_data)
                json_data['PosterLoc'] = filename
            return json_data
        else:
            print("Error encountered: ",json_data['Error'])
    
    except urllib.error.URLError as e:
        print(f"ERROR: {e.reason}")
