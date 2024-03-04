import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
    
# Load stored values from session state
PROJECT_ID = st.session_state.get("PROJECT_ID", "")

PROCESSOR_ID = st.session_state.get("PROCESSOR_ID", "")
LOCATION = st.session_state.get("LOCATION", "")

# Sidebar input fields
PROJECT_ID = st.sidebar.text_input(
    label="#### GCP PROJECT ID",
    placeholder="Paste your GCP Project ID",
    value=PROJECT_ID,
    type="default")


PROCESSOR_ID = st.sidebar.text_input(
    label="#### DocAI Processor ID",
    placeholder="Paste your DocAI Processor ID",
    value=PROCESSOR_ID,
    type="default")

LOCATION = st.sidebar.text_input(
    label="#### DocAI Location",
    placeholder="US/EU",
    value=LOCATION,
    type="default")

if LOCATION and LOCATION.lower() not in ['us', 'eu']:
    LOCATION = None
    st.sidebar.warning("Only US or EU allowed!")

# Check if LOCATION is not None before calling lower()
if LOCATION:
    LOCATION = LOCATION.lower()

# Button to submit the configuration in the sidebar
submit_button = st.sidebar.button("Save Configuration")

# Button to reset the browser in the sidebar
reset_button = st.sidebar.button("Reset Configuration")

if submit_button:
    if not PROJECT_ID and not PROCESSOR_ID and not LOCATION:
        st.sidebar.warning("Please fill up all the fields.", icon="⚠️")
    else:
        st.sidebar.success("Configuration Saved!")

if reset_button:
    PROJECT_ID = None

    PROCESSOR_ID = None
    LOCATION = None
    st.sidebar.success("Variables Cleared!")

# Store input values in session state
st.session_state['PROJECT_ID'] = PROJECT_ID

st.session_state['PROCESSOR_ID'] = PROCESSOR_ID
st.session_state['LOCATION'] = LOCATION

# Display values
st.write("#### GCP PROJECT ID")
if not PROJECT_ID:
    st.markdown(':red[*Not Configured*]')
else:
    st.text(PROJECT_ID)



st.write("#### DocAI Processor ID")
if not PROCESSOR_ID:
    st.markdown(':red[*Not Configured*]')
else:
    st.text(PROCESSOR_ID)

st.write("#### DocAI Location")
if not LOCATION:
    st.markdown(':red[*Not Configured*]')
else:
    st.text(LOCATION)
