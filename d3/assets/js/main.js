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
    $(this).children('.drop').css('display', 'block');
  }

  function _hideMenu() {
    $(this).children('.drop').css('display', 'none');
  }

  function _hideNav() {
    $drop.hide();
  }
})();

var toggleLegendaries = (function() {
  //*cache DOM
  var $toggle = $('.toggle');
  var $item = $('.item');

  //*bind events
  //Click a class-toggler to hide non-class items
  $toggle.on('click', _toggleItems);


  function _toggleItems() {
    var owner = $(this).attr('class').split(' ')[1].substring(8);
    if (owner == 'all') {
      $item.each(function() {
        $(this).css('display', 'block');
      });
    }
    else {
      $item.each(function() {
        var itemOwner = $(this).attr('class').split(' ')[1];
        if (itemOwner == owner || itemOwner == 'all') {
          $(this).css('display', 'block');
        }
        else {
          $(this).css('display', 'none');
        };
      });
    };
    //Adds a brighter border when selected.
    $(this).siblings().removeClass('toggle--selected');
    $(this).addClass('toggle--selected');
  }
})();

var toggleItemSets = (function() {
  //*cache DOM
  var $toggle = $('.toggle');
  var $set = $('.set');

  //*bind events
  //Click a class-toggler to hide non-class items
  $toggle.on('click', _toggleSets);

  function _toggleSets() {
    var owner = $(this).attr('class').split(' ')[1].substring(8);
    if (owner == 'all') {
      $set.each(function() {
        $(this).css('display', 'block');
      });
    }
    else {
      $set.each(function() {
        var set = $(this).attr('class').split(' ')[1];
        if (set == owner || set == 'Universal') {
          $(this).css('display', 'block');
        }
        else {
          $(this).css('display', 'none');
        };
      });
    };
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
    $(this).parent().siblings('.extra').toggle(150);
  }

  function _hideExtra() {
    $(this).parent().hide();
  }
})();