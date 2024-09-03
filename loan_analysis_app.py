import streamlit as st
import pickle
# Title of the app
st.title("Loan Risk Analysis")

model = pickle.load(open("model.pkl", "rb"))

# Input fields for user to provide parameters
credit_lines_outstanding = st.number_input("Credit Lines Outstanding", min_value=0, format="%d")
loan_amt_outstanding = st.number_input("Loan Amount Outstanding", min_value=0.0, format="%.2f")
total_debt_outstanding = st.number_input("Total Debt Outstanding", min_value=0.0, format="%.2f")
income = st.number_input("Income", min_value=0.0, format="%.2f")
years_employed = st.number_input("Years Employed", min_value=0, format="%d")
fico_score = st.number_input("FICO Score", min_value=300, max_value=850, format="%d")

# Button to trigger analysis
if st.button("Analyze"):
    model_input = np.array([[credit_lines_outstanding, loan_amt_outstanding, total_debt_outstanding, income, years_employed, fico_score]])
    print("Model input:", model_input)  # Debugging: Print the model input

    prediction = model.predict(model_input)
    print("Prediction:", prediction)  # Debugging: Print the prediction result
    # Display the input data
    st.write("### Input Data:")
    st.write(f"Credit Lines Outstanding: {credit_lines_outstanding}")
    st.write(f"Loan Amount Outstanding: {loan_amt_outstanding}")
    st.write(f"Total Debt Outstanding: {total_debt_outstanding}")
    st.write(f"Income: {income}")
    st.write(f"Years Employed: {years_employed}")
    st.write(f"FICO Score: {fico_score}")

    # Show the risk message with red alerting text
    st.markdown("<h2 style='color: red;'>High risk of not paying loan</h2>", unsafe_allow_html=True)
