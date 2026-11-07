import streamlit as st

# ── 1. Headings & Title ───────────────────────────────────────
st.title("📄 Personal CV & Profile Generator")
st.subheader("Build your digital resume instantly")
st.markdown("---")

# ── 2. Info Box ───────────────────────────────────────────────
st.info("Fill out your information below, check the confirmation box, and click the button to generate your CV card.")

# ── 3. Input Widgets (More than 5 widget types) ────────────────
name = st.text_input("Full Name")
age = st.slider("Age", 18, 60, 22)
major = st.selectbox("Major / Specialization", ["Computer Science", "Artificial Intelligence", "Information Technology", "Software Engineering", "Data Science"])
gpa = st.number_input("GPA (out of 4.0)", 0.0, 4.0, 3.5, step=0.1)
bio = st.text_area("Short Bio (Tell us about yourself)")
ready_to_publish = st.checkbox("I confirm that the entered data is correct")

st.markdown("---")

# ── 4. Action Button & Reaction Logic ─────────────────────────
if st.button("Show My CV 🪪"):
    # Checkbox validation message (Warning box)
    if not ready_to_publish:
        st.warning("⚠️ Please check the confirmation box before generating your CV.")
    # Text input validation message (Error box)
    elif not name.strip():
        st.error("❌ Please enter your full name to proceed.")
    else:
        # Success message and Markdown Card (Success box)
        st.success("✅ Your Personal CV has been generated successfully!")
        
        # Formatted Markdown Profile Card
        st.markdown(f"""
        ### 🌟 Digital Profile Card
        ---
        - **Name:** {name}
        - **Age:** {age} Years old
        - **Major:** {major}
        - **GPA:** {gpa:.2f} / 4.0
        
        #### 📝 About Me:
        > *{bio if bio else "No bio provided."}*
        ---
        """)
