$(document).ready(function() {

    $('.lulupic,.ahripic,.lebpic,.backbutton,.summtab,.ahriicon,.lebicon,.aziricon,.luluinfo,.ahriinfo,.lebinfo').hide()

    $('.lulu').click(function() {
    $('div.default h5').hide();
    $('.lulupic,.backbutton,.luluinfo').fadeIn('slow');
    $('.lulu,.ahri,.leblanc,.summary').hide();});
    
    $('.ahri').click(function() {
    $('div.default h5').hide();
    $('.ahripic,.backbutton,.ahriinfo').fadeIn('slow');
    $('.lulu,.ahri,.leblanc,.summary').hide();});
    
    $('.leblanc').click(function() {
    $('div.default h5').hide();
    $('.lebpic,.backbutton,.lebinfo').fadeIn('slow');
    $('.lulu,.ahri,.leblanc,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.ahriicon,.lebicon,.aziricon').fadeIn('slow');
    $('.lulu,.ahri,.leblanc,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.lulupic,.ahripic,.lebpic,.backbutton,.summtab,.ahriicon,.lebicon,.aziricon,.ahriinfo,.luluinfo,.lebinfo').hide()
    $('.lulu,.ahri,.leblanc,.summary').fadeIn('slow');});})