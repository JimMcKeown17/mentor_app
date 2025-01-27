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

schools = [
    "Holy Name Community",
    "Linge Tots",
    "Little Angels Unite",
    "Ekhaya",
    "Future Kids Educare",
    "Nolundi",
    "Nomonde",
    "Arise and Shine",
    "Early Rose",
    "Njongozabantu",
    "Nontsapho",
    "Dorcas Educare Centre",
    "Lukhanyiso",
    "Thandi's Educare & Aftercare",
    "Kings and Quuens",
    "Libhongo Lwethu",
    "Entokozweni EduCare",
    "Luv Birds Day care",
    "Kwakhanya",
    "Nosandla Educare",
    "Sakhuxolo Educare",
    "Umzam'omhle Educare",
    "Busy Bee",
    "Vulithemba",
    "Good Hope",
    "Sekunjalo EduCentre",
    "Sunnyside",
    "Nelisa",
    "Rock of Ages",
    "Sikhulise Pre-School",
    "Twinkle toes Educare",
    "Yomelela EduCare",
    "Cuttee Babies Nursery",
    "P.G Mangqana Pre-School",
    "Aaron Gqadu",
    "Adcoc Brighton kids",
    "Bambino",
    "Bavumeleni",
    "Bomi obutsha",
    "Bright Angels",
    "Charles Duna",
    "Dorothy",
    "Ezibeleni",
    "Future Angels",
    "Future Stars",
    "Govan Mbeki",
    "Green Apple",
    "Hlumelo",
    "Ikamvalethu",
    "Ilithalethu",
    "Isizwe Sethu",
    "Jesus Dominion",
    "Jongilanga",
    "Khazimla",
    "Kids College",
    "Kokkewiet",
    "Lithemba",
    "Little Ships",
    "Living Ubuntu",
    "Lukhanyiselo",
    "Malikhanye Day Care",
    "Minnie Day Care",
    "Msobomvu Pre-School",
    "Mzamomhle Edu-care",
    "Nceduluntu Edu-care",
    "New Brighton Future Kids",
    "Nobandla",
    "Noluthando",
    "Nonkqubela",
    "Paulos Oyigcwele",
    "Qaqawuli Godolozi",
    "Sakha Abantwana",
    "Seyisi",
    "Sifunimfundo",
    "Simanye",
    "Sinethemba",
    "Sisonke",
    "Siyabulela",
    "Siyazama",
    "St Magdalene",
    "Thanda Abantwana",
    "Tinky Winky Day Care",
    "Vukani Daycare",
    "Zizamele",
    "Zukhanye",
    "Aaron Gqadu",
    "Charles Duna",
    "Seyisi",
    "Astra",
    "Ben Sinuka",
    "Bethelsdorp",
    "BJ Mnyanda",
    "Clarkson",
    "Ebongweni",
    "Empumalanga",
    "Fumisukoma",
    "Isaac Booi",
    "Elufefeni",
    "Dumani",
    "Kama",
    "Khanyisa",
    "KK Ncwana",
    "Kroneberg",
    "Mboniselo",
    "Melisizwe",
    "Molefe",
    "Mzingisi",
    "Phakamile",
    "Sandwater",
    "St Augustines",
    "Zukisa",
    "Canzibe",
    "Cebelihle",
    "Daniels Public",
    "David Vuku",
    "Emafini Primary",
    "Emfundweni",
    "Emsengeni",
    "Emzomncane",
    "Gertrude Shope",
    "KwaNoXolo",
    "Mzimhlophe",
    "Ntyatyambo",
    "Sivuyiseni",
    "Spencer Mabija",
    "Stephen Mazungula",
    "Jarvis Gqamlana",
    "Lamani Primary School",
]

mentors = ["Babalo", "Buyi", "Chombe", "Faith", "Fiks", "Sibongile", "Suthukazi", "Zama", "Ziyanda", "Zolani"]

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
    mentor_name = st.selectbox("Mentor Name", mentors)

    # Date
    visit_date = st.date_input("Date", datetime.date.today())

    # School Visited
    # You can expand this list as needed; “Other” reveals a text box.
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
