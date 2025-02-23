Overview

The Resume Builder is a Flask-based web application that allows users to create and download professional resumes in PDF format. It supports dynamic profile selection, pre-filled forms, profile image uploads, and custom styling.

Features

✅ User Profile & Image Upload – Users can upload and preview their profile images.✅ Pre-Filled Form Data – Loads existing user data using JSON.✅ Custom Resume Templates – Dynamically populates templates using Jinja2.✅ PDF Download Support – Converts resumes to PDF using html2pdf.js.✅ Dynamic Sections – Supports Education, Work Experience, Skills, and Projects.✅ Responsive Design – Ensures proper display across devices.✅ Page Break Handling – Automatically inserts page breaks if content exceeds A4 size.✅ Proper PDF Borders – Ensures content is not cut off on the right side.

Technologies Used

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript (Jinja2 for templating)

PDF Generation: html2pdf.js, jsPDF

Styling: CSS (custom styling for resume templates)

Installation & Setup

Prerequisites

Ensure you have Python 3.x installed.

Steps

1️⃣ Clone the repository:

git clone https://github.com/NeinusTech/RB.git
cd resume-builder

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run the Flask app:

python app.py

4️⃣ Open your browser and go to:

http://127.0.0.1:5000

Usage

Fill out the form with your details.

Upload a profile image (optional).

Click "Download PDF" to generate your resume.
