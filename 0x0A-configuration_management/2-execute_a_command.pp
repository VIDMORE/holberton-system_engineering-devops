# Kill a process called killmenow

exec { 'pkill killmenow':
  path    => '/usr/bin/'
}
