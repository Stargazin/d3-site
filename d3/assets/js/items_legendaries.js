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


var toggleLegendaries = (function() {

  //*cache DOM
  var $toggle = $('.toggle');
  var $patch = $('.patch > span');
  var patch24 = '24'
  var $itemContainer = $('.item-container');
  var $item = $('.item');
  var $noItemMsg = $('.nothing-found');
  var $filler = $('.filler');
  var $reverseItem = $($item.get().reverse())

  //*bind events
  //Click a class-toggler to hide non-class items
  $toggle.on('click', _toggleClassItems);
  //Click to toggle displaying 2.4 items only
  $patch.on('click', _togglePatchItems);

  _delayLoading()

  function _toggleClassItems() {
    $item.hide();
    var owner = $(this).attr('class').split(' ')[1].substring(8);
    //Show all items in original order
    if (owner == 'all') {
      $reverseItem.each(function() {
        $(this).prependTo($itemContainer);
        $(this).show();
      });
    }
    else {
      $reverseItem.each(function() {
        var itemOwner = $(this).attr('class').split(' ')[1];
        //Show item if useable by class
        if (itemOwner == owner || itemOwner == 'all') {
          $(this).show();
          //Move class-specific items to top
          if (itemOwner == owner) {
            $(this).prependTo($itemContainer);
          };
        }
        //Hide item if not useable by class
        else {
          $(this).hide();
        };
      });
    };

    //Changes border color when toggle button is selected
    $(this).siblings().removeClass('toggle--selected');
    $(this).addClass('toggle--selected');

    _visibleItemCheck()
  }

  function _togglePatchItems() {
    $itemContainer.fadeTo(25, 0.1);
    $item.each(function() {
      var item = $(this).attr('class').split(' ')[2];
      //Hide/show items not from Patch 2.4
      if (item !== patch24) {
        $(this).toggleClass('patch-off');
      };
    });
    $itemContainer.fadeTo(25, 1);

    //Changes border color when patch button is selected
    $(this).toggleClass('patch--selected');

    _visibleItemCheck()
  }

  //Checks if there are no items to be shown
  function _visibleItemCheck() {
    var visibleItem = 0;
    $item.each(function() {
      if ($(this).is(':visible')) {
        visibleItem++;
      };
    });
    visibleItem ? $noItemMsg.hide() : $noItemMsg.show()
  }

  //load first 20 items first
  function _delayLoading() {
    $item.slice(20).show();
    $filler.show();
  }

})();


var affixExtra = (function() {
  //*cache DOM
  var $vary = $('.vary');
  var $extraX = $('.extra-x');

  //*bind events
  //Toggles .extra when clicking .vary
  $vary.on('click', _showExtra);
  //Closes .extra when clicking the 'x'
  $extraX.on('click', _hideExtra);


  function _showExtra() {
    $(this).parent().siblings('.extra').toggle(100);
  }

  function _hideExtra() {
    $(this).parent().hide(100);
  }

})();