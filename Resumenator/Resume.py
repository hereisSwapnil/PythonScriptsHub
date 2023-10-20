import streamlit as st
from jinja2 import Environment, FileSystemLoader, select_autoescape
# Load Jinja environment with the template folder
def temp1() :
    template_env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(['html', 'xml'])
    )
    def generate_resume(user_data):
        template = template_env.get_template("ResumeTemplate.html")
        rendered_html = template.render(data=user_data)
        return rendered_html
    def save_to_html(html_content):
        with open("Resume.html", "w") as html_file:
            html_file.write(html_content)

    user_data1 = {'Inst':[],'Proj':[]}
    st.title("Resume Generator")
    # Input fields for user data
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    a=st.columns([1,2])
    with a[0]: 
        number_inputs = st.number_input('Number of Degrees',min_value=1, max_value=10)
    for i in range(number_inputs):
        st.write(f"Institute {i + 1}")
        cols = st.columns(4)  # Divide row into 4 columns
        Inst_data = {
            "Institutename": cols[0].text_input(f"Institution Name", key=f"Institute_name{i}"),
            "Degreetype": cols[1].text_input(f"Degree type", key=f"Degree_type{i}"),
            "Degreeperiod": cols[2].text_input(f"Degree period", key=f"Degree_period{i}"),
            "cgpa": cols[3].text_input(f"Percentage / CGPA", key=f"cgpa_{i}"),
        }
        user_data1['Inst'].append(Inst_data)
    b = st.columns([1,2])
    with b[0]: 
        number_inputs1 = st.number_input('Number of Projects',min_value=1, max_value=10)        
    for i in range(number_inputs1):
        st.write(f"Projects {i + 1}")
        cols = st.columns(3)  # Divide row into 3 columns
        Project_data = {
            "ProjectName": cols[0].text_input(f"Project Name", key=f"project_name{i}"),
            "ProjectDesc": cols[1].text_input(f"Project Description", key=f"Project_desc{i}"),
            "ProjectStack": cols[2].text_input(f"Tech Stack used", key=f"tech_stacks{i}"),
        }
        user_data1['Proj'].append(Project_data)
    achivements = st.text_input('Achivements (seperate with , )')
    result_ach = achivements.split(',')
    prog_lan = st.text_input("Programming Languages you know (seperate with , )")
    result_pro = prog_lan.split(',')
    tools = st.text_input("Tools Used till now (seperate with , )")
    result_tools = tools.split(',')
    user_data = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "ProgLang": result_pro,
        "Tools": result_tools,
        "Achievement": result_ach,
        "GithubID": st.text_input("Github ID"),
        "LinkedinID": st.text_input("Linkedin ID"),
        "HackerRankID": st.text_input("HackerRank ID")
    }
    user_data.update(user_data1)
    if st.button("Generate Resume"):
        resume = generate_resume(user_data)
        save_to_html(resume)
        st.success("Resume generated successfully!")
        st.balloons()
        # Add a download button
        with open('Resume.html', 'rb') as f:
            st.download_button('Download resume', f, file_name='Resume.html')
