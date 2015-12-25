var nav = (function() {
  //*cache DOM
  var $navMain = $('.nav-main');
  var $allButNav = $navMain.nextAll('*');
  var $link = $('.link');
  var $drop = $('.drop');
  var $linkDrop = $('.link > .drop');

  //*bind events
  //Fade out everything but the nav bar
  $navMain.hover(_fade, _unfade);
  //Hover nav links to show drop menus
  $link.hover(_showMenu, _hideMenu);
  //Hide opened nav bar on touch devices
  $allButNav.on('click', _hideNav);


  function _fade() {
    $allButNav.fadeTo(0.5, 0.7);
  }

  function _unfade() {
    $allButNav.fadeTo(0.5, 1);
  }

  function _showMenu() {
    //Use css instead of .show() so mobile doesn't require double tap for links
    $(this).children('.drop').css('display', 'block');
  }

  function _hideMenu() {
    //Use css instead of .hide() so mobile doesn't require double tap for links
    $(this).children('.drop').css('display', 'none');
  }

  function _hideNav() {
    $drop.hide();
  }

})();


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