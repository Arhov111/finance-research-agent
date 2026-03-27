import streamlit as st
from crew import run_research

# page configuration
st.set_page_config(
    page_title="Finance Research Agent",
    page_icon="📈",
    layout="wide"
)

# title and description
st.title("📈 Finance & Crypto Research Agent")
st.markdown("""
This app uses AI agents to research any stock or cryptocurrency 
and generate a professional research report.
""")

# input section
st.subheader("Enter an asset to research")
asset = st.text_input(
    "Stock or Crypto",
    placeholder="e.g. Bitcoin, NVIDIA, Apple, Ethereum..."
)

# button to trigger research
if st.button("🔍 Generate Research Report"):
    if asset:
        # show spinner while agents are working
        with st.spinner(f"Researching {asset}... This may take a minute..."):
            try:
                result = run_research(asset)
                
                # display the report
                st.success("Research complete!")
                st.markdown("---")
                st.subheader(f"Research Report: {asset}")
                st.markdown(str(result))
            
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
    else:
        st.warning("Please enter a stock or crypto name first!")

# footer
st.markdown("---")
st.caption("Powered by CrewAI + Groq + DuckDuckGo")