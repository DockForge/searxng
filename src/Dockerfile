# Use the official SearXNG image as the base
FROM searxng/searxng:latest

# Set the working directory to where the settings.yml is located
WORKDIR /usr/local/searxng

# Install pyyaml using Alpine's package manager (apk)
RUN apk add --no-cache py3-yaml

# Add the Python script to modify the settings.yml file
COPY modify_settings.py /usr/local/bin/modify_settings.py

# Run the Python script during the build process to modify the settings.yml
RUN python3 /usr/local/bin/modify_settings.py

# Expose the required port (default 8080)
EXPOSE 8080

# Keep the original entrypoint from the base image
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/searxng/dockerfiles/docker-entrypoint.sh"]
