import streamlit as st

def next_button(next_page_name, next_page_label):
    button_html = f"""
    <style>
        .next-button-container {{
            display: flex;
            justify-content: flex-end;
            margin-top: 20px;
        }}
        .next-button {{
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            display: inline-block;
            font-weight: bold;
        }}
        .next-button:hover {{
            background-color: #45a049;
        }}
    </style>
    <div class="next-button-container">
        <a class="next-button" href="?next_page={next_page_name}">{next_page_label} &rarr;</a>
    </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
