import streamlit as st
from jinja2 import Environment, FileSystemLoader, select_autoescape
import base64
template_env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(['html', 'xml'])
)
def generate_resume(user_data):
    template = template_env.get_template("PortfolioTemplate.html")
    rendered_html = template.render(data=user_data)
    return rendered_html
def save_to_html(html_content):
    with open("Portfolio.html", "w") as html_file:
        html_file.write(html_content)
def temp2():
    st.title("Portfolio Generator")
    user_data = {
        "Companies": [],
        "Skills": [],
        "Hobbies": [],
        "Education": [],
        "Projects":[],
        "Ach":[],
        "PL":[],
        "Tool":[]
    }
    st.subheader("Personal Information")
    cols1, cols2 = st.columns(2)
    user_data["Name"] = cols1.text_input("Name")
    user_data["Call"] = cols1.text_input("Call")
    user_data["Mail"] = cols1.text_input("Mail")
    user_data["Website"] = cols1.text_input("Website")
    user_data["Home"] = cols2.text_input("Home")
    user_data["TwitterID"] = cols2.text_input("Twitter ID")
    user_data["LinkedinID"] = cols2.text_input("Linkedin ID")
    user_data["GithubID"] = cols2.text_input("Github ID")
    user_data["Bio"] = st.text_area("Bio", height=200)  # Increase the text area height
    num_companies = st.number_input("Number of Companies to Add", min_value=0, step=1)
    for i in range(num_companies):
        st.write(f"Company {i + 1}")
        cols = st.columns(4)  # Divide row into 4 columns
        company_data = {
            "CompanyName": cols[0].text_input(f"Company Name", key=f"company_name_{i}"),
            "CompanyPeriod": cols[1].text_input(f"Company Period", key=f"company_period_{i}"),
            "CompanyRole": cols[2].text_input(f"Company Role", key=f"company_role_{i}"),
            "WorkDetails": cols[3].text_input(f"Work Details", key=f"work_details_{i}"),
        }
        user_data["Companies"].append(company_data)

    num_Education = st.number_input("Education Data", min_value=0, step=1)
    for i in range(num_Education):
        st.write(f"Education Institute {i + 1}")
        cols = st.columns(4)  # Divide row into 4 columns
        Education_data = {
            "SchoolName": cols[0].text_input(f"School Name", key=f"SchoolName{i}"),
            "StudyPeriod": cols[1].text_input(f"Study period", key=f"StudyPeriod{i}"),
            "CourseName": cols[2].text_input(f"course Name", key=f"CourseName{i}"),
            "GPA": cols[3].text_input(f"GPA", key=f"GPA{i}"),
        }
        user_data["Education"].append(Education_data)

    num_Projects = st.number_input("Projects Data", min_value=0, step=1)
    for i in range(num_Projects):
        st.write(f"Project {i + 1}")
        cols = st.columns(2)  # Divide row into 4 columns
        Projects_data = {
            "ProjectName": cols[0].text_input(f"Project Name", key=f"Project_Name{i}"),
            "Techstacks": cols[1].text_input(f"Techstacks", key=f"ProjectName{i}"),
            "PDescription": st.text_area(f"Project Description", height=200,key=f"PDescription{i}"),
        }
        user_data["Projects"].append(Projects_data)


    num_skills = st.number_input("Number of Skills to Add", min_value=0, step=1, value=0)
    for i in range(num_skills):
        user_data["Skills"].append(st.text_input(f"Skill {i + 1}"))
    num_hobbies = st.number_input("Number of Hobbies to Add", min_value=0, step=1, value=0)
    for i in range(num_hobbies):
        user_data["Hobbies"].append(st.text_input(f"Hobby {i + 1}"))
    num_Ach = st.number_input("Number of Achievements to Add", min_value=0, step=1, value=0)
    for i in range(num_Ach):
        user_data["Ach"].append(st.text_input(f"Achievement {i + 1}"))
    ProgrammingLangs = st.number_input("Number of Programming Languages to Add", min_value=0, step=1, value=0)
    for i in range(ProgrammingLangs):
        user_data["PL"].append(st.text_input(f"Programming Lang {i + 1}"))
    num_tools = st.number_input("Number of Tools to Add", min_value=0, step=1, value=0)
    for i in range(num_tools):
        user_data["Tool"].append(st.text_input(f"Tool {i + 1}"))
    uploaded_image = st.file_uploader("Upload Profile Image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        image_data = uploaded_image.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")
        user_data["ProfileImage"] = encoded_image
    if st.button("Generate Resume"):
        resume = generate_resume(user_data)
        save_to_html(resume)
        st.success("Portfolio generated successfully!")
        st.balloons()
        with open('Portfolio.html', 'rb') as f:
            st.download_button('Download resume', f, file_name='Portfolio.html')
