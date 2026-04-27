import streamlit as st

# Page setup
st.set_page_config(page_title="New Rama Lab ", layout="wide")

# ---------- SIMPLE CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cccccc;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("📸 New Rama Lab ")
menu = st.sidebar.radio("Menu", ["Home", "Services", "Gallery", "Contact"])

# ---------- HOME ----------
if menu == "Home":
    st.markdown('<div class="title">New Rama Lab</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Capture Your Best Moments</div>', unsafe_allow_html=True)

    # Online image (no error)
    st.image("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee", use_column_width=True)

    st.write("## About Us")
    st.write("We provide professional photography and photo lab services.")

# ---------- SERVICES ----------
elif menu == "Services":
    st.title("Our Services")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><h3>Wedding</h3><p>₹50,000</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>Events</h3><p>₹15,000</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>Portrait</h3><p>₹5,000</p></div>', unsafe_allow_html=True)

# ---------- GALLERY ----------
elif menu == "Gallery":
    st.title("Gallery")

    col1, col2, col3 , col4 = st.columns(4)

    col1.image("https://images.unsplash.com/photo-1504198453319-5ce911bafcde")
    col2.image("https://images.unsplash.com/photo-1492724441997-5dc865305da7")
    col3.image("https://images.unsplash.com/photo-1516035069371-29a1b244cc32")
    col4.image("https://images.unsplash.com/photo-1519183071298-a2962be96b83")

# ---------- CONTACT ----------
elif menu == "Contact":
    st.title("Contact Us")

    st.write("📍  Bishan Sroop Colonay,Panipat, Haryana")
    st.write("📞 9813082872, ")

    st.write("### Send Message")
    name = st.text_input("Your Name")
    msg = st.text_area("Message")

    if st.button("Send"):
        st.success("Message sent successfully!")