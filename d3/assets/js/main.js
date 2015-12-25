var scrollToTop = (function() {

  //*cache DOM
  var $window = $(window);
  var $body = $('body');
  var $scrollBtn = $('#scroll-btn');

  //*bind events
  $window.scroll(_showToTopButton);
  $scrollBtn.on('click', _scrollToTop);


  function _showToTopButton() {
    ( $(this).scrollTop() > 550 ) ? $scrollBtn.addClass('scroll-btn--show') :
      $scrollBtn.removeClass('scroll-btn--show');
  }

  function _scrollToTop() {
    $body.animate({scrollTop: 0}, 500);
  }

})();