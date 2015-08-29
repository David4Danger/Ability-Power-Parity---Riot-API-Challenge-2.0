$(document).ready(function() {

    $('.korpic,.korinfo,.rumpic,.backbutton,.summtab,.mordicon,.eliseicon,.vladicon,.ruminfo').hide()

    $('.rumble').click(function() {
    $('div.default h5').hide();
    $('.rumpic,.backbutton,.ruminfo').fadeIn('slow');
    $('.korea,.rumble,.summary').hide();});
    
    $('.korea').click(function() {
    $('div.default h5').hide();
    $('.korpic,.backbutton,.korinfo').fadeIn('slow');
    $('.korea,.rumble,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.mordicon,.eliseicon,.vladicon').fadeIn('slow');
    $('.korea,.rumble,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.korpic,.korinfo,.rumpic,.backbutton,.summtab,.mordicon,.eliseicon,.vladicon,.ruminfo').hide()
    $('.korea,.rumble,.summary').fadeIn('slow');});})