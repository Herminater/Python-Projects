import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

previous_jobs = [{'Rådgiver - Informasjonssikkerhet og personvern ': 'https://arbeidsplassen.nav.no/stillinger/stilling/b3f35239-1e93-4557-9646-5d9f6475ee42'}, {'Regnskapskonsulent': 'https://arbeidsplassen.nav.nohttps://www.finn.no/300615305'}, {'Vil du jobbe med veldedighet over telefon?': 'https://arbeidsplassen.nav.no/stillinger/stilling/17f434eb-68ef-4fc1-8c52-1395e280e13f'}, {'Prosjektplanlegger': 'https://arbeidsplassen.nav.no/stillinger/stilling/e47d0d6e-ad09-41d6-b03c-7bebaacf5ec6'}, {'Helsefagarbeider ønskes til Nes sykehjem ': 'https://arbeidsplassen.nav.no/stillinger/stilling/2159bd53-a7df-43ab-a54a-55e838b63360'}, {'Sekretær/lederstøtte': 'https://arbeidsplassen.nav.no/stillinger/stilling/95b19efa-00eb-409a-8329-7f7726cc44c9'}, {'Butikksjef': 'https://arbeidsplassen.nav.nohttps://www.finn.no/330617487'}, {'Salgssjef': 'https://arbeidsplassen.nav.nohttps://www.finn.no/330388338'}, {'Kundeveileder': 'https://arbeidsplassen.nav.no/stillinger/stilling/320bb95c-14fe-44d3-9ae6-d28ef280712b'}, {'Selgerleder Ski & Sykkel avd. Tønsberg': 'https://arbeidsplassen.nav.no/stillinger/stilling/a4cb57c4-6896-4955-85a4-fff73c6e0c53'}, {'Kundemottaker': 'https://arbeidsplassen.nav.no/stillinger/stilling/62d25a9e-442d-492b-9112-f8e578a014e7'}, {'Sykepleier ': 'https://arbeidsplassen.nav.no/stillinger/stilling/5b7d4be6-52f2-4c53-8e33-1d7a1c0f8390'}, {'Fysioterapeut': 'https://arbeidsplassen.nav.no/stillinger/stilling/258d59e2-e60c-4012-9f3d-b0295a88528f'}, {'Elektriker gr. L.': 'https://arbeidsplassen.nav.no/stillinger/stilling/eb4738f5-f209-4b98-bc63-4e8193a2ca4c'}, {'Greveskogen vgs, vikariat og timevikarer': 'https://arbeidsplassen.nav.no/stillinger/stilling/a66e4dcb-cd8d-4a6c-ac56-841aaa2ca2ae'}, {'Rådgiver/ spesialkonsulent økonomi': 'https://arbeidsplassen.nav.no/stillinger/stilling/7c95959a-21a8-4c89-8ebc-5639096330db'}, {'Sykepleier': 'https://arbeidsplassen.nav.no/stillinger/stilling/02e48c61-0260-41b9-ba0f-e491ec1b7ea5'}, {'Idrettspedagog/fysioterapeut': 'https://arbeidsplassen.nav.no/stillinger/stilling/f26d7e72-4abd-4a05-8cd8-214704c25c2a'}, {'Sykepleierstudent': 'https://arbeidsplassen.nav.no/stillinger/stilling/4984355f-4046-47dc-9f76-3885fb253bd8'}, {'Butikkmedarbeider': 'https://arbeidsplassen.nav.no/stillinger/stilling/ea4b62f2-86f0-4ed0-b418-c652e4939cee'}, {'Fagarbeider forsterket enhet': 'https://arbeidsplassen.nav.no/stillinger/stilling/5aa4e8e2-ed07-4bf6-8270-0161f026e09c'}, {'Helsesekretær ': 'https://arbeidsplassen.nav.no/stillinger/stilling/80ee596d-7802-48eb-b8f5-8c1adf11a242'}, {'Seniorrådgiver, metode og innhold': 'https://arbeidsplassen.nav.no/stillinger/stilling/f29f31a6-832f-4025-8215-22550d22d835'}, {'Kundekonsulent': 'https://arbeidsplassen.nav.no/stillinger/stilling/c69c7971-4e11-44bc-8d63-b92b9360c22b'}]

def get_jobs_in_content():
    driver = webdriver.Chrome(service=ChromeService(), options=Options())
    driver.get("https://arbeidsplassen.nav.no/stillinger?municipals[]=VESTFOLD%20OG%20TELEMARK.T%C3%98NSBERG&counties[]=VESTFOLD%20OG%20TELEMARK")

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    articles = soup.find_all("article")
    
    jobs = []
    
    for article in articles:
        title = article.find("p", class_="mb-4")
        link = article.find("a")

        job_title = f"{str(title.text) if title else link.text.strip()}"
        
        job_link = link.get("href") if link else None
        job_link_url = f"https://arbeidsplassen.nav.no{job_link}"

        jobs.append({job_title: job_link_url})
       
    driver.quit()
    return jobs


def get_new_jobs(previous_jobs):
    current_jobs = get_jobs_in_content()
    new_jobs = []
    for job in current_jobs:
        if job in previous_jobs:
            continue
        else:
            new_jobs.append(job)
    return new_jobs


def main():
    #previous_jobs = get_jobs_in_content()
    
    while True:
        time.sleep(30)
        new_listed_jobs = get_new_jobs(previous_jobs)
        if new_listed_jobs:
            for new_job in new_listed_jobs:
                print(new_job)
                email_subject = "New job!"

                email_body = "WAY!"
                send_email(email_subject, email_body)    
                previous_jobs.append(new_job)
        else:
            print("No new jobs listed")
            


import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    # Replace these with your email and password
    sender_email = "automailherman@gmail.com"
    sender_password = "u!4yGj{a)Q"

    recipient_email = "hermanskovbjerg@gmail.com"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")


main()