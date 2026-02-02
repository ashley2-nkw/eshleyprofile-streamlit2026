import streamlit as st


# Set page title
st.set_page_config(page_title="Nkwane Eshley Senoni profile", layout="wide")



profile_image_url = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg"

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile","About", "Contact"],
)

# Sections based on menu selection
if menu == "Profile":
    st.title("Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Nkwane Eshley Senoni"
    field = "Computer Science"
    institution = "University of Limpopo"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Study:** {field}")
    st.write(f"**Institution:** {institution}")
    
    # Display profile picture from URL
    st.image(profile_image_url, caption="Nature (Pixabay)")

elif menu == "About":
    st.title("About")
    st.sidebar.header("About Me")
    
    st.write("""
    I am a passionate computer science student in my final year at the University of Limpopo. I am deeply interested in technology, especially in software development, and enjoy building solutions that solve real-world problems. My goal is to become a skilled software developer and contribute to innovative projects. I am always eager to learn new programming languages, frameworks, and tools to expand my knowledge and expertise.
    """)
    
    # Display profile picture from URL
    st.image(profile_image_url, caption="Nature (Pixabay)")

elif menu == "Contact":
    
    st.header("Contact Information")
    email = "ashleynkwane8@gmail.com"
    phone = "0634118366"  
    st.write(f"You can reach me at {email}.")
    st.write(f"Phone: {phone}")