# Execute a command

exec { 'Kill-me-now':
  command => 'pkill -9 -f killmenow',
  path    => '/usr/bin',
}
