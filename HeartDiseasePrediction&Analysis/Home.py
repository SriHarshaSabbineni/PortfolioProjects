import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
def main():
    import streamlit as st
    st.set_page_config(
        page_title="Home"
    )
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        "Heart",
        "1234",
        30
    )
    name, authentication_status, username = authenticator.login('Login', 'main')
    if authentication_status == False:
        st.error("Username/Password are incorrect")
    elif authentication_status == None:
        st.warning("Enter your credentials")
    elif authentication_status:
        authenticator.logout('Logout', 'main')
        image = "heart_img3.jpeg"
        st.image(image,  use_column_width=True)
        st.title('Heart Disease Prediction & Analysis')
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("Enter project overview here")
        st.markdown("<hr>", unsafe_allow_html=True)
        no_sidebar_style = """
            <style>
                div[data-testid="stSidebarNav"] {display: inline;}
            </style>
        """
        st.markdown(no_sidebar_style, unsafe_allow_html=True)

if __name__ == '__main__':
    main()