# Installing flask from pip3
package {'python3':
  ensure => 'installed',
}

package {'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip'
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
