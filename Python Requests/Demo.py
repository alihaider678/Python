# Requests Web Pages

# import requests

# r = requests.get('https://xkcd.com/353/')

# print(r)

# print(dir(r))

# Toget the HTML of page

# print(r.text)



# Import Image from URL

# import requests

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# with open('comic.png', 'wb') as f:
# 	f.write(r.content)


# HTTP Methods

# 1) GET METHOD

# import requests

# payload = {'page' : 2, 'Count' : 25}

# r = requests.get('https://httpbin.org/get', params = payload)

# print(r.text)


# 2) POST METHOD

# import requests

# payload = {'username' : 'Ali', 'Password' : 'husne1129'}

# r = requests.post('https://httpbin.org/post', data = payload)

# print(r.text)



# 3) Read JSON

import requests


r = requests.get('https://httpbin.org/basic-auth/Ali/husne1129', auth = ('Ali', 'husne1129'))

print(r.text)