import re

def remove_html_tags(text):  
    return re.sub('<.*?>', '', text)
