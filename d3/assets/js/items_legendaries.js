var toggleLegendaries = (function() {

  //*cache DOM
  var $toggle = $('.toggle');
  var $patch = $('.patch > span');
  var patch24 = '24'
  var $itemContainer = $('.item-container');
  var $item = $('.item');
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
          $(this).show(200);
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
  }

  //load first 20 items first
  function _delayLoading() {
    $item.slice(20).show();
    $filler.show();
  }

})();