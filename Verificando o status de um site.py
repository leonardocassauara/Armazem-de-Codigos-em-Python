import urllib
import urllib.request

try:
    url = 'http://www.op.gg'
    site = urllib.request.urlopen(url)
except urllib.error.URLError:
    print('\033[0:31mO site não está acessível no momento.\033[m')
else:
    print('\033[0:32mConsegui acessar o site.\033[m')