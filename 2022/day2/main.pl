use strict;
use warnings;
use v5.34;

my $ans    = 0;
my $ans2   = 0;
my %wr     = qw(r p p s s r);
my %lr     = qw(r s p r s p);
my %scores = qw(r 1 p 2 s 3);

sub score {
    my $ws = 0;
    $_[0] eq $_[1] ? $ws += 3 : $wr{ $_[0] } eq $_[1] ? $ws += 6 : undef;
    return $scores{ $_[1] } + $ws;
}

sub score2 {
        $_[1] eq "r" ? return $scores{ $lr{ $_[0] } } + 0
      : $_[1] eq "p" ? return $scores{ $_[0] } + 3
      :                return $scores{ $wr{ $_[0] } } + 6;
}

open( my $f, "<", "input.txt" );
while (<$f>) {
    tr/XYZ/ABC/;
    tr/ABC/rps/;
    my ( $c, $s ) = split(/\s/);
    $ans  += score( $c, $s );
    $ans2 += score2( $c, $s );
}
say "Part 1: $ans";
say "Part 2: $ans2";
