# Email Sender
Small application which can send custom emails to different users.

This app has two pages. A page with a form and a page with confirmation.

## Email form page.

A Form has three fields:

1. Email subject.
2. Recipent list.
3. Email message.

It is evident how first and last field work. But it's necessary to explain how the second field works.

In case you want to send an email to one person just write its email and click the button. In case of having multiple recipents you ought to write emails separating them with `', '`.

## Confirmation page.

A simple page with notification that email was sent to all recipents. Their addresses will be written on the page.

## Installation

1. Copy a repository on your computer.
2. Create a virtual environment with `python -m venv venv`.
3. Activate it using `./venv/Scripts/activate`.
4. Install requirements with `pip install -r requirements.txt`.
5. In `settings.py` find `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`. Then change their values to your email account and email/application password.
6. Change your directory to `email_sender` using `cd email_sender`.
7. Launch application with `python manage.py runserver` and follow the link `http://127.0.0.1:8000`.

## Technology stack

1. Python 3.9.4
2. Django 4.0.3
