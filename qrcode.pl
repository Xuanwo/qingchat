#!/usr/bin/env perl
use Mojolicious::Lite;

#push @{app->static->paths}, 'E:/portablePerl';

get '/' => sub {
  my $c = shift;
  $c->reply->static('qrcode.jpg');
};

app->start('daemon', '-l', 'http://*:8080');