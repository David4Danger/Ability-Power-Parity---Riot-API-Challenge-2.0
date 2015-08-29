$(document).ready(function() {

    $('.rumblepic,.backbutton,.summtab,.eliseicon,.brandicon,.rumbleicon,.rumbleinfo').hide()

    $('.rumble').click(function() {
    $('div.default h5').hide();
    $('.rumblepic,.backbutton,.rumbleinfo').fadeIn('slow');
    $('.rumble,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.eliseicon,.brandicon,.rumbleicon').fadeIn('slow');
    $('.rumble,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.rumblepic,.backbutton,.summtab,.eliseicon,.brandicon,.rumbleicon,.rumbleinfo').hide()
    $('.rumble,.summary').fadeIn('slow');});})