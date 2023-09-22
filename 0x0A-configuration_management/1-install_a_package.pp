# Using Puppet, install flask from pip3
package { 'Flask':
  ensure   => '2.1.0', # ensure flask installation version
  provider => 'pip3', # flask to be installed from pip3
}
