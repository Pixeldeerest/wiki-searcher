# Wiki-searcher
This mini web application was created with the intention to search for a wikipedia page based on information in the subdomain of the url that the app is routing to.
The application would parse the subdomain from the url, and use that variable to search wikipedia. Once a page has been identified, a url would be extracted based on the page information.
If the page result returned ambiguous results, the expection results (ie: options) would be used as a variable to get a page matching the result - and thus, it's URL.
If another DisambiguationError was thrown, then that result would be skipped and the program would continue.
