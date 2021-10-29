import wikipedia
import json 
from urllib.parse import urlparse 
from flask import Flask, url_for, request
from wikipedia.wikipedia import WikipediaPage

app = Flask(__name__) 

if __name__ == "main":
    app.config['SERVER_NAME'] = 'wiki-search.com'
    app.run()

@app.route("/", methods=['GET'])
def wikisearch_index():
    url = urlparse(request.url)
    searchTerm = url.hostname.split('.')[0]

    wikiResults = {"links":[]}
    try:
        wikiPage = wikipedia.page(searchTerm)
        wikiURL = wikiPage.url
        wikiResults["links"].append(wikiURL)
    except wikipedia.exceptions.DisambiguationError as e:
        for option in e.options:
            try:
                wikiPage = wikipedia.page(option)
                wikiURL = wikiPage.url
            except wikipedia.exceptions.DisambiguationError as e:
                continue
            wikiResults["links"].append(wikiURL)
    result = json.dumps(wikiResults)
    return result

