$(document).ready(function() {

    $('.urgpic,.lowinfo,.turpic,.turinfo,.oripic,.backbutton,.summtab,.luxicon,.oriicon,.ziggsicon,.oriinfo').hide()
    
    $('.low').click(function() {
    $('div.default h5').hide();
    $('.urgpic,.backbutton,.lowinfo').fadeIn('slow');
    $('.low,.turkey,.orianna,.summary').hide();});    
    
    $('.orianna').click(function() {
    $('div.default h5').hide();
    $('.oripic,.backbutton,.oriinfo').fadeIn('slow');
    $('.low,.turkey,.orianna,.summary').hide();});
    
    $('.turkey').click(function() {
    $('div.default h5').hide();
    $('.turpic,.backbutton,.turinfo').fadeIn('slow');
    $('.low,.turkey,.orianna,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.luxicon,.oriicon,.ziggsicon').fadeIn('slow');
    $('.low,.turkey,.orianna,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.urgpic,.lowinfo,.turpic,.turinfo,.oripic,.backbutton,.summtab,.luxicon,.oriicon,.ziggsicon,.oriinfo').hide()
    $('.low,.turkey,.orianna,.summary').fadeIn('slow');});})