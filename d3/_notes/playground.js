//testing self executing anonymous function
function hi() {
  console.log('hi');
}

function bye() {
  console.log('bye');
}

function hellogoodbye() {
  hi();
  bye();
}

(function() {
  function hi() {
    console.log('hi');
  };

  function bye() {
    console.log('bye');
  };

  function hellogoodbye() {
    console.log('hellogoodbye() is running');
    hi();
    bye();
  };

  hellogoodbye();
})();


// return locally scoped variable to override globally scoped variable
var a = 1;

function test() {
  console.log('test is running for the first time:', a);
  a = 2;
  console.log('the new value of a is:', a);
  return a;
}

function execute() {
  console.log(a);
}


// .delay() function
(animation).delay(by_x);