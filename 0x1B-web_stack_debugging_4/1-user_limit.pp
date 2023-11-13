# Puppet Script to enable the user - holberton, to login and open files without error

# hard file limit increase for user - holberton
exec { 'hard-file-limit-increase':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Soft file limit increase for user - holberton
exec { 'soft-file-limit-increase':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
