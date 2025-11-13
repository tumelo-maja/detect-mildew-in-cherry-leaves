import streamlit as st


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func, version) -> None:
        self.pages.append({"title": title, "function": func, "version": version})

    def run(self):
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'], key="main-sidebar" )
        page['function'](page['version'])