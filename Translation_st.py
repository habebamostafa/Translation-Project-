#########################################################################################
# this code for streamlit the Translation Project
#########################################################################################

# this code test for stream sharing and test it is cloud 

# import streamlit as st
# st.title("Text Translation App")
# input_text = st.text_area("Enter text to translate", "")
# if st.button("Translate"):
#     st.write("Translated Text:", input_text[::-1])  # For demo, reverse text


# the Actual code uesd 
import streamlit as st
import tempfile

# Set the page title and layout
st.set_page_config(page_title="Translation App", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ("Home", "Text Translation", "Audio Translation", "Image Translation", "PDF Translation"))

# Home page
if page == "Home":
    st.header("Translation project")
    st.title("Welcome to the Real-Time Translation Project!")
    st.title("Let's bridge the language gap and connect the world")
    st.write("We're excited to have you join our mission to the Translation App! Use the sidebar to navigate through the different translation options.")

# Text Translation page
elif page == "Text Translation":
    st.title("Text Translation")
    input_text = st.text_area("Enter text to translate", "")
    if st.button("Translate"):
        # Placeholder for actual translation logic
        st.write("Translated Text:", input_text[::-1])  # Example logic: reverse the text

# Audio Translation page
elif page == "Audio Translation":
    st.title("Audio Translation")
    
    # Record audio from the microphone
    if st.button("Record Audio"):
        audio_data = st.audio_recorder()  # Record audio
        if audio_data is not None:
            st.audio(audio_data, format='audio/wav')
            st.write("Audio recorded successfully.")
            
            # Save the audio to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio_file:
                tmp_audio_file.write(audio_data)
                audio_file_path = tmp_audio_file.name
                
            st.write(f"Audio saved at: {audio_file_path}")

    # Upload audio file
    audio_file = st.file_uploader("Or Upload Audio File", type=["wav", "mp3"])
    if audio_file is not None:
        st.audio(audio_file, format='audio/wav')
        st.write("Audio file uploaded successfully.")


# Image Translation page
elif page == "Image Translation":
    st.title("Image Translation")
    image_file = st.file_uploader("Upload Image File", type=["jpg", "jpeg", "png"])
    if image_file is not None:
        st.image(image_file, caption='Uploaded Image', use_column_width=True)
        st.write("Image file uploaded successfully.")

# PDF Translation page
elif page == "PDF Translation":
    st.title("PDF Translation")
    pdf_file = st.file_uploader("Upload PDF File", type=["pdf"])
    if pdf_file is not None:
        st.write("PDF file uploaded successfully.")
