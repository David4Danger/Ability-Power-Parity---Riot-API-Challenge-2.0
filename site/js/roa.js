$(document).ready(function() {

    $('.korpic,.korinfo,.chopic,.anivpic,.karthuspic,.kasspic,.backbutton,.summtab,.choicon,.annieicon,.malzicon,.choinfo,.anivinfo,.kassinfo,.karthinfo').hide()

    $('.korea').click(function() {
    $('div.default h5').hide();
    $('.korpic,.backbutton,.korinfo').fadeIn('slow');
    $('.korea,.kassadin,.anivia,.karthus,.chogath,.summary').hide();});

    $('.chogath').click(function() {
    $('div.default h5').hide();
    $('.chopic,.backbutton,.choinfo').fadeIn('slow');
    $('.korea,.kassadin,.anivia,.karthus,.chogath,.summary').hide();});
    
    $('.anivia').click(function() {
    $('div.default h5').hide();
    $('.anivpic,.backbutton,.anivinfo').fadeIn('slow');
    $('.korea,.kassadin,.anivia,.karthus,.chogath,.summary').hide();});
    
    $('.karthus').click(function() {
    $('div.default h5').hide();
    $('.karthuspic,.backbutton,.karthinfo').fadeIn('slow');
    $('.korea,.kassadin,.anivia,.karthus,.chogath,.summary').hide();});
    
    $('.kassadin').click(function() {
    $('div.default h5').hide();
    $('.kasspic,.backbutton,.kassinfo').fadeIn('slow');
    $('.korea,.kassadin,.anivia,.karthus,.chogath,.summary').hide();});    
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.annieicon,.malzicon,.choicon').fadeIn('slow');
    $('.korea,.chogath,.anivia,.kassadin,.karthus,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.korpic,.korinfo,.karthuspic,.anivpic,.kasspic,.chopic,.backbutton,.summtab,.annieicon,.malzicon,.choicon,.anivinfo,.choinfo,.karthinfo,.kassinfo').hide()
    $('.korea,.kassadin,.anivia,.karthus,.chogath,.summary').fadeIn('slow');});})