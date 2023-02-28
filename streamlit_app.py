import streamlit as st

st.title('Data Science')

def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
st.markdown('# 30 Days of Streamlit')

days_list = [f'Day {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox('Start the Challenge 👇', days_list, key="day", on_change=update_params)
