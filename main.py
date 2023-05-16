import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
       Below is a GOV.UK web page written in markdown by a content designer.
    You are an expert in writing content for GOV.UK and your goal is to:
    - Properly format the page
    - Follow the Government Digital Service (GDS) style guide and writing guidance
    - Be specific and concise
    - Use short sentences
    - Use a simple vocabulary

    Below is the content's tone, and the user intention you are writing for:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR {dialect} RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template,
)


def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm


st.set_page_config(page_title="GOV.UK Publishing Pal", page_icon=":robot:")
st.header("GOV.UK Publishing Pal")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Generative Large Language Models have been shown to assist with writing content. \n\n"
                "Perhaps this technology has a role to play in helping produce initial drafts of GOV.UK content? \n\n "

                "This demo uses prompt engineering to modify content to be more GOV.UK-like. Fine tuning a "
                "open-source model on more GOV.UK content could produce better results \n\n"
                )

with col2:
    st.image(image='govuk.png', width=500)

st.markdown("## Enter Your Text To GOV.UK-ify")


def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ", placeholder="Ex: sk-2twmA8tfCb8un4...",
                               key="openai_api_key_input")
    return input_text


openai_api_key = get_api_key()

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'Which tone would you like your content to have?',
        ('GOV.UK', 'Informal', 'Formal'))

with col2:
    option_dialect = st.selectbox(
        'Which user group are you writing for?',
        ('People who need to do a thing', 'People who need to find some information'))


def get_text():
    input_text = st.text_area(label="Email Input", label_visibility='collapsed', placeholder="Your Email...",
                              key="email_input")
    return input_text


email_input = get_text()

if len(email_input.split(" ")) > 700:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()


def update_text_with_example():
    print("in updated")
    st.session_state.email_input = "# cost o' living crisis!!!!  ## Overview  A page of useful info.  ## Check 'elp " \
                                   "you can get  Answe a few questions and try this link " \
                                   "https://www.gov.uk/check-benefits-financial-support  ## Scams  don't trust people " \
                                   "who ring and say they are government, they're not!"


st.button("*See An Example*", type='secondary', help="Click to see an example of the content you will be converting.",
          on_click=update_text_with_example)

st.markdown("### Your Converted Content:")

if email_input:
    if not openai_api_key:
        st.warning(
            'Please insert OpenAI API Key. Instructions [here]('
            'https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)',
            icon="⚠️")
        st.stop()

    llm = load_LLM(openai_api_key=openai_api_key)

    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)

    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)
