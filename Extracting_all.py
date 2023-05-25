import re
import requests
import os

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

def extract_phones(text):
    phone_pattern = r'(?:(?:\+\d{1,2}\s*)(?:\(?\d{3}\)?[\s.-]*)?\d{3}[\s.-]?\d{4})'
    phones = re.findall(phone_pattern, text)
    return phones

def extract_links(text):
    link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    links = re.findall(link_pattern, text)
    return links

def get_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Example usage
url = input("Enter the website URL: ")

content = get_website_content(url)
if content is not None:
    emails = extract_emails(content)
    phones = extract_phones(content)
    links = extract_links(content)

    # Create a directory to save the files
    folder_name = input("Enter the folder name: ")
    os.makedirs(folder_name, exist_ok=True)

    # Save emails to a file
    email_filename = os.path.join(folder_name, "emails.txt")
    with open(email_filename, 'w') as email_file:
        for email in emails:
            email_file.write(email + '\n')

    # Save phone numbers to a file
    phone_filename = os.path.join(folder_name, "phones.txt")
    with open(phone_filename, 'w') as phone_file:
        for phone in phones:
          phone_file.write(' '.join(phone) + '\n')


    # Save links to a file
    link_filename = os.path.join(folder_name, "links.txt")
    with open(link_filename, 'w') as link_file:
        for link in links:
            link_file.write(link + '\n')

    print(f"Content saved in the folder '{folder_name}'.")

else:
    print(f"Failed to retrieve content from {url}.")