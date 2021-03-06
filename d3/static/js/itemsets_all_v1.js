$(document).ready(function() {
  //Initially highlight first set piece for every set
  //Can be changed later (see setPiecePics)
  $('.set__piece-container div:first-child a').addClass('pic-showing');
});


/* START main.js */
var nav = (function() {
  //*cache DOM
  var $navMain = $('.nav-main');
  var $allButNav = $navMain.nextAll('*');
  var $drop = $('.drop');
  var $link = $drop.parent();
  var $linkDrop = $('.link > .drop');

  //*bind events
  //Hover nav links to show drop menus
  $link.hover(_showMenu, _hideMenu);
  //Hide opened nav bar on touch devices
  $allButNav.on('click', _hideNav);


  function _showMenu() {
    $(this).children('.drop').css('display', 'block');
  }

  function _hideMenu() {
    $(this).children('.drop').css('display', 'none');
  }

  function _hideNav() {
    $drop.hide();
  }

})();


var scrollToTop = (function() {

  //*cache DOM
  var $window = $(window);
  var $bodyHTML = $('body, html');
  var $scrollBtn = $('#scroll-btn');

  //*bind events
  $window.scroll(_showToTopButton);
  $scrollBtn.on('click', _scrollToTop);


  function _showToTopButton() {
    ( $(this).scrollTop() > 550 ) ? $scrollBtn.addClass('scroll-btn--show') :
      $scrollBtn.removeClass('scroll-btn--show');
  }

  function _scrollToTop() {
    $bodyHTML.animate({scrollTop: 0}, 500);
  }

})();
/* END main.js */


var toggleItemsets = (function() {

  //*cache DOM
  var $toggle = $('.toggle');
  var $patch = $('.patch > span');
  var patch24 = '24'
  var $setContainer = $('.set-container');
  var $set = $('.set');
  var $reverseSet = $($set.get().reverse())

  //*bind events
  //Click a class-toggler to hide non-class set
  $toggle.on('click', _toggleClassSets);
  //Click to toggle displaying 2.4 sets only
  $patch.on('click', _togglePatchSets);

  function _toggleClassSets() {
    $set.hide();
    var owner = $(this).attr('class').split(' ')[1].substring(8);
    //Show all sets in original order
    if (owner == 'all') {
      $reverseSet.each(function() {
        $(this).prependTo($setContainer);
        $(this).show();
      });
    }
    else {
      $reverseSet.each(function() {
        var setOwner = $(this).attr('class').split(' ')[1];
        //Show set if useable by class
        if (setOwner == owner || setOwner == 'universal') {
          $(this).show();
          //Move class-specific sets to top
          if (setOwner == owner) {
            $(this).prependTo($setContainer);
          };
        }
        //Hide set if not useable by class
        else {
          $(this).hide();
        };
      });
    };
    //Changes border color when toggle button is selected
    $(this).siblings().removeClass('toggle--selected');
    $(this).addClass('toggle--selected');
  }

  function _togglePatchSets() {
    $setContainer.fadeTo(25, 0.1);
    $set.each(function() {
      var set = $(this).attr('class').split(' ')[2];
      //Hide/Show sets not from Patch 2.4
      if (set !== patch24) {
        $(this).toggleClass('patch-off');
      };
    });
    $setContainer.fadeTo(25, 1);
    //Changes border color when patch button is selected
    $(this).toggleClass('patch--selected');
  }

})();


var setPiecePics = (function() {
  //*cache DOM
  var $setPiece = $('.set__piece__name');

  //Global var for _switchPiecePic()
  var $showing = 0;

  //*bind events
  //Changes picture to selected set piece
  $setPiece.on('click', _switchPiecePic);


  function _switchPiecePic(e) {
    e.preventDefault();
    var piece = $(this).parent().attr('id').replace(/-/g, '_');
    var ownerSet = $(this).parent().parent().parent();
    var owner = ownerSet.attr('class').split(' ')[1];
    switch (true) {
      case owner == 'barbarian':
        owner = 'barb';
        break;
      case owner == 'crusader':
        owner = 'sader';
        break;
      case owner == 'demon-hunter':
        owner = 'dh';
        break;
      case owner == 'monk':
        owner = 'monk';
        break;
      case owner == 'witch-doctor':
        owner = 'wd';
        break;
      case owner == 'wizard':
        owner = 'wiz';
        break;
      default:
        owner = 'universal';
    }
    //Changes pictures
    $(this).parent().parent().siblings('.set__pic-container').children().attr('style', 'background: url(/static/media/items/sets/' +owner+ '/' +piece+ '.png)');

    //Changes which set piece name is highlighted
    if ( $(this).attr('class').split(' ')[1] !== 'pic-showing' ) {
      $(this).parent().siblings().children().removeClass('pic-showing');
      $(this).addClass('pic-showing');
    };
  }

})();