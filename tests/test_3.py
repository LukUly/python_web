from requests import get, delete

print(delete('http://localhost:8080/api/jobs/11').json())  # a proper request
print(delete('http://localhost:8080/api/jobs/500').json())  # no record with this id
print(delete('http://localhost:8080/api/jobs/qwerty').json())  # id not a number
print(get('http://localhost:8080/api/jobs').json())
