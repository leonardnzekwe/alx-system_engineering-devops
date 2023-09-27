# Using Puppet to Install Nginx Web Server and Configure it

# nginx_setup.pp

# Update package lists
exec { 'apt-update':
  command     => '/usr/bin/apt-get update',
  refreshonly => true,
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'], # Ensure update happens first
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Create parent directory /var/www
file { '/var/www':
  ensure => directory,
}

# Create the Nginx root HTML directory
file { '/var/www/html':
  ensure  => directory,
  require => File['/var/www'], # Ensure /var/www exists first
}

# Create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  content => "Hello World!\n",
  require => File['/var/www/html'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    server_name _;
    root /var/www/html;

    location / {
      index  index.html;
    }

    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
  }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
