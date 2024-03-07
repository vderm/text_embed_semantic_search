"""
TODO
+ write metadata
+ filter by date added or updated
+ filter by tags (multiple) https://stackoverflow.com/questions/45312377/how-to-one-hot-encode-from-a-pandas-column-containing-a-list
+ filter by category (one) --> needed?
+ sort by date after filter... able to rebuild "story"
+ search?
+ generate card
+ load file from link to file?
+ function for new panel
+ function for new card (card lives in panel)
+ shortcuts in sidebar
+ capture new note --> start in streamlit -> open in vim or vscode

DONE
+ read all metadata

"""

import os
import frontmatter

import pandas as pd
import streamlit as st

from utils import read_added_to_git_cache, read_markdown_metadata

CURRENT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(CURRENT_DIR)
NOTES_DIR = os.path.join(PARENT_DIR, "notes")
added_to_git_filepath = os.path.join(CURRENT_DIR, "added_to_git_output.csv")


# Scan files and merge with git info
markdown_dict = read_markdown_metadata(NOTES_DIR)
df_added_to_git = read_added_to_git_cache(added_to_git_filepath)
df = pd.DataFrame.from_dict(markdown_dict, orient="index")
df = df.join(df_added_to_git)
# st.dataframe(df)


# TODO: skip metadata
# TODO: fix links
# TODO: fix images
# def read_markdown(filepath: str, read_chars: int = None) -> str:
#     with open(filepath, "r") as f:
#         file_str = f.read(read_chars)
#     return file_str

def read_markdown(filepath: str) -> str:
    with open(filepath, "r") as f:
        metadata, content = frontmatter.parse(f.read())
    return metadata, content


mila_timl_filepath = "/home/vasken/Repos/foam-notes/notes/mila-timl.md"
metadata, file_str = read_markdown(mila_timl_filepath)
st.title(metadata["title"])
st.markdown(file_str, unsafe_allow_html=True)
