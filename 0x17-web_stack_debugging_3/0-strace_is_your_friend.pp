# Puppet script that fixes the file  wp-settings.php by replacing .phpp with .php
exec { 'fix php':
  command     => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
