import requests
from bs4 import BeautifulSoup

def grab_resume_sample(url):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the resume sample on the page (modify this according to the website structure)
        resume = soup.find('div', class_='resume-sample')

        if resume:
            # Extract the text or download the resume
            resume_text = resume.get_text()
            # Or save the resume to a file
            # with open('resume_sample.docx', 'wb') as file:
            #     file.write(response.content)

            return resume_text
        else:
            print("Resume sample not found on the page.")
    else:
        print(f"Failed to retrieve the URL. Error code: {response.status_code}")

    return None

# Example usage
url = 'https://www.example.com/resume-sample'
resume_sample = grab_resume_sample(url)

if resume_sample:
    print(resume_sample)
