import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def st_button(icon, url, label, iconsize):
    if icon == 'IBM':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true"> 
                {label}
            </a>
        </p>'''
    return st.markdown(button_code, unsafe_allow_html=True)    
    