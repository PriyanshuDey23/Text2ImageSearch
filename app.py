import streamlit as st
from multimodel_search import MultimodalSearch

# Constants
NUM_SEARCH_RESULTS = 3

def display_header():
    st.markdown("<h1 style='text-align: center; color: green;'>Fashion Cloth Search App</h1>", unsafe_allow_html=True)

def get_user_query():
    return st.text_input("Enter your query:")

def perform_search(query, multimodal_search):
    try:
        return multimodal_search.search(query)
    except Exception as e:
        st.error(f"An error occurred during the search: {str(e)}")
        return []

def display_results(results):
    if len(results) == 0:
        st.warning("No results found.")
        return

    st.warning("Your query was " + results[0].query)
    st.subheader("Search Results:")
    cols = st.columns([1,1,1])
    for i, result in enumerate(results[:NUM_SEARCH_RESULTS]):
        with cols[i]:
            st.write(f"Score: {round(result.score*100, 2)}%")
            st.image(result.content, use_column_width=True)

def main():
    display_header()
    multimodal_search = MultimodalSearch()
    query = get_user_query()
    if st.button("Search"):
        if len(query) > 0:
            results = perform_search(query, multimodal_search)
            display_results(results)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()