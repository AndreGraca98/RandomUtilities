import os
import requests
from bs4 import  BeautifulSoup
from pathlib import Path
from datetime import datetime
from tqdm import tqdm

# Anaconda versions archive
url = 'https://repo.anaconda.com/archive/'
response = requests.get(url)

# Parse url response
parsed_response = BeautifulSoup(response.content, 'html.parser')

# Get all conda versions up to date
available_versions = [ s.get('href') for s in parsed_response.find_all('a')]


def filter_by_word(list_, word):
    return [x for x in list_ if str(word).lower() in str(x).lower()]


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


# Mannualy choose what filters you want to choose the conda version
linux_versions = filter_by_word(available_versions, 'sh')
linux_versions = filter_by_word(linux_versions, 'linux')
linux_versions = filter_by_word(linux_versions, 'Anaconda3') # For python3
linux_versions = filter_by_word(linux_versions, 'x86_64')


year = int(datetime.today().year)
month = 12

# CHoose the latest version
while 1:
    linux_versions_py3_year = filter_by_word(linux_versions, str(year))
    if linux_versions_py3_year:
        break
    year -= 1

    if year < 2019:
        raise ValueError(f'Something went wrong. Check what versions are available as of today in {url}')

while 1:
    linux_versions_py3_year_month = filter_by_word(linux_versions_py3_year, str(month))
    if linux_versions_py3_year_month:
        break
    month -= 1
    
    if month < 1:
        raise ValueError(f'Something went wrong. Check what versions are available as of today in {url}')


final_conda_version = sorted(linux_versions_py3_year_month)[-1]
final_url = url + final_conda_version

print('Anaconda version:', final_conda_version)


# User input
while 1:
    inp = str(input('Download? [Y]/n : '))
    if inp in ('Y', 'y', 'n', ''):
        inp = True if inp in ('Y', 'y', '') else False
        break


# Download file
if is_downloadable(final_url) and inp:
    filesize = int(requests.head(final_url).headers["Content-Length"])
    with requests.get(final_url, stream=True, allow_redirects=True) as r, \
         open(os.path.join(Path.home(), final_conda_version), "wb") as f, \
         tqdm(unit="B", unit_scale=True, unit_divisor=1024, total=filesize, desc=final_url) as progress:
         
         for chunk in r.iter_content(chunk_size=1024):
            datasize = f.write(chunk)
            progress.update(datasize)
