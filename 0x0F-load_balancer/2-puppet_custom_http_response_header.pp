# Nginx Configuration Management

exec { 'apt_update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'present',
  require => Exec['apt_update'],
}

file_line { 'add_header':
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'server_name _',
  line    => "\tadd_header X-Served-By \"${::hostname}\";",
  require => Package['nginx'],
}

exec { 'nginx_restart':
  command   => '/usr/sbin/service nginx restart',
  subscribe => File_line['add_header'],
}
