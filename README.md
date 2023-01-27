# requests-vs-urllib3
two implementation of same requests in requests and urllib

| request -------------------------              ------------------ ----|urllib3 -----------------------------------------------------|
|---------|-------|
|   r= requests.post('http:             | http = urllib3.PoolManager() ;  http.request('POST'         |
| files={'file': file}                                 |    with open(file_path, 'rb') as file: file_data = file.read()  ; fields={'file': ('a.mp3', file_data)}              |
| r.status_code, r.text, r.json()  |  r.status, r.data, json.loads(r.data) |
|  params={'sentences': sentences} | fields=[('sentences', x) for x in sentences if x] |
| r.encoding = 'UTF-8' ; json.dumps(r.json(), indent=4, ensure_ascii=False) | json.dumps(json.loads(p.data), indent=4, ensure_ascii=False) | 

