import joblib
import streamlit as st
import streamlit_authenticator as stauth


class detect :
    def main():
        file_name = "finalized_model.sav"
        loaded_model = joblib.load(file_name)

        st.title("Depression Detection And Management System")
        # st.header("Depression Detection And Management System")

        st.markdown("Hey, Tell me how you're feeling today")

        # removing the streamlit banner at the bottom
        hide_streamlit_style = """
                    <style>
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        st.text_input("Text", key="user_text")

        # You can access the value at any point with:
        text = st.session_state.user_text
        print(text)
        result = loaded_model.predict([text])

                

        def specialist() :
            specialists = [
            {"Name": "John Smith", "Gender": "Male", "Age": "25", "Phone Number": "08126259023", "Status": "Available"},
            {"Name": "Cheryl Wilson", "Gender": "Female", "Age": "58", "Phone Number": "08127299093", "Status": "Unavailable"},
            {"Name": "Jackie Chan", "Gender": "Male", "Age": "82", "Phone Number": "08099876530", "Status": "Available"},
            {"Name": "Aderibigbe Samuel", "Gender": "Male", "Age": "53", "Phone Number": "08121819026", "Status": "Unavailable"},
            {"Name": "MaryAnne Gabriella", "Gender": "Female", "Age": "27", "Phone Number": "08145659473", "Status": "Available"}
            ]

            if st.checkbox("View Available Specialists"):
                st.write("**Available Specialists**:")
                for idx, specialist in enumerate(specialists):
                    # Check if the specialist is available
                    if specialist["Status"] == "Available":
                        # Use a collapsible expander for each specialist's details
                        with st.expander(f"Specialist {idx + 1}: {specialist['Name']}"):
                            st.write("Name:", specialist["Name"])
                            st.write("Gender:", specialist["Gender"])
                            st.write("Age:", specialist["Age"])
                            st.write("Phone Number:", specialist["Phone Number"])
                            st.write("Status:", specialist["Status"])



        if len(text.split()) > 2:
            if (result[0] == "suicide"):
                prediction = "Depressed"
                            
                        
            else:
                prediction = "Not Depressed"

        else: prediction = "Please express your feelings with more than two words"
        
        
        # Define the PHQ-9 questions and scoring options
        questions = [
            "Little interest or pleasure in doing things",
            "Feeling down, depressed, or hopeless",
            "Trouble falling or staying asleep, or sleeping too much",
            "Feeling tired or having little energy",
            "Poor appetite or overeating",
            "Feeling bad about yourself – or that you are a failure or have let yourself or your family down",
            "Trouble concentrating on things, such as reading the newspaper or watching television",
            "Moving or speaking so slowly that other people could have noticed. Or the opposite – being so fidgety or restless that you have been moving around a lot more than usual",
            "Thoughts that you would be better off dead or of hurting yourself in some way"
        ]

        # Define scoring options (0 - 3)
        options = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
        scores = [0, 1, 2, 3]

        # Display app title
        st.title("PHQ-9 Depression Questionnaire")

        # Introduction text
        st.write("Answer the following questions to help assess your current mood. "
                "This assessment is based on the PHQ-9 questionnaire.")

        # Start form for user input
        with st.form("phq9_form"):
            st.write("Please select how often you've been bothered by the following problems over the past two weeks.")

            # Create variables for each question and store user input
            user_scores = []
            for i, question in enumerate(questions):
                choice = st.radio(f"{i+1}. {question}", options, key=f"q{i}")
                score = scores[options.index(choice)]
                user_scores.append(score)
            
            # Form submission
            submitted = st.form_submit_button("Submit")

        # Calculate the total score and make predictions
        total_score = sum(user_scores)
        
        if submitted:            
            # Interpretation of score based on PHQ-9 scoring guidelines
            if total_score >= 20:
                if prediction == "Depressed":
                    st.write("Based on your answers to both the text prompt and the questionnaire, **Prediction:** Severe depression")
                else:
                    st.write("Your answers to the text prompt suggested you are not depressed but your answers to the questionnaire suggest: Severe depression \n Please see a Specialist")
            elif total_score >= 15:
                if prediction == "Depressed":
                    st.write("Based on your answers to both the text prompt and the questionnaire, **Interpretation:** Moderately severe depression")
                else:
                    st.write("Your answers to the text prompt suggested you are not depressed but your answers to the questionnaire suggest:Moderately severe depression \n Please see a Specialist")
            elif total_score >= 10:
                if prediction == "Depressed":
                    st.write("Based on your answers to both the text prompt and the questionnaire, **Interpretation:** Moderate depression")
                else:
                    st.write("Your answers to the text prompt suggested you are not depressed but your answers to the questionnaire suggest:Moderate depression \n Please see a Specialist")
            elif total_score >= 5:
                if prediction == "Depressed":
                    st.write("Based on your answers to both the text prompt and the questionnaire, **Interpretation:** Mild depression")
                else:
                    st.write("Your answers to the text prompt suggested you are not depressed but your answers to the questionnaire suggest:Mild depression \n Please see a Specialist")
            else:
                if prediction == "Depressed":
                    st.write("Your answer to the text prompt suggested that you might be depressed but your answers to the questionnaire suggested otherwise, Please see a Specialist for further diagnosis")
                else:
                    st.write("Your answers to the text prompt suggested you are not depressed and your answers to the questionnaire confirmed it \n Do continue to have a lovely day")

        if total_score >= 5 or prediction == "Depressed" :          
            specialist()
           
        # Further steps or advice
        st.write("Note: This tool is a screening aid, not a diagnostic tool. Please consult a healthcare provider for a full assessment.")

# Run `python -m streamlit run stream.py`
# to run the file
