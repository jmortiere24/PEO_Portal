import streamlit as st

# Set page config
st.set_page_config(page_title="PEO Client Portal", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "HR Tools", "Compliance Hub", "Case Management"])

def dashboard():
    st.title("Hello, Jane")
    st.write("Here's what we have for you today.")

    # Article cards
    st.subheader("Monthly Compliance Highlights")
    st.write("A quick roundup of policy changes, upcoming deadlines, and best practices to keep your business compliant.")
    st.markdown("**Read article** | Loki Bright | Oct 19, 2021 • 5min read")
    st.subheader("Payroll & Compliance Updates")
    st.write("Quis neque, eu et ipsum amet, vel et. Varius integer enim pellentesque ornare pharetra faucibus arcu. Mauris blandit egestas nibh.")
    st.markdown("**Read article** | Loki Bright | Oct 19, 2021 • 5min read")
    st.subheader("HR Tips & Deadlines You Should Know")
    st.write("Quis neque, eu et ipsum amet, vel et. Varius integer enim pellentesque ornare pharetra faucibus arcu. Mauris blandit egestas nibh.")
    st.markdown("**Read article** | Loki Bright | Oct 19, 2021 • 5min read")

    # HR Tools quick access
    st.subheader("HR Tools")
    st.write("Access your payroll and employee management platform directly from here.")
    st.button("Open HR System")

    # External Tools
    st.subheader("External Tools")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Tool 1**\nGet the latest updates about Designership's new features and product updates.")
        st.button("Visit Site", key="tool1")
    with col2:
        st.write("**Tool 2**\nGet the latest updates about Designership's new features and product updates.")
        st.button("Visit Site", key="tool2")
    with col3:
        st.write("**Tool 3**\nGet the latest updates about Designership's new features and product updates.")
        st.button("Visit Site", key="tool3")

    # Key Contacts
    st.subheader("Key Contacts - Your OneDigital Support Team")
    st.write("**Name:** Taylor Scott  |  **Role:** Payroll & HR Specialist  |  **Email:** taylor.scott@onedigital.com  |  **Phone:** (123) 456-7890")
    st.write("**Name:** Jamie Rivera  |  **Role:** Compliance Advisor  |  **Email:** jamie.rivera@onedigital.com  |  **Phone:** (123) 555-2345")

def hr_tools():
    st.title("HR Tools")
    st.write("Access payroll and employee management tools here. (Placeholder)")

def compliance_hub():
    st.title("Compliance Hub")
    st.write("Find the latest HR, tax, and labor law requirements specific to your state. Select a state to view resources and regulations that apply to your business.")
    st.write("(Interactive US map and state-specific info would go here.)")
    st.write("Example: Select 'Alabama' to see compliance topics like Emergency Response Leave, Family and Medical Leave, etc.")

def case_management():
    st.title("Submit a Request")
    st.write("Use this form to request support from the OneDigital PEO team. Your case will be routed based on the selected request type.")
    request_types = [
        "Plan/Employer", "Complete Retirement Solution Implementation", "Education Meeting", "Fund Change", "Internal VM Changes", "Internal/Compliance", "Marketing Services", "Onboarding/Terminations", "Participant", "RPS Client Conversions", "Trade Error or Incident", "VM Prospect Paperwork", "VM Service Request"
    ]
    request_type = st.selectbox("Request Type", request_types)
    contact_name = st.text_input("Contact Name")
    email = st.text_input("Email")
    description = st.text_area("Description")
    if st.button("Submit"):
        st.success("Request submitted!")

# Page routing
if page == "Dashboard":
    dashboard()
elif page == "HR Tools":
    hr_tools()
elif page == "Compliance Hub":
    compliance_hub()
elif page == "Case Management":
    case_management()
