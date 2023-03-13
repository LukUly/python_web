from requests import get

print(get('http://localhost:8080/api/jobs').json())
print(get('http://localhost:8080/api/jobs/3').json())
print(get('http://localhost:8080/api/jobs/500').json())
print(get('http://localhost:8080/api/jobs/qwerty').json())
