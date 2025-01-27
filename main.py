import streamlit as st
import datetime
from pyairtable import Table

# -- Set up your Airtable credentials in Streamlit Secrets --
# You can add them via the Streamlit web interface or a .streamlit/secrets.toml file.
# st.secrets["AIRTABLE_API_KEY"]
# st.secrets["AIRTABLE_BASE_ID"]
# st.secrets["AIRTABLE_TABLE_NAME"]

# Example structure of secrets.toml:
# [AIRTABLE]
# API_KEY = "your_airtable_key"
# BASE_ID = "appYourBaseID"
# TABLE_NAME = "MentorVisits"

def save_to_airtable(data: dict):
    """Save the given data dictionary to Airtable."""
    table = Table(
        st.secrets["AIRTABLE"]["API_KEY"],
        st.secrets["AIRTABLE"]["BASE_ID"],
        st.secrets["AIRTABLE"]["TABLE_NAME"],
    )
    return table.create(data)


def main():
    st.title("Mentor Visit Tracker")
    st.write("Record details about your school visit")

    # Mentor Name
    mentor_name = st.selectbox("Mentor Name", ["Fiks", "Chombe", "Zama", "Buyiswa"])

    # Date
    visit_date = st.date_input("Date", datetime.date.today())

    # School Visited
    # You can expand this list as needed; “Other” reveals a text box.
    schools = ["School A", "School B", "School C", "Other"]
    selected_school = st.selectbox("School Visited", schools)
    if selected_school == "Other":
        custom_school = st.text_input("Enter the school's name")
        if custom_school.strip():
            selected_school = custom_school.strip()

    # Programme (changes questions below if needed)
    programme = st.selectbox("Programme", ["Literacy", "Zazi iZandi"])

    if programme == "Literacy":
        q1 = st.checkbox("Are LC's using their Letter Trackers correctly?")
        q2 = st.checkbox("Are LC's using their Session Trackers correctly?")
        q3 = st.checkbox("Are LC's completing back-of-book admin correctly??")
    elif programme == "Zazi iZandi":
        q4 = st.checkbox("Are LC's using their Letter Trackers correctly?")
        q5 = st.checkbox("Do the LC's groups look correct?")
        q6 = st.checkbox("Are LC's completing their admin correctly??")


    # Quality of Sessions (slider 1-10)
    quality = st.slider("Quality of Sessions", 1, 10, 5)

    # “Any Supplies Needed” and “Commentary”
    # (If you truly want checkboxes, adjust accordingly, but typically these are text areas.)
    supplies = st.text_area("Any Supplies Needed")
    commentary = st.text_area("Commentary")

    # Button to Save Record
    if st.button("Save Visit Record"):
        # Build dictionary for Airtable
        if programme == "Literacy":
            data = {
                "Mentor Name": mentor_name,
                "Date": visit_date.isoformat(),
                "School Visited": selected_school,
                "Programme": programme,
                "Using Letter Trackers": q1,
                "Using Session Trackers": q2,
                "Completing Admin": q3,
                "Quality of Sessions": quality,
                "Supplies Needed": supplies,
                "Commentary": commentary,
            }
        elif programme == "Zazi iZandi":
            data = {
                "Mentor Name": mentor_name,
                "Date": visit_date.isoformat(),
                "School Visited": selected_school,
                "Programme": programme,
                "Using Letter Trackers": q4,
                "Groups_Correct": q5,
                "Completing Admin": q6,
                "Quality of Sessions": quality,
                "Supplies Needed": supplies,
                "Commentary": commentary,
            }

        try:
            record = save_to_airtable(data)
            st.success("Visit record saved successfully!")
            # st.json(record)
        except Exception as e:
            st.error(f"Failed to save record: {e}")


if __name__ == "__main__":
    main()
