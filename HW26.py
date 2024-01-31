import os
import requests
import json
p = 'HW26_json'
os.makedirs(p, exist_ok=True)
r = requests.get('https://jsonplaceholder.typicode.com/posts')
if r.status_code == 200:
    for i, j in enumerate(r.json()):
        fname = os.path.join(p, f'json{i + 1}.json')
        with open(fname, 'w', encoding='utf-8') as file:
            json.dump(j, file, ensure_ascii=False, indent=2)
        print(f'{fname} сохранен')
else:
    print(f'Ошибка. Код статуса: {r.status_code}')