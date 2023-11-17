import requests, os, shutil
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("./"))
template = env.get_template("template.jinja")

#MarkDown 문법 추가
def addMarkdown(p_list, type):
    _content = ''''''
    if(type == "D"):
        for content in p_list:
            #print(f"{content.get_text(strip=True)}\n")
            _content += f"{content.get_text(strip=True)}<br>\n"
        return _content
    elif(type == "IO"):
        for content in p_list:
            #print(f"{content.get_text(strip=True)}\n")
            _content += f"- {content.get_text(strip=True)}\n"
        return _content

def create_files(number, rendered_contents):
    problems = os.mkdir(f"{number}")
    readme_file_path = os.path.join(number, "README.md")
    cplus_file_path = os.path.join(number, "main.cpp")
    python_file_path = os.path.join(number, "main.py")
    
    shutil.copy("main.cpp", cplus_file_path)
    shutil.copy("main.py", python_file_path)
    
    with open(readme_file_path, "w", encoding="utf-8") as readme_file:
        readme_file.write(rendered_contents)
    
    
    print("Creating Template is Done.")

#문제 번호 입력 후 요청
print("Problem Number >> ", end="")
number = input()
url = f"https://www.acmicpc.net/problem/{number}"
headers = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

#문제 존재 여부 확인 후 파싱
# print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Content 추출
    title = soup.find(id="problem_title").get_text(strip=True)
    description = soup.find(id="problem_description") #.get_text(strip=True)
    description = description.find_all('p') if description else []
    description = addMarkdown(description, "D")
    
    input = soup.find(id="problem_input") #.get_text(strip=True)
    input = input.find_all('p') if input else []
    input = addMarkdown(input, "IO")
    
    output = soup.find(id="problem_output") #.get_text(strip=True)
    output= output.find_all('p') if output else []
    output = addMarkdown(output, "IO")
    
    README = template.render(title = title, url = url, description = description, input = input, output = output)
    
    create_files(number, README)
    
else:
    print("Problem isn't exist.")
    
