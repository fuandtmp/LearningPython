# define function which check is url correct or not
def normalize_url(entered_url):
    if entered_url.find('http://') == 0:
        # we get url with http:// title, then erase first 7 simbols and add https:// to string
        return 'https://' + entered_url[7:]
    elif entered_url.find('https://') == 0:
        # we get url with https:// title, then just return that
        return entered_url
    else:
        # we get url without title, then and add https:// to string
        return 'https://' + entered_url


# get url from user
print('Please, enter a url:', end='')

url = input('')
# print correct url
print(normalize_url(url))
