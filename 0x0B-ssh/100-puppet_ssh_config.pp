#!/usr/bin/env bash
# Using Puppet to create client configuration file

file_line {'Ascertain the config file contains the identity file config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

file_line {'Ascertain the config file contains the pass_auth set to no':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
