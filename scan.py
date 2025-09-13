import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
#Function to get all forms from a given URL
def get_all_forms(url):
    """Given a URL, it returns all forms from the HTML content"""
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")

def form_details(form):
    """This function extracts all possible useful information about an HTML form"""
    detailsofForm = {}
    # get the form action (target url)
    action = form.attrs.get("action", "")
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get")
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    detailsofForm["action"] = action
    detailsofForm["method"] = method
    detailsofForm["inputs"] = inputs
    return detailsofForm

def vulnerable(response):
    """A simple way to check for SQL injection vulnerability"""
    errors = {
        "you have an error in your sql syntax;",
        "warning: mysql",
        "unclosed quotation mark after the character string",
        "quoted string not properly terminated",
    }
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

def scan_sql_injection(url):
    """Given a URL, it scans all forms and submits them with a SQL injection payload"""
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_info = form_details(form)
        for input in form_info["inputs"]:
            if input["type"] == "hidden" or input["value"]:
                continue
            input["value"] = "'"
        form_data = {input["name"]: input["value"] for input in form_info["inputs"] if input["name"]}
        target_url = urljoin(url, form_info["action"])
        if form_info["method"].lower() == "post":
            response = s.post(target_url, data=form_data)
        else:
            response = s.get(target_url, params=form_data)
        if vulnerable(response):
            print(f"[!] SQL Injection vulnerability detected on {target_url}")
            print(f"[*] Form details: {form_info}")
        else:
            print(f"[-] No SQL Injection vulnerability detected on {target_url}")
            break

if __name__ == "__main__":
    url = "https://www.google.com/"
    scan_sql_injection(url)
