import streamlit as st
import time

# Page Config
st.set_page_config(page_title="ClarityAI Prototype", page_icon="🚀", layout="wide")

# Custom CSS for "AI" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4259; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🚀 ClarityAI: GenAI Career Copilot")
st.write("### *Stop Guessing. Start Building.*")
st.divider()

# Sidebar
with st.sidebar:
    st.header("👤 Student Profile")
    name = st.text_input("Full Name", "Ankit Sharma")
    target_role = st.selectbox("Target Role", ["Full Stack Developer", "Data Scientist", "AI Engineer", "Product Manager"])
    uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    interests = st.multiselect("Interests", ["GenAI", "Fintech", "Web3", "HealthTech"], ["GenAI"])

# Main Dashboard Logic
if st.button("Generate Career Intelligence Engine ⚡"):
    if uploaded_file is not None:
        with st.spinner("Analyzing Resume & Matching with Industry Pulse..."):
            time.sleep(2) # Fake processing time for demo effect
            
        # Layout Columns
        col1, col2 = st.columns([1, 1.5])

        with col1:
            st.subheader("📊 Skill Gap Intelligence")
            st.metric(label="Current Readiness Score", value="62%", delta="-23% from Industry Average")
            
            st.write("**Missing Skills (High Impact):**")
            st.error("❌ System Design (LLM Scalability)")
            st.error("❌ Vector Databases (Pinecone/Chroma)")
            st.error("❌ CI/CD Pipelines")
            
            st.write("**Matched Skills:**")
            st.success("✅ Python (Advanced)")
            st.success("✅ React.js")
            st.success("✅ Fast API")

        with col2:
            st.subheader("🏗️ Industry-Aligned Project Idea")
            with st.container():
                st.info(f"**Project Title:** Multi-Agent {interests[0]} Research Assistant")
                st.write("**Why?** This closes your 'Vector DB' gap and aligns with current {target_role} hiring trends.")
                st.write("**Architecture:** LangChain + Pinecone + Streamlit")
                st.write("**Resume Bullet:** 'Built a RAG-based engine reducing research time by 40%.'")

        st.divider()
        
        # 90-Day Roadmap
        st.subheader("📅 Personalized 90-Day Action Plan")
        tab1, tab2, tab3 = st.tabs(["Month 1: Foundation", "Month 2: Build", "Month 3: Placement"])
        
        with tab1:
            st.write("Target: Master Vector Databases & RAG Architecture.")
            st.progress(100, text="Focus: Data Persistence")
        with tab2:
            st.write("Target: Complete the Multi-Agent Research Project.")
            st.progress(50, text="In Progress: Deployment")
        with tab3:
            st.write("Target: 10 Mock Interviews & Resume Polishing.")
            st.progress(10, text="Pending")

    else:
        st.warning("Please upload a resume to start the analysis.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Built for Students 🎓 By Students")
