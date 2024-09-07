FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy source code to the working directory
COPY . /app

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 5000

# Command to run your Streamlit application
CMD ["streamlit", "run", "loan_analysis_app.py", "--server.port=5000", "--server.address=0.0.0.0"]
