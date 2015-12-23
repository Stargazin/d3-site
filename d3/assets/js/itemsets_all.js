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
        $(this).show(250);
      });
    }
    else {
      $reverseSet.each(function() {
        var setOwner = $(this).attr('class').split(' ')[1];
        //Show set if useable by class
        if (setOwner == owner || setOwner == 'universal') {
          $(this).show(150);
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