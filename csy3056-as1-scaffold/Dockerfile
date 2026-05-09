FROM python:3.11-slim

# Sets the working directory in the container to /app
WORKDIR /app

# Tells Python where to find the project files when running pytest
ENV PYTHONPATH=/app

#Copies the current project into the container at /app
COPY . .

# Installs dependencies from requirements.txt
RUN pip install -r requirements.txt

# Runs pytest when the container starts and prints the results to the console
CMD ["python", "-m", "pytest"]