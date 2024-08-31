import streamlit as st
from pathlib import Path
from PIL import Image

#------path setting
current_dir = Path(__file__).parent if"__file__" in locals() else Path().cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "resume.pdf"
profile_pic = current_dir / "profile_pic.jpg"

PAGE_TITLE = "Sanika Patil"
PAGE_ICON = ":wave:"
NAME = "Hello :wave: I'm Sanika Patil"
DESCRIPTION = """
a fresh and enthusiastic software developer with a strong foundation in Computer Science and Engineering. 
I'm eager to learn new technologies, take on challenges, and build innovative solutions. 


"""
EMAIL = "2611sanika@gmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/sanikaap/",
    "LinkedIn": "https://linkedin.com/in/sanika-patil-8623a5223",
    "Codechef": "https://www.codechef.com/learn",
    "Leetcode": "",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.write('----------')
st.subheader('👩🏻‍💻Projects')
st.subheader(" :rocket: Autism Spectrum Disorder Detection Using Machine Learning")
st.write(
    """
- ► Directed a thorough investigation of machine learning-based methods for detecting ASD. 
- ► Led a significant research effort to improve ASD diagnostic precision and
early intervention
    """
)
st.write('\n')


st.subheader(" :rocket:  Twitter Clone - Using Next.Js")
st.write(
    """
- ► Create reusable UI components for tweets,user profiles,comments,and likes using Tailwind CSS classes.
- ►  Implement Next.js routing for different pages and design consistent layouts for a seamless user experience.

    """
)
st.write('\n')

st.subheader(" :rocket: Sorting Algorithm Visualizer")
st.write(
    """
- ► Engineered a sorting algorithm visualizer that allows users to see how different sorting algorithms work.
- ► Developed a web application that allows users to see how different sorting algorithms work.
    """
)




# --- SKILLS ---
st.write('\n')
st.subheader(" :star: Hard Skills & Soft Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C & C++, Java
- 📊 Frameworks: HTML, CSS, JavaScript, Bootstrap, ReactJS, Tailwind CSS,NextJS,Node js , Express js , SpringBoot, Django
- 📊 Familar with: Git , Github , Gitlab, Bitbucket, Devops,Docker , Kubernetes
- 🗄️ Databases: Postgres, MongoDB, MySQL , MongoDB
- :star: Soft skills: Teamwork, Communication, Problem Solving, Adaptability, Work Ethic
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader(" :fire: Internships")
st.write("---")

# --- JOB 1
st.write("🚧", "**Machine Learning Intern | 1STOP.AI**")
st.write("Aug 2022 - oct 2022")
st.write(
    """
- ► Built a sentiment analysis model using a variety of NLP
    techniques, including text classification, tokenization, and lemmatization.
- ► Developed a high-accuracy NLP system to extract features from
restaurant reviews, achieving over 90% accuracy on a held-out
test set

"""
)

 #--- JOB 1
st.write("🚧", "**Software Engineering Intern Virtual Experience Program| Goldman Scahs**")
st.write("April 2023 - May 2023")
st.write(
    """
- ► Researched a broken password database as a virtual intern at
Goldman Sachs
- 

"""
)

st.write('\n')
st.write('----------')
st.subheader(' :medal: Achievements')
st.write(
    """
- ► Codechef Rating : Solve 100+ problems on Codechef
- ► Research Paper : Published a research paper on "Autism Spectrum Disorder Detection Using Machine Learning" in UGC Approved Journal
    """
)

st.write('\n')
st.write('----------')
st.subheader(' 🎓 Certifications and Courses')
st.write(
    """
- ► Geneative AI Microsoft and Linedin Learning Professional Certificate
- ► Learning Java Linedin Learning
- ► React Js - HackerRank
- ► Python _ HackerRank
- ► C++ Fundamentals - Infosys Springboard
- ► Data Structures and Algorithms - Infosys Springboard
- ► Database Management System - Infosys Springboard
"""
)
st.write('\n')
st.write('----------')
st.subheader('🤩Interests')
st.write(
    """
 - ► TED Talks
 - ► Travelling
 - ► Listening Music
 - ► Reading Books
    """
)
    



# --- Projects & Accomplishments ---
