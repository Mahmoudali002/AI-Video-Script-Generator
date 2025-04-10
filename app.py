import streamlit as st
from main import VideoScriptGenerator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Video Script Generator",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Header
    st.title("🎬 AI Video Script Generator")
    st.markdown("Generate engaging video scripts for YouTube Shorts and Instagram Reels")
    
    # Sidebar
    with st.sidebar:
        st.header("Settings")
        platform = st.selectbox(
            "Choose Platform",
            ["YouTube Shorts", "Instagram Reels"],
            key="platform"
        )
        
        niche = st.text_input(
            "Enter Your Niche",
            placeholder="e.g., fitness, cooking, technology",
            key="niche"
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("This tool helps you generate engaging video scripts using AI.")

    # Main content
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown("### Script Parameters")
        
        tone = st.selectbox(
            "Content Tone",
            ["Informative", "Entertaining", "Professional", "Casual"]
        )
        
        duration = st.slider(
            "Video Duration (seconds)",
            min_value=15,
            max_value=60,
            value=30,
            step=15
        )

    # Generate button
    if st.button("Generate Script", type="primary"):
        if not niche:
            st.error("Please enter a niche first!")
            return
            
        try:
            with st.spinner("Generating your script..."):
                generator = VideoScriptGenerator()
                platform_key = "youtube_shorts" if platform == "YouTube Shorts" else "instagram_reels"
                script = generator.generate_script(niche, platform_key)
                
                # Display results
                st.markdown("### Your Generated Script")
                st.markdown("---")
                
                # Parse and display script sections
                sections = script.split("\n\n")
                for section in sections:
                    if "HOOK:" in section:
                        st.markdown("#### 🎯 Hook")
                        st.markdown(section.replace("HOOK:", ""))
                    elif "MAIN CONTENT:" in section:
                        st.markdown("#### 📝 Main Content")
                        st.markdown(section.replace("MAIN CONTENT:", ""))
                    elif "CALL TO ACTION:" in section:
                        st.markdown("#### ⚡ Call to Action")
                        st.markdown(section.replace("CALL TO ACTION:", ""))
                
                # Download button
                st.download_button(
                    label="Download Script",
                    data=script,
                    file_name=f"video_script_{niche.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()