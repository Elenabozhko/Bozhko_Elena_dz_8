
import re
import requests

PAD = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                 r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                 r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nqinx_logs/nqinx_logs'
content = requests.get(url).text
for arg in PAD.findall(content):
    addr, datetime, r_type, resource, code, size = arg
    print(addr, datetime, r_type, resource, code, size)