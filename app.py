import streamlit as st
from groq import Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
client = Groq(api_key="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")

st.set_page_config(
    page_title="AI Resume Scorer",
    page_icon="🚀",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #000000;
}
canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 0;
}
.main .block-container {
    position: relative;
    z-index: 1;
}
</style>

<canvas id="matrix"></canvas>
<script>
var canvas = document.getElementById('matrix');
var ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()';
chars = chars.split('');
var fontSize = 14;
var columns = canvas.width / fontSize;
var drops = [];
for(var x = 0; x < columns; x++) {
    drops[x] = 1;
}
function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#00ff41';
    ctx.font = fontSize + 'px monospace';
    for(var i = 0; i < drops.length; i++) {
        var text = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillStyle = '#00ff41';
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        drops[i]++;
    }
}
setInterval(draw, 35);
window.addEventListener('resize', function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
</script>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; padding:30px'>
<h1 style='color:#00ff41; font-family:monospace; 
font-size:3em; text-shadow: 0 0 20px #00ff41'>
🚀 AI RESUME SCORER
</h1>
<p style='color:#00ff41; font-family:monospace;
opacity:0.7'>
> ANALYZING CAREERS WITH ARTIFICIAL INTELLIGENCE_
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        "<p style='color:#00ff41; font-family:monospace'>📋 YOUR RESUME</p>",
        unsafe_allow_html=True
    )
    resume = st.text_area(
        "Resume",
        height=250,
        placeholder="Paste your resume here...",
        label_visibility="collapsed"
    )
with col2:
    st.markdown(
        "<p style='color:#00ff41; font-family:monospace'>💼 JOB DESCRIPTION</p>",
        unsafe_allow_html=True
    )
    job = st.text_area(
        "Job",
        height=250,
        placeholder="Paste job description here...",
        label_visibility="collapsed"
    )

st.markdown("""
<style>
.stTextArea textarea {
    background-color: #0a0a0a !important;
    color: #00ff41 !important;
    border: 1px solid #00ff41 !important;
    font-family: monospace !important;
}
.stButton>button {
    background: transparent !important;
    color: #00ff41 !important;
    border: 2px solid #00ff41 !important;
    font-family: monospace !important;
    font-size: 1.2em !important;
    width: 100% !important;
    transition: all 0.3s !important;
}
.stButton>button:hover {
    background: #00ff41 !important;
    color: #000000 !important;
    box-shadow: 0 0 20px #00ff41 !important;
}
</style>
""", unsafe_allow_html=True)

if st.button("[ ANALYZE MY RESUME NOW ]"):
    if resume and job:
        with st.spinner("[ AI ANALYZING... ]"):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role": "user",
                    "content": f"""
You are an expert HR recruiter.
Analyze this resume against the job description.

RESUME: {resume}
JOB DESCRIPTION: {job}

Give:
1. MATCH SCORE: X out of 100
2. TOP 5 MATCHING SKILLS
3. TOP 5 MISSING SKILLS
4. 3 WAYS TO IMPROVE RESUME
5. 3 INTERVIEW TIPS
6. SHOULD THEY APPLY? Yes or No

Use emojis and clear formatting.
                    """
                }]
            )
            result = response.choices[0].message.content

        st.markdown("""
            <div style='border:1px solid #00ff41; 
            padding:20px; background:#0a0a0a;
            font-family:monospace'>
        """, unsafe_allow_html=True)
        st.success("[ ANALYSIS COMPLETE ]")
        st.markdown(
            f"<div style='color:#00ff41; font-family:monospace'>{result}</div>",
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.download_button(
            label="[ DOWNLOAD REPORT ]",
            data=result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )
    else:
        st.error("[ ERROR: PLEASE FILL BOTH FIELDS ]")

st.markdown("""
<p style='text-align:center; color:#00ff41; 
font-family:monospace; opacity:0.5; font-size:0.8em'>
> AI RESUME SCORER v2.0 • POWERED BY GROQ & LLAMA AI • FREE FOREVER_
</p>
""", unsafe_allow_html=True)
