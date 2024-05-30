# import streamlit as st

# def next_button(current_page, next_page):
#     if st.button("Sonraki Derse Git"):
#         st.experimental_set_query_params(page=next_page)
#         st.experimental_rerun()

# def get_current_page():
#     query_params = st.experimental_get_query_params()
#     return query_params.get("page", [None])[0]

# def set_initial_page(default_page):
#     if 'initialized' not in st.session_state:
#         st.session_state['initialized'] = True
#         if not st.experimental_get_query_params().get("page"):
#             st.experimental_set_query_params(page=default_page)
#             st.experimental_rerun()
