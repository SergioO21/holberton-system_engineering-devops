# Set up your client SSH configuration file so that
# you can connect to a server without typing a password.

file_line { 'Remove authentications':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  match  => 'PasswordAuthentication no'
}

file_line { 'Use private key':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton'
}
