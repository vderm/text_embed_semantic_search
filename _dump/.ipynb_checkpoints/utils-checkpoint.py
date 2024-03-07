"""
TODO
+ read all metadata
+ write metadata
+ filter by date
+ filter by tags (multiple)
+ sort by date after filter... able to rebuild "story"
+ search?
+ generate card
+ load file from link to file?
+ function for new panel
+ function for new card (card lives in panel)
+ shortcuts in sidebar
+ capture new note --> start in streamlit -> open in vim or vscode
"""

import os
import pandas as pd
import datetime
import frontmatter
import glob


def read_markdown_metadata(
        notes_dir: str,
        post_keys_keep_list: list = ["title", "author", "categories", "tags", "links", "date"],
) -> dict:
    assert os.path.exists(notes_dir), f"folder {dir} does not exist"
    markdown_dict = {}
    for filepath in glob.glob(os.path.join(notes_dir, "*.md")):
        # print(f"{filepath = }")
        filename = os.path.split(filepath)[1]
        post = frontmatter.load(filepath)
        markdown_dict[filename] = {
            "filepath": filepath,
            **{k:post.get(k, None) for k in post_keys_keep_list}
        }
    return markdown_dict


def read_added_to_git_cache(added_to_git_filepath: str) -> pd.DataFrame:
    """ Read git initial commit and updated cache """
    col_names_added_to_git = ["created", "updated"]
    df_added_to_git = pd.read_csv(
        added_to_git_filepath,
        names=col_names_added_to_git,
        index_col=[0],
    )
    for col in col_names_added_to_git:
        df_added_to_git[col] = pd.to_datetime(df_added_to_git[col])
    assert isinstance(df_added_to_git.iloc[0][col_names_added_to_git[0]], datetime.datetime)
    return df_added_to_git

