# Using Puppet, create a file 'school' in /tmp
file { '/tmp/school':
  ensure  => 'file', # ensure it's a file
  mode    => '0744', # set the file permission to 0744
  owner   => 'www-data', # set the file owner to www-data
  group   => 'www-data', # set the file group to www-data
  content => 'I love Puppet', # set the file content
}
