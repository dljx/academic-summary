import streamlit as st
from vertexai.preview.language_models import TextGenerationModel
import vertexai

PROJECT_ID = st.session_state['PROJECT_ID']


# Initialize st.session_state['text'] if not already initialized
if 'text' not in st.session_state:
    st.session_state['text'] = ""

with st.sidebar:
    st.title('Model and Parameters')

# Use st.sidebar.selectbox directly
selected_model = 'text-bison'

# Default parameter values
default_temperature = 0.0
default_token_limit = 1024
default_top_k = 40
default_top_p = 0.95

# Use st.sidebar.expander for the advanced settings
with st.sidebar.expander("Settings", expanded=True):
    # Use st.sidebar.slider directly
    input_temperature = st.slider('Temperature', min_value=0.0,
                                  max_value=1.0, value=default_temperature, step=0.1)

    # Use st.sidebar.slider directly
    input_token_limit = st.slider('Token Limit', min_value=1,
                                  max_value=1024, value=default_token_limit, step=8)

    # Use st.sidebar.slider directly
    input_top_k = st.slider('Top K', min_value=1, max_value=40,
                            value=default_top_k, step=1)

    # Use st.sidebar.slider directly
    input_top_p = st.slider('Top P', min_value=0.0, max_value=1.0,
                            value=default_top_p, step=0.01)

# Display the current parameter values (for testing purposes)
st.write("Current Model: ", selected_model)
st.write("Current Temperature:", input_temperature)
st.write("Current Token Limit:", input_token_limit)
st.write("Current Top K:", input_top_k)
st.write("Current Top P:", input_top_p)

# Save the variables to session state
st.session_state['PROJECT_ID'] = PROJECT_ID
st.session_state['input_temperature'] = input_temperature
st.session_state['input_token_limit'] = input_token_limit
st.session_state['input_top_k'] = input_top_k
st.session_state['input_top_p'] = input_top_p



def predict_large_language_model_sample(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: str,
    tuned_model_name: str = "",
):
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
        model = model.get_tuned_model(tuned_model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,)
    # print(f"Response from Model: {response.text}")
    return response.text


prompt1 = st.text_area(
    label="Enter your prompt",
    value="Please provide a concise summary of the following academic paper, highlighting the key findings, methods, and conclusions:\n\n"
    + st.session_state['text'],
    height=200  # Set the desired height
)

if st.button("Generate Summary"):
    # Update selected_model in session state
    st.session_state['selected_model'] = selected_model

    # Call the prediction function
    caption = predict_large_language_model_sample(
        st.session_state['PROJECT_ID'], selected_model, input_temperature, input_token_limit, input_top_p, input_top_k, prompt1)

    # Display the caption
    st.session_state['caption'] = caption
    st.text_area(label="Summary", value=caption, height=350)
    st.session_state['caption'] = caption