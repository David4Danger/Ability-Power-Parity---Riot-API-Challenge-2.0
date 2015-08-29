$(document).ready(function() {

    $('.ryzepic,.anivpic,.backbutton,.summtab,.anivicon,.oriicon,.cassicon,.ryzeinfo,.anivinfo').hide()

    $('.ryze').click(function() {
    $('div.default h5').hide();
    $('.ryzepic,.backbutton,.ryzeinfo').fadeIn('slow');
    $('.ryze,.anivia,.summary').hide();});
    
    $('.anivia').click(function() {
    $('div.default h5').hide();
    $('.anivpic,.backbutton,.anivinfo').fadeIn('slow');
    $('.ryze,.anivia,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.anivicon,.oriicon,.cassicon').fadeIn('slow');
    $('.ryze,.anivia,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.ryzepic,.anivpic,.backbutton,.summtab,.anivicon,.oriicon,.cassicon,.anivinfo,.ryzeinfo').hide()
    $('.ryze,.anivia,.summary').fadeIn('slow');});})