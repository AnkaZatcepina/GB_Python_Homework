import argparse

DEFAULT_URLS = ['https://happypik.ru/wp-content/uploads/2019/09/njashnye-kotiki8.jpg',
                'https://w.forfun.com/fetch/70/7047b702475924ba8f8044b5b5ca56ba.jpeg',
                'https://scientificrussia.ru/images/b/teb-full.jpg',
                ]       

def url_to_filename(url:str)->str:
    return url.split("/")[-1]  

def parse()->[str]:
    urls = []     
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', nargs='+', help='Ссылки на картинки через пробел')
    args = parser.parse_args()
    if args.urls:
        urls = args.urls
    else:
        urls = DEFAULT_URLS.copy()
    print(urls)    
    return urls     
            
