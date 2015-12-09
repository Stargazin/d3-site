var toggleItems = (function() {

  //cache DOM
  var $toggle = $('.toggle');
  var $item = $('.item');

  //bind events
  $toggle.on('click', _toggler);

  function _toggler() {
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
  };
})();


var extraAffix = (function() {

  //cache DOM
  var $vary = $('.vary');
  var $extraX = $('.extra-x');

  // //bind events
  $vary.on('click', _showExtra);
  $extraX.on('click', _hideExtra);

  function _showExtra() {
    $(this).parent().siblings('.extra').toggle(150);
  }

  function _hideExtra() {
    $(this).parent().hide();
  }
})();