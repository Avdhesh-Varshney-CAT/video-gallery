import streamlit as st

def dashboard():
	st.title("Welcome to the Streamlit Videos World!")

	st.write("This is a simple Streamlit app that showcases videos from different websites. You can watch videos, download them, visit the website, and watch more videos from the website.")

	st.write("To get started, you can log in or sign up to access the dashboard. If you are already logged in, you can view your profile and log out.")

	st.write("You can also view videos from different websites by clicking on the respective links in the sidebar.")

	st.write("Enjoy watching videos!")

	st.write("Note: This app is for educational purposes only and does not host any videos.")

	st.markdown("You can also access vercel website: [click](https://main-gallery.vercel.app/)")

	st.info("Made with ❤️ by Avdhesh", icon="ℹ️")

dashboard()
