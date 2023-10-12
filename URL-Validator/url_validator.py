from urllib.parse import urlparse
import requests

def url_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme and result.netloc])
    except:
        return False
    
def url_functional(url):
    try:
        response = requests.head(url)
        if response.status_code < 400:
            return True
        
    except:
        return False


if __name__ == "__main__":
    url = input("Please enter the URL to verify: ")
    if url_validator(url):
        print("URL Format is Valid")
        if url_functional(url):
            print("URL is Functional")
        else:
            print("URL is not functional")
    else:
        print("URL format is Invalid")
        