$(document).ready(function() {

    $('.vladpic,.backbutton,.summtab,.mordicon,.vladicon,.kennenicon,.vladinfo').hide()

    $('.vlad').click(function() {
    $('div.default h5').hide();
    $('.vladpic,.backbutton,.vladinfo').fadeIn('slow');
    $('.vlad,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.mordicon,.vladicon,.kennenicon').fadeIn('slow');
    $('.vlad,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.vladpic,.backbutton,.summtab,.mordicon,.vladicon,.kennenicon,.vladinfo').hide()
    $('.vlad,.summary').fadeIn('slow');});})