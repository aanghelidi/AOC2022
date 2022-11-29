#!/usr/bin/perl

use strict;
use warnings;
use v5.34;
use File::Path qw(make_path);

# Check number of arguments
my $number_args = $#ARGV + 1;
if ( $number_args == 0 ) {
    say "AOC Perl setup script that perform the following actions:";
    say "- create a new directory for the choosen puzzle";
    say "- download the corresponding input";
    say "- open puzzle in nvim\n";
    say "Usage: ./setup.pl 1 2022 main.pl\n";
}

# Check day
if ( $ARGV[0] < 1 or $ARGV[0] > 25 ) {
    say "Day should be greater or equal than 1 and less than or equal to 25!";
}

# Create directory if not exists
make_path( $ARGV[1] . "/day" . $ARGV[0] );

# Check $AOC_SESSION token and download input
if ( defined $ENV{"AOC_SESSION"} ) {
    my $url =
      "https://adventofcode.com/" . $ARGV[1] . "/day/" . $ARGV[0] . "/input";
    say "Downloading $url ...";
    system "curl", "-b", "session=" . $ENV{"AOC_SESSION"}, "-o",
      $ARGV[1] . "/day" . $ARGV[0] . "/input.txt", $url;
    say "Done !";
}
else {
    say "AOC_SESSION not set up!";
    say "Will not download problem input!";
    exit 1;
}

# Change directory
chdir( $ARGV[1] . "/day" . $ARGV[0] );

# Open file in vim
exec "nvim", $ARGV[2];
