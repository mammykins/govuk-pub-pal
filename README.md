# GOV.UK-ify Text LangChain-Streamlit Example

This repo serves as a template for how to make your own LangChain apps on Streamlit.

This app was inspired by and draws heavily from this YouTube video: https://www.youtube.com/watch?v=U_eV8wfMkXU.  

You can also review their [GitHub code](https://github.com/gkamradt/globalize-text-streamlit).  

## Setup

We used python 3.11.0 to build this app.

Setup a virtual environment and activate it. 

Run `pip install -r requirements.txt` to install the required packages. 


## Deploy on Streamlit

This app is meant to be deployed on [Streamlit](https://streamlit.io/).
Note that when setting up your StreamLit app you should make sure to add `OPENAI_API_KEY` as a secret environment variable.

## OPENAI_API_KEY

You can also paste your OPENAI_API_KEY into the Streamlit app if you find setting variables finnicky.