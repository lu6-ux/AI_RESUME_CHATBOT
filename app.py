import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills

# ================= Page Setup =================
st.set_page_config(
    page_title="AI Resume Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ================= Custom CSS for Background & Cards =================
st.markdown("""
<style>
/* Full-page gradient background */
body {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
}

/* Card style for resumes */
.resume-card {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 2px 2px 20px rgba(0,0,0,0.3);
}

/* Skill badges */
.skill-badge {
    background: linear-gradient(135deg, #FF4B4B, #FF8C42);
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    margin: 3px;
    display: inline-block;
    font-weight: bold;
}

/* Sidebar custom style */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #4CA1AF, #C4E0E5);
    color: black;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ================= Sidebar =================
with st.sidebar:
    st.markdown("<h2>💡 How to Use</h2>", unsafe_allow_html=True)
    st.write("""
        1. Upload one or multiple resumes in **PDF** format.  
        2. System extracts text and detects your skills.  
        3. Skills are highlighted with **colorful badges**.  
        4. Match percentage is displayed as a progress bar.  
        5. Works best with **text-based PDFs**.  
    """)
    st.markdown("---")
    st.markdown("Powered by **Lakshana Gnanasekaram**", unsafe_allow_html=True)

# ================= Load Skills =================
with open("skills.txt") as f:
    skills_list = [line.strip() for line in f]

# ================= Main Title =================
st.markdown("<h1 style='text-align:center; color:#FF4B4B;'>🤖 AI Resume Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ffffff;'>Upload PDF resumes to extract skills and match percentages</p>", unsafe_allow_html=True)
st.write("---")

# ================= File Uploader =================
uploaded_files = st.file_uploader(
    "📂 Drag & drop PDF resumes here or click to upload",
    type=["pdf"],
    accept_multiple_files=True,
    key="file_uploader"
)

# ================= Process Resumes =================
if uploaded_files:
    for file in uploaded_files:
        # Card-style container
        st.markdown(f"<div class='resume-card'>", unsafe_allow_html=True)
        st.markdown(f"### 📄 {file.name}")
        st.write(f"File size: {round(len(file.getvalue())/1024, 2)} KB")

        # Extract text
        text = extract_text_from_pdf(file)

        # Extract skills
        found_skills = extract_skills(text, skills_list)
        match_percentage = int(len(found_skills)/len(skills_list)*100) if skills_list else 0

        # Match progress
        st.markdown(f"**Match Percentage:** {match_percentage}% 🔥")
        st.progress(match_percentage)

        # Display skill badges
        if found_skills:
            st.markdown("**Skills Found:**")
            badges_html = " ".join([f"<span class='skill-badge'>{skill}</span>" for skill in found_skills])
            st.markdown(badges_html, unsafe_allow_html=True)
        else:
            st.warning("No matching skills found 😕")

        st.markdown("</div>", unsafe_allow_html=True)
        st.write("---")

# ================= Footer =================
st.markdown(
    "<p style='text-align:center; font-size:12px; color:lightgray;'>Powered by Streamlit & Python | AI Resume Chatbot</p>",
    unsafe_allow_html=True
)