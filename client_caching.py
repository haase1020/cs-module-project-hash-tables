# let's make a web client
# it will fetch URLs
# but it will cache the web page that's returned

# PLAN
# how to use hash tables to make a web cache?
# key: url
# value: webpage data

# could make the value store more info
# webpage data
# when we looked it up

import urllib.request
# EXECUTE
cache = {}

url = 'https://www.google.com'
# given a url, check it see if its in the cache
if url in cache:
    webpage = cache[url]
# if so, return that


# if not, go get it
else:
    print('going out into the webs to get the page')
    resp = urllib.request.urlopen(url)
    data = resp.read()
    resp.close()
    # put in cache
    cache[url] = data
print(cache[url])
