#1. 
it registers a URL path with a function telling flask what function to call when someone visits that URL.

#2.
flask checks this URL against a table of all registered routes and calls the matching function. 

#3. 
route parameters are a part of the URL path itself. example /greet/Sarah right. 
query parameters are optional key value pairs added after a ?. example to calculate, '/calculate?num1=10'

#4. 
since they are in different places.
query parameters are in the URL so flask puts them in 'request.args'.
POST data is in the request body so use 'request.get_json()' to parse it. 

#5. 
will throw a runtimeerror because 'request' only exists while flask is actively handling a request.  