FROM python:3.9-slim

# Set the working directory
WORKDIR /

# Copy source code to the working directory
COPY . /

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Command to run your Streamlit application
CMD ["streamlit", "run", "loan_analysis_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
