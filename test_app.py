from streamlit.testing.v1 import AppTest
import numpy as np
import pickle

# Assuming your app is defined in app.py
from loan_analysis_app import run_app


def test_loan_risk_analysis():
    # Initialize AppTest with a default timeout (in seconds)
    
    at = AppTest.from_file("loan_analysis_app.py")
    # Provide inputs
    at.run()
    at.number_input[0].set_value(1)  ##.set_value(5)
    at.number_input[1].set_value(5)  ##.value(10000.0)
    at.number_input[2].set_value(700)  ##.value(5000.0)
    at.number_input[3].set_value(3000)  ##.value(50000)
    at.number_input[4].set_value(5)  #.value(5)
    at.number_input[5].set_value(300)  #.value(700)
    # Click the Analyze button
    at.button[0].click().run()
    assert "Not a risk of missing loan payment" in at.markdown[0].value, "Low-risk case failed"
    
    at.run()
    at.number_input[0].set_value(10)  ##.set_value(5)
    at.number_input[1].set_value(1000)  ##.value(10000.0)
    at.number_input[2].set_value(1000)  ##.value(5000.0)
    at.number_input[3].set_value(1000)  ##.value(50000)
    at.number_input[4].set_value(5)  #.value(5)
    at.number_input[5].set_value(300)  #.value(700)
    # Click the Analyze button
    at.button[0].click().run()
    assert "High risk of not paying loan" in at.markdown[0].value,"High-risk case passed unexpectedly"
    



if __name__ == "__main__":
    test_loan_risk_analysis()
