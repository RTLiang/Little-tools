import requests
from urllib.parse import urlparse
import os
from bs4 import BeautifulSoup
import json
import re

# Replace 'short_link' with your actual short link
short_link = 'http://xhslink.com/AWwtmu'
long_link = ''
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
headers = {'User-Agent': user_agent}


def get_long_link(short_link):
    # Replace 'your_user_agent' with the User-Agent you want to use
    global headers
    # Define headers with the User-Agent

    try:
        response = requests.head(
            short_link, allow_redirects=False, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 307:
            long_link = response.headers['Location']
            # print(f"Long Link: {long_link}")
            # Print response headers
            # print("Response Headers:")
            # for key, value in response.headers.items():
            # print(f"{key}: {value}")
            print("long_link:\n" + long_link)
            return long_link
        
        else:
            print(
                f"Failed to retrieve the long link. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def ignore_paras(url):
    parsed = urlparse(url)
    # print("parsered:\n"+str(parsed.scheme + "://" + parsed.netloc + parsed.path))
    return str(parsed.scheme + "://" + parsed.netloc + parsed.path)

def request_url(url):
    global headers
    print("url:\n"+url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # os.system('cls')
            # with open('test.html', 'w',encoding='utf-8') as file:
            #     file.write(response.text)
            # print(response.text)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print(
                f"Failed to retrieve the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def explore(url):
    try:
    # Replace '/discovery/item/' with '/explore/'
        modified_url = url.replace('/discovery/item/', '/explore/')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    print("Modified URL:", modified_url)
    return modified_url

def get_script(soup):
    script_tag = soup.find('script', text=lambda text: text and 'window.__INITIAL_STATE__' in text)
    # print("script\t"+str(script_tag))
    # os.system('cls')
    if script_tag:
        script_content = script_tag.string
        # You can then parse the JSON content within the script tag
        initial_state = script_content.split('=')[1].strip()
        # print(initial_state)
        initial_state = replace_undefined(initial_state)
        return initial_state
    else:
        print("Script tag not found.")
        
def get_image_list(initial_state):
    # You can then parse the JSON content within the script tag
    # os.system('cls')
    # print("initial_state:\n")
    # print(initial_state)
    data = json.loads(str(initial_state))
    image_id_list = extract_trace_ids(data)
    image_info_list = []
    # print("image_id_list:\n")
    # print(image_id_list)
    for image_info in image_id_list:
        # image_info = ignore_paras(image_info)
    
        image_url = "https://sns-img-qc.xhscdn.com/"+ image_info
        # print(image_url)
        image_info_list.append(image_url)
        # print("iiiiiiiiiiiiiiiii")
    print("image_info_list:\n")
    print(image_info_list)
    return image_info_list
    
def extract_trace_ids(data):
    trace_ids = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'traceId':
                trace_ids.append(value)
            else:
                trace_ids.extend(extract_trace_ids(value))
    elif isinstance(data, list):
        for item in data:
            trace_ids.extend(extract_trace_ids(item))
    return trace_ids   
    
def get_note_title(data):
    os.system('cls')
    print(data)
    key = "desc"
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                return v
            elif isinstance(v, (dict, list)):
                result = get_note_title(v)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                result = get_note_title(item)
                if result is not None:
                    return result
    
    # trace_ids = []
    # if isinstance(data, dict):
    #     for key, value in data.items():
    #         if key == 'traceId':
    #             trace_ids.append(value)
    #         else:
    #             trace_ids.extend(extract_trace_ids(value))
    # elif isinstance(data, list):
    #     for item in data:
    #         trace_ids.extend(extract_trace_ids(item))
    # return trace_ids[0]
    
    
    
    
# def change_url_header(url):
#     url = url.replace("sns-webpic.xhscdn.com", "ci.xiaohongshu.com")
#     return url

def save_to_file(url):
    if re.match(r'http://xhslink.com/', url):
        url = get_long_link(url)
    # Extract image URLs and other data
    image_list = get_image_list(get_script(request_url(url)))
    # note_title = get_note_title(get_script(request_url(explore(ignore_paras(get_long_link(url))))))
    # print(image_list)
    # print("note_title:\n")
    # print(note_title)
    
    for image_url in image_list:
        file_name = image_url.split("/")[-1] + ".jpg"
        sanitized_file_name = re.sub(r'[\/:*?"<>|]', '_', file_name)
        # Create the full path to save the image
        # save_directory = os.path.join(os.getcwd(), note_title)
        # os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist
        # save_path = os.path.join(str(save_directory), sanitized_file_name)
        # Send an HTTP GET request to download the image
        response = requests.get(image_url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            with open(sanitized_file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded and saved: {sanitized_file_name}")
        else:
            print(f"Failed to download: {image_url}")

def replace_undefined(json_str):
    return json_str.replace("undefined", "null")
# Example usage:
# save_to_file("https://example.com/some/url")


save_to_file(input("link:"))
# save_to_file()