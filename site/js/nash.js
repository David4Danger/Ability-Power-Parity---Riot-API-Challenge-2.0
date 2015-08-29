$(document).ready(function() {

    $('.ruspic,.rusnash,.korpic,.kornash,.kaylepic,.azirpic,.backbutton,.summtab,.dianaicon,.kayleicon,.teemoicon,.kayleinfo,.azirinfo').hide()

    $('.kayle').click(function() {
    $('div.default h5').hide();
    $('.kaylepic,.backbutton,.kayleinfo').fadeIn('slow');
    $('.russia,.korea,.kayle,.azir,.summary').hide();});
    
    $('.azir').click(function() {
    $('div.default h5').hide();
    $('.azirpic,.backbutton,.azirinfo').fadeIn('slow');
    $('.russia,.korea,.kayle,.azir,.summary').hide();});
    
    $('.korea').click(function() {
    $('div.default h5').hide();
    $('.korpic,.backbutton,.kornash').fadeIn('slow');
    $('.russia,.korea,.kayle,.azir,.summary').hide();});
    
    $('.russia').click(function() {
    $('div.default h5').hide();
    $('.ruspic,.backbutton,.rusnash').fadeIn('slow');
    $('.russia,.korea,.kayle,.azir,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.dianaicon,.kayleicon,.teemoicon').fadeIn('slow');
    $('.russia,.korea,.kayle,.azir,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.ruspic,.rusnash,.korpic,.kornash,.kaylepic,.azirpic,.backbutton,.summtab,.dianaicon,.kayleicon,.teemoicon,.kayleinfo,.azirinfo').hide()
    $('.russia,.korea,.kayle,.azir,.summary').fadeIn('slow');});})