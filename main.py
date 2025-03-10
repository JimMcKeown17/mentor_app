import streamlit as st
import datetime
from pyairtable import Table

# -- Set up your Airtable credentials in Streamlit Secrets --
# You can add them via the Streamlit web interface or a .streamlit/secrets.toml file.

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
    st.divider()
    st.subheader("Details of Visit")

    mentor_name = st.selectbox("Mentor Name", mentors)
    visit_date = st.date_input("Date", datetime.date.today())
    selected_school = st.selectbox("School Visited", schools)

    st.divider()
    st.subheader("Mentor Observations")

    q1 = st.checkbox("Are TA's using their Letter Trackers correctly?")
    q2 = st.checkbox("Do the TA's groups look correct?")
    q3 = st.checkbox("Are TA's completing their admin correctly?")

    quality = st.slider("Quality of Sessions Observed", 1, 10, 5)
    supplies = st.text_area("Any Supplies Needed")
    commentary = st.text_area("Commentary")

    if st.button("Save Visit Record"):
        data = {
            "Mentor Name": mentor_name,
            "Date": visit_date.isoformat(),
            "School Visited": selected_school,
            "Using Letter Trackers": q1,
            "Groups_Correct": q2,
            "Completing Admin": q3,
            "Quality of Sessions": quality,
            "Supplies Needed": supplies,
            "Commentary": commentary,
        }
        try:
            record = save_to_airtable(data)
            st.success("Visit record saved successfully!")
        except Exception as e:
            st.error(f"Failed to save record: {e}")


if __name__ == "__main__":
    main()
