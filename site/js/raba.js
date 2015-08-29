$(document).ready(function() {

    $('.ruspic,.rusinfo,.viktpic,.ahripic,.karthpic,.veipic,.syndpic,.heimpic,.backbutton,.summtab,.vikticon,.annieicon,.fizzicon,.viktinfo,.ahriinfo,.karthinfo,.veiinfo,.syndinfo,.heiminfo').hide()

    $('.russia').click(function() {
    $('div.default h5').hide();
    $('.ruspic,.backbutton,.rusinfo').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();});
    
    $('.viktor').click(function() {
    $('div.default h5').hide();
    $('.viktpic,.backbutton,.viktinfo').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();});
    
    $('.ahri').click(function() {
    $('div.default h5').hide();
    $('.ahripic,.backbutton,.ahriinfo').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();});
    
    $('.karthus').click(function() {
    $('div.default h5').hide();
    $('.karthpic,.backbutton,.karthinfo').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();});
    
    $('.veigar').click(function() {
    $('div.default h5').hide();
    $('.veipic,.backbutton,.veiinfo').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();});
    
    $('.syndra').click(function() {
    $('div.default h5').hide();
    $('.syndpic,.backbutton,.syndinfo').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();});
    
    $('.heimerdinger').click(function() {
    $('div.default h5').hide();
    $('.heimpic,.backbutton,.heiminfo').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();});
    
    $('.summary').click(function() {
    $('div.default h5').hide();
    $('.summtab,.backbutton,.vikticon,.annieicon,.fizzicon').fadeIn('slow');
    $('.russia,.viktor,.ahri,.karthus,.syndra,.veigar,.heimerdinger,.summary').hide();})
    
    $('.backbutton').click(function() {
    $('div.default h5').fadeIn('slow');
    $('.ruspic,.rusinfo,.viktpic,.ahripic,.karthpic,.veipic,.syndpic,.heimpic,.backbutton,.summtab,.vikticon,.annieicon,.fizzicon,.viktinfo,.ahriinfo,.karthinfo,.veiinfo,.syndinfo,.heiminfo').hide()
    $('.russia,.viktor,.ahri,.syndra,.veigar,.karthus,.heimerdinger,.summary').fadeIn('slow');});})