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


var setPiecePictures = (function() {
  //*cache DOM
  var $setPieceName = $('.set__piece__name');
  var $setPiecePic = $('.set__piece__pic');

  //Global var for _showPiecePic()
  var $showing = 0;

  //*bind events
  //Toggles piece picture when clicking piece name
  $setPieceName.on('click', _showPiecePic);
  //Closes piece picture when clicking the picture
  $setPiecePic.on('click', _hidePiecePic);


  function _showPiecePic() {
    if ( $(this).attr('class').split(' ')[1] !== 'pic-showing' ) {
      if ( $showing ) {
        $showing.siblings('.set__piece__pic').hide(50);
        $showing.removeClass('pic-showing');
      };
      $(this).siblings('.set__piece__pic').show(50);
      $(this).addClass('pic-showing');
      $showing = $(this);
    }
    else {
      $(this).siblings('.set__piece__pic').hide(50);
      $(this).removeClass('pic-showing');
      $showing = 0;
    };
  }

  function _hidePiecePic() {
    $(this).hide(50);
    $showing.removeClass('pic-showing');
  }

})();