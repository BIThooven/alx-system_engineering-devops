# ssh config to connect to a server without a password using Puppet
include stdlib

file_line { 'PasswordAuthentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
file_line {'IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}
