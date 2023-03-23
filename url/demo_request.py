import requests
import time
import concurrent.futures
with open('urls.txt','r') as url_list:
    img_urls = [str(line) for line in url_list.readlines()]
print(img_urls)
print(len(img_urls))
i=1
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    global i
    img_name='img'+ str(i)
    i+=1
    img_name = f'{img_name}.jpg'
    with open (img_name,'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was download.....')
t1=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    for url in img_urls:
        executor.submit(download_image,url)
t2=time.perf_counter()
print(f'Finished in {t2-t1} seconds')

