FROM ubuntu

# Install python and pip
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# Create app directory
RUN mkdir /api/

# Copy files into app directory
COPY . /api/

# Install packages
RUN pip install --no-cache-dir -r /api/requirements.txt

# Assign work directory
WORKDIR /api

#Expose port 4000
EXPOSE 4000

# Start API
CMD ["/bin/sh", "-c", "python3 main.py"]
