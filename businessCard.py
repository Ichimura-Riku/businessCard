import streamlit as st
from PIL import Image

image_ichimura = Image.open('businessCard_ichimura.png')

st.image(image_ichimura, use_column_width=True)

markdown_ichimura = """
    [@shiosioco40](https://twitter.com/shiosioco40)

    [Ichimura-Riku](https://github.com/Ichimura-Riku)
"""

st.markdown(markdown_ichimura)

# link_twitter = '[<span class="hljs-string">@shiosioco40</span>](<span class="hljs-link">https://twitter.com/shiosioco40</span>)'
# st.sidebar.markdown(link_twitter, unsafe<span class="hljs-emphasis">_allow_</span>html=True)


# link_github = '[<span class="hljs-string">@Ichimura-Riku</span>](<span class="hljs-link">https://github.com/Ichimura-Riku</span>)'
# st.sidebar.markdown(link_github, unsafe<span class="hljs-emphasis">_allow_</span>html=True)

image_katsuki = Image.open('businessCard_katsuki.png')

st.image(image_katsuki, use_column_width=True)

markdown_katsuki = """
    [Taka1304](https://github.com/Taka1304)
"""

st.markdown(markdown_katsuki)



# link_github = '[<span class="hljs-string">@Taka1304</span>](<span class="hljs-link">https://github.com/Taka1304</span>)'
# st.sidebar.markdown(link_github, unsafe<span class="hljs-emphasis">_allow_</span>html=True)
