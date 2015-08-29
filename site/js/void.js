$(document).ready(function() {

    $('.backbutton,.summtab,.ahriicon,.annieicon,.luxicon').hide()
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.ahriicon,.annieicon,.luxicon').fadeIn('slow');
    $('.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.backbutton,.summtab,.ahriicon,.annieicon,.luxicon').hide()
    $('.summary').fadeIn('slow');});})