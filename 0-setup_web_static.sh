#!/usr/bin/env bash
# script to that setup web server for deployment

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
	    sudo apt-get update
	        sudo apt-get install -y nginx
fi

# Define directories
data_dir="/data"
web_static_dir="$data_dir/web_static"
releases_dir="$web_static_dir/releases"
shared_dir="$web_static_dir/shared"
test_release_dir="$releases_dir/test"
html_file="$test_release_dir/index.html"
current_link="$web_static_dir/current"

# Create necessary directories if they don't exist
sudo mkdir -p "$data_dir" "$web_static_dir" "$releases_dir" "$shared_dir" "$test_release_dir"
sudo touch "$html_file"

# Create fake HTML file for testing
echo "<html>
<head>
</head>
<body>
    Holberton School
    </body>
    </html>" | sudo tee "$html_file"

    # Ensure symbolic link exists and points to the test release directory
    sudo ln -sf "$test_release_dir" "$current_link"

    # Set ownership recursively
    sudo chown -R ubuntu:ubuntu "$data_dir"

    # Update Nginx configuration
    nginx_config="/etc/nginx/sites-enabled/default"
    sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' "$nginx_config"

    # Restart Nginx
    sudo service nginx restart

    # Exit successfully
    exit 0
