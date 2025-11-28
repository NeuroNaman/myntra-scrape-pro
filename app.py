import pandas as pd
import streamlit as st
from dotenv import load_dotenv
load_dotenv()     # <---- THIS LOADS .env FILE

from src.cloud_io import MongoIO

import streamlit as st
from src.cloud_io import MongoIO
from src.constants import SESSION_PRODUCT_KEY
from src.scrapper.scrape import ScrapeReviews

st.set_page_config(
    "myntra-review-scrapper by Naman"
    

)

st.title("")
st.markdown("""
<style>
.header-title {
    background-color:#1F2937;   /* Dark Blue-Grey */
    color:white;
    padding:18px;
    border-radius:10px;
    text-align:center;
    font-size:36px;
    font-weight:700;
    margin-bottom:25px;
    white-space: nowrap;
}
</style>

<h1 class="header-title">Myntra Review Scrapper by Naman Nanda</h1>
""", unsafe_allow_html=True)


st.session_state["data"] = False


def form_input():
    product = st.text_input("Search Products")
    st.session_state[SESSION_PRODUCT_KEY] = product
    no_of_products = st.number_input("No of products to search",
                                     step=1,
                                     min_value=1)

    if st.button("Scrape Reviews"):
        scrapper = ScrapeReviews(
            product_name=product,
            no_of_products=int(no_of_products)
        )

        scrapped_data = scrapper.get_review_data()
        if scrapped_data is not None:
            st.session_state["data"] = True
            mongoio = MongoIO()
            mongoio.store_reviews(product_name=product,
                                  reviews=scrapped_data)
            print("Stored Data into mongodb")

        st.dataframe(scrapped_data)


if __name__ == "__main__":
    data = form_input()
