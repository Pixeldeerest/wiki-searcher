import wikipedia
import json 
from urllib.parse import urlparse 
from flask import Flask, url_for, request
from wikipedia.wikipedia import WikipediaPage

#create an instance of Flask
app = Flask(__name__) 


if __name__ == "main":
    #app.config['SERVER_NAME'] = 'wiki-search.com'
    app.run()

#route to the main page
@app.route("/", methods=['GET'])
def wikisearch_index():
    #parse the url for the subdomain, extract it and use it as a variable
    url = urlparse(request.url)
    searchTerm = url.hostname.split('.')[0]

    #create an empty dictionary of lists to store the links
    wikiResults = {"links":[]}

    #try/catch used to identify if a search term results in ambiguous results (ie: more than one)
    try:
        #use the extracted subdomain to search for a page, get the url for the page, and add that link to the dictionary list
        wikiPage = wikipedia.page(searchTerm)
        wikiURL = wikiPage.url
        wikiResults["links"].append(wikiURL)
    #catch if an DisambiuationError exception occurs
    except wikipedia.exceptions.DisambiguationError as e:
        #loop through each option in the wiki search results
        for option in e.options:
            try:
                wikiPage = wikipedia.page(option)
                wikiURL = wikiPage.url
            #if another exception is thrown when trying to create the dictionary list, continue instead
            except wikipedia.exceptions.DisambiguationError as e:
                continue
            #add final result to dictionary list
            wikiResults["links"].append(wikiURL)
    #formate the dictionary into a json object format
    result = json.dumps(wikiResults)
    #return the object
    return result

