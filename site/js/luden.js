$(document).ready(function() {

    $('.korpic,.korinfo,.kogpic,.ahripic,.syndpic,.lebpic,.katpic,.xerpic,.backbutton,.summtab,.ahriicon,.ekkoicon,.katicon,.katinfo,.lebinfo,.xerinfo,.koginfo,.ahriinfo,.syndinfo').hide()

    $('.korea').click(function() {
    $('div.default h5').hide();
    $('.korpic,.backbutton,.korinfo').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();});
    
    $('.kogmaw').click(function() {
    $('div.default h5').hide();
    $('.kogpic,.backbutton,.koginfo').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();});
    
    $('.ahri').click(function() {
    $('div.default h5').hide();
    $('.ahripic,.backbutton,.ahriinfo').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();});
    
    $('.syndra').click(function() {
    $('div.default h5').hide();
    $('.syndpic,.backbutton,.syndinfo').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();});
    
    $('.leblanc').click(function() {
    $('div.default h5').hide();
    $('.lebpic,.backbutton,.lebinfo').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();});
    
    $('.katarina').click(function() {
    $('div.default h5').hide();
    $('.katpic,.backbutton,.katinfo').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();});
    
    $('.xerath').click(function() {
    $('div.default h5').hide();
    $('.xerpic,.backbutton,.xerinfo').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.katicon,.ahriicon,.ekkoicon').fadeIn('slow');
    $('.korea,.kogmaw,.ahri,.syndra,.leblanc,.katarina,.xerath,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.korpic,.korinfo,.kogpic,.ahripic,.syndpic,.lebpic,.katpic,.xerpic,.backbutton,.summtab,.ahriicon,.ekkoicon,.katicon,.katinfo,.lebinfo,.xerinfo,.koginfo,.ahriinfo,.syndinfo').hide()
    $('.korea,.kogmaw,.ahri,.katarina,.leblanc,.xerath,.syndra,.summary').fadeIn('slow');});})