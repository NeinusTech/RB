from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed

class ResumeForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    phone = StringField("Phone Number", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    experience = IntegerField("Years of Experience", validators=[DataRequired()])
    
    qualification = SelectField("Highest Qualification", choices=[
        ("Bachelors", "Bachelors"),
        ("Masters", "Masters"),
        ("PhD", "PhD"),
        ("Diploma", "Diploma"),
    ], validators=[DataRequired()])
    
    skills = SelectField("Technical Skills", choices=[
        ("Python", "Python"),
        ("Java", "Java"),
        ("C++", "C++"),
        ("HTML", "HTML"),
        ("Web Development", "Web Development"),
        ("Data Science", "Data Science"),
    ], validators=[DataRequired()])
    
    photo = FileField("Upload Photo", validators=[FileAllowed(["jpg", "png"], "Images only!")])
    submit = SubmitField("Generate My Profile")
