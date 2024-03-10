### Project archived
This project is one of the many practice assignments for my degree and there will be no more further development. This project contains multiple vulnerabilities (intentionally and unintentionally), so use it at your own risk!

## Project description

<img src=".\documents\screenshot_1.PNG" alt="screenshot_1" style="zoom: 67%;" />

"SecuMsgr" is a course project for Cyber Security 2021 carried out by the Department of Computer Science at the University of Helsinki. The main goal was to create a web application with Python and Django and include five out of ten TOP-10 vulnerabilities from [OWASP's list](https://owasp.org/Top10/).

#### Installation instructions

Clone or download project, confirm that you have Python 3 and Django installed, then navigate with your terminal to the project folder root and insert these commands*:

- python3 manage.py migrate
- python3 manage.py loaddata demodata.json
- python3 manage.py runserver

Open the browser and navigate to: localhost:8000

*On Windows use python instead of python3.

#### User credentials

- `admin : admin1`
- `chrissy : 123456`
- `nemo : g43W3w`
- `lorena : ******`

It is recommended to login as Chrissy (most of the demo data on this account). Admin is the only superuser. All usernames are case sensitive.
