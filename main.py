import requests


print(requests.__version__)
google = requests.get('http://google.com/')
print(google.text)
python_script = requests.get('https://raw.githubusercontent.com/zqq66/404_lab1/main/main.py')
print(python_script.text)
