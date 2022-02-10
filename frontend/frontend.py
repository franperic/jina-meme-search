import streamlit as st
from config import IMAGE_PORT, IMAGE_SERVER, DEBUG, TEXT_PORT, TEXT_SERVER, TEXT_SAMPLES
from helper import (
    search_by_file,
    search_by_text,
    UI,
    convert_file_to_document,
    get_image_url,
)

matches = []

# Layout
st.set_page_config(page_title="Jina Meme Search", layout="wide")


st.header("Jina Meme Search")
# media_type = st.radio("Search with...", ["Text", "Image"])

# if media_type == "Image":
#     upload_cell, preview_cell = st.columns([12, 1])
#     query = upload_cell.file_uploader("")
#     if query:
#         doc = convert_file_to_document(query)
#         if st.button(label="Search"):
#             if not query:
#                 st.markdown("Please enter a query")
#             else:
#                 matches = search_by_file(document=doc, server=IMAGE_SERVER, port=IMAGE_PORT)

# elif media_type == "Text":
with st.form("text_search"):
    query = st.text_input("", key="text_search_box")
    search_fn = search_by_text
    submitted = st.form_submit_button("Search")
if submitted:
    matches = search_by_text(input=query, server=TEXT_SERVER, port=TEXT_PORT)[::2]
st.subheader("...or search from a sample")

for text in TEXT_SAMPLES:
    if st.button(text):
        matches = search_by_text(input=text, server=TEXT_SERVER, port=TEXT_PORT)[::2]


# Results area
cell1, cell2, cell3 = st.columns(3)
cell4, cell5, cell6 = st.columns(3)
cell7, cell8, cell9 = st.columns(3)
all_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]

for cell, match in zip(all_cells, matches):
    cell.image("http:" + match.tags["image_url"])
