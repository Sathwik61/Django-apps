
# Django Apps Collection

This repository contains several Django apps that demonstrate various functionalities, including displaying current date and time, managing student registrations, and creating interactive pages with AJAX. Each app is designed to showcase different aspects of Django development.

## Table of Contents

- [Apps Overview](#apps-overview)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [App Details](#app-details)
- [Contributing](#contributing)
- [License](#license)

## Apps Overview

1. **Current Date and Time**: Displays the current server date and time.
2. **Date and Time Offset**: Shows the current date and time with a four-hour offset both forward and backward.
3. **Fruit and Student Lists**: Displays an unordered list of fruits and an ordered list of selected students.
4. **Layout with Header and Footer**: Provides a base layout with a navigation menu and footer, including About Us and Home pages.
5. **Student Registration and Course Management**: Manages student registrations for courses through the admin interface and displays registered students.
6. **Project Model Form**: Creates a model form for students to register their project details, including chosen topic, languages used, and duration.
7. **Student Enrollment Views**: Provides generic class views for listing students and detailed views for individual student information.
8. **CSV Generation**: Generates CSV files from Django models.
9. **AJAX Registration Page**: Allows student registration without page refresh using AJAX.
10. **AJAX Search Application**: Searches for courses enrolled by a student using AJAX.

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sathwik61/Django-apps.git
    cd your-repo
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser for the admin interface:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the Django admin interface** at `http://localhost:8000/admin/` to manage app data.
2. **Visit each app's URL** to see the functionality in action:
   - **Current Date and Time**: `/current-time/`
   - **Date and Time Offset**: `/time-offset/`
   - **Fruit and Student Lists**: `/lists/`
   - **Layout Pages**: `/about/` and `/home/`
   - **Student Registration and Course Management**: `/courses/`
   - **Project Model Form**: `/project-form/`
   - **Student Enrollment Views**: `/students/` and `/students/<id>/`
   - **CSV Generation**: `/generate-csv/`
   - **AJAX Registration Page**: `/ajax-register/`
   - **AJAX Search Application**: `/search-courses/`

## App Details

### 1. Current Date and Time

Displays the current date and time from the server.

### 2. Date and Time Offset

Shows the date and time four hours ahead and four hours before the current time.

### 3. Fruit and Student Lists

Displays an unordered list of fruits and an ordered list of selected students.

### 4. Layout with Header and Footer

Provides a base layout (`layout.html`) with a navigation menu and footer. Includes About Us and Home pages that inherit from the base layout.

### 5. Student Registration and Course Management

Allows student registration through the admin interface and displays a list of registered students for selected courses.

### 6. Project Model Form

Includes a model form for students to input project details such as chosen topic, languages used, and duration.

### 7. Student Enrollment Views

Provides a generic class view for listing students and a detail view for individual student information.

### 8. CSV Generation

Generates CSV files for Django models.

### 9. AJAX Registration Page

Facilitates student registration using AJAX to avoid page refresh.

### 10. AJAX Search Application

Searches for courses enrolled by a student using AJAX.


---

