from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ensure secret_key is set for sessions
app.secret_key = os.urandom(24)  # Use a random 24-byte secret key

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        website = request.form.get('website', '')
        summary = request.form['summary']

        # Split skills into a list of individual skills
        skills = request.form['skills'].split(',')  
        skills = [skill.strip() for skill in skills]  

        # Education section (optional second degree)
        education = []
        education.append({
            'degree': request.form['edu_degree1'],
            'institution': request.form['edu_institution1'],
            'start_date': request.form['edu_duration1'],
            'end_date': request.form['edu_duration1'],
            'cgpa': request.form['edu_cgpa1']
        })
        if request.form.get('edu_degree2'):
            education.append({
                'degree': request.form['edu_degree2'],
                'institution': request.form['edu_institution2'],
                'start_date': request.form['edu_duration2'],
                'end_date': request.form['edu_duration2'],
                'cgpa': request.form['edu_cgpa2']
            })

        # Work Experience section
        work_experience = []

        if request.form.get('exp_position1') and request.form.get('exp_company1'):
            work_experience.append({
                'position': request.form['exp_position1'],
                'company': request.form['exp_company1'],
                'start_date': request.form['exp_start_date1'],
                'end_date': request.form['exp_end_date1'],
                'duties': request.form.getlist('duties1')
            })

        if request.form.get('exp_position2'):
            work_experience.append({
                'position': request.form['exp_position2'],
                'company': request.form['exp_company2'],
                'start_date': request.form['exp_start_date2'],
                'end_date': request.form['exp_end_date2'],
                'duties': request.form.getlist('duties2')
            })

        # Project Details Section
        projects = []
        
        if request.form.get('project1_title'):
            projects.append({
                'title': request.form['project1_title'],
                'description': request.form['project1_description'],
                'technologies': request.form['project1_technologies'].split(',')
            })

        if request.form.get('project2_title'):
            projects.append({
                'title': request.form['project2_title'],
                'description': request.form['project2_description'],
                'technologies': request.form['project2_technologies'].split(',')
            })

        # Handle profile image upload
        profile_image = None
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                profile_image = f"static/uploads/{filename}"

        return render_template('resume_template.html', name=name, email=email, phone=phone, address=address,
                               website=website, summary=summary, skills=skills, education=education,
                               work_experience=work_experience, projects=projects, profile_image=profile_image)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
