repopack --include "src/Dockerfile,src/modify_settings.py"

docker build -f src/Dockerfile -t searxng . && docker run --rm -it -p 80:8080 searxng
