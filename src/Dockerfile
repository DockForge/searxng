# Use the official SearXNG image as the base
FROM searxng/searxng:latest AS builder

# Set the working directory to where the settings.yml is located
WORKDIR /usr/local/searxng

# Install pyyaml using Alpine's package manager (apk) to handle YAML modifications
RUN apk add --no-cache py3-yaml

# Add the Python script to modify the settings.yml file
COPY modify_settings.py /usr/local/bin/modify_settings.py

# Run the Python script to modify settings.yml
RUN python3 /usr/local/bin/modify_settings.py

# Final stage: use the original SearXNG image and copy only the modified settings.yml
FROM searxng/searxng:latest

# Set the working directory to where the settings.yml is located
WORKDIR /usr/local/searxng

# Copy only the modified settings.yml from the builder stage
COPY --from=builder /usr/local/searxng/searx/settings.yml /usr/local/searxng/searx/settings.yml

# Expose the required port (default 8080)
EXPOSE 8080

# Keep the original entrypoint from the base image
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/searxng/dockerfiles/docker-entrypoint.sh"]
