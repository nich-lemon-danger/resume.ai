import streamlit as st
from groq import Groq
client = groq(api_key=st.secrets["GROQ_API_KEY"])
client = Groq(api_key="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")

st.set_page_config(
    page_title="AI Resume Scorer",
    page_icon="🚀",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    }
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #7b2ff7);
        color: white;
        font-size: 1.2em;
        font-weight: bold;
        border: none;
        border-radius: 30px;
        padding: 15px 40px;
        width: 100%;
    }
    .stTextArea textarea {
        background-color: #1a1a2e;
        color: white;
        border: 1px solid #00d2ff;
        border-radius: 10px;
        modle="1lama-3.3-70b-versatile" }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#00d2ff'>🚀 AI Resume Scorer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888'>Land your dream job with AI-powered resume analysis</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.info("⚡ Instant Results")
with col2:
    st.info("🎯 AI Powered")
with col3:
    st.info("💰 100% Free")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📋 Your Resume")
    resume = st.text_area(
        "Resume",
        height=250,
        placeholder="Paste your resume here...",
        label_visibility="collapsed"
    )
with col2:
    st.markdown("### 💼 Job Description")
    job = st.text_area(
        "Job",
        height=250,
        placeholder="Paste job description here...",
        label_visibility="collapsed"
    )

if st.button("🔍 ANALYZE MY RESUME NOW"):
    if resume and job:
        with st.spinner("🤖 AI is analyzing your resume..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role": "user",
                    "content": f"""
You are an expert HR recruiter and career coach.
Analyze this resume against the job description.

RESUME: {resume}
JOB DESCRIPTION: {job}

Give detailed analysis:
1. MATCH SCORE: X out of 100
2. TOP 5 MATCHING SKILLS
3. TOP 5 MISSING SKILLS
4. 3 WAYS TO IMPROVE RESUME
5. 3 INTERVIEW TIPS
6. SHOULD THEY APPLY? Yes or No

Use emojis and be encouraging.
                    """
                }]
            )
            result = response.choices[0].message.content

        st.balloons()
        st.success("✅ Analysis Complete!")
        st.markdown(result)
        st.download_button(
            label="📥 Download Report",
            data=result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )
    else:
        st.error("⚠️ Please paste both resume AND job description!")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#555'>🚀 AI Resume Scorer • Powered by Groq • 100% Free</p>", unsafe_allow_html=True)