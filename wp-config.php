<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'grupo100' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '0D>nvC(,s1hvM=CUUJwd=}Q=`#@xbaaS$}`#/>Cp=WEk;{E;Q07T#g]$~,evTjMy' );
define( 'SECURE_AUTH_KEY',  'l_K+Yy$.GCa@9VxG{:1*9dQiQh4e]nbwj4nnra*9i&TPvk;d#sc/9%T5G%85`q3r' );
define( 'LOGGED_IN_KEY',    'c;eh!cx)/>e11=FX>1_pPJfn2IsU_A1+7@kij~GP1^j6X6i|sRPtG$bSnw^V?I/%' );
define( 'NONCE_KEY',        'WivwzBP!x%W{HCQ4;3F3MgvsSr:&NYi|{@/P>oq>@o?bgz58(&O5Ze4`aLe2zQ,.' );
define( 'AUTH_SALT',        'H=yR_#5cB]g2zz)d1%6tOE}L=&dh&x4OQ% = ^rH0@Ty%> Z^Q26Iqvmj9WjX^(A' );
define( 'SECURE_AUTH_SALT', '2!o)c]p_6|<,!w;-#K<dk:Q)T_FG+s)#&6>kzQUw|/x+c{)9%Qf<7X*g-Y(p9f^7' );
define( 'LOGGED_IN_SALT',   'iQ,p/BY!kj}C3VX1:yxO7Ox7NqM(<s;*K&y!5&vy%BV,3B7ND4)u2;;#RK/8.n0*' );
define( 'NONCE_SALT',       'MLy59Bx*yZnW~<5AJkpgOp-2g{w-L/#3?SxsKX{Q I4<%I&,[)_(V1`H^ob;#~AK' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
