# Puppet script to increase the amount of traffic an Nginx server can handle

# Default ULIMIT Increase
exec { 'default-ulimit-increase':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Nginx Restart
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
