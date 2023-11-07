# Puppet script to carry out substitution in a file on the server

$target_file = '/var/www/html/wp-settings.php'

#substitute "phpp" with "php"

exec { 'substitution':
  command => "sed -i 's/phpp/php/g' ${target_file}",
  path    => ['/bin','/usr/bin']
}
