# SURVEYPRO

## postman collection link
[Link to postman](https://www.postman.com/technical-saganist-92041798/skyworld/collection/kr4dj2y/surveypro?action=share&creator=16848533)

## My Required files 
in the folder named required_files
1. Erd - erd.png 
2. Postman - postman_collection_link.txt
For this Postman is in a live public url
3. Sql Code - sql_code.sql
This project is build on django orm but that is a copy of the sql I would have used to achieve the same results

## Set Up
1. Clone repo
2. cd into repo 
3. Create Env ```python -m venv env```
4. Install requirements ```pip install -r requirements.txt```
5. Create .env from .env.example
6. Make migrations ```python manage.py makemigrations```
7. Run migrations ```python manage.py migrate```
8. Create Super User ```python manage.py createsuperuser```
9. Log in to django admin
10. Create Questions 

### 1. Creating Single Select Question example: Yes or No
- Question type = Choice
- Text = "Your Question"
- Description = "Help Text eg, gender is required"
- Multiple = No

### 2. Creating Email Question
- Question type = Email
- Text = "Your Question"
- Description = "Help Text eg, gender is required"
- Multiple = No

### 3. Creating Multiple Choice Questions
- Question type = Choice
- Text = "Your Question"
- Description = "Help Text eg, You can have many choices"
- Multiple = Yes

### 3. Accepting Files example: Certificates
- Question type = File
- Text = "Your Question"
- Description = "Help Text eg, gender is required"
- Multiple = No

### 4.Creating Short / Long answer questions
- Question type = Short Text / Long Text
- Text = "Your Question"
- Description = "Help Text eg, gender is required"
- Multiple = No

