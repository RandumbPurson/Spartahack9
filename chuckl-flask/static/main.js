// $('a[href*=#]').click(function(){
//   return false;
// });
  

var animationEndEvent = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

var Person = {
  wrap: $('#people'),
  add: function(image){
    this.wrap.append("<div class='person'><src='" + image + "' /></div>");
  }
}

var App = {
  yesButton: $('.button.yes .trigger'),
  noButton: $('.button.no .trigger'),
  blocked: false,
  like: async function(liked){
    var animate = liked ? 'animateYes' : 'animateNo';
    var self = this;
    console.log("test")
    var person = await fetch("/memes");
    Person.add(person);
    if (!this.blocked) {
      this.blocked = true;           
      $('.person').eq(0).addClass(animate).one(animationEndEvent, function() {
        $(this).remove();
        self.blocked = false;
      });
    }
  }
};

var Phone = {
  wrap: $('#phone'),
  clock: $('.clock'),
  updateClock: function() {
    var date = new Date();
    var hours = date.getHours();
    var min = date.getMinutes();
    hours = (hours < 10 ? "0" : "") + hours;
    min = (min < 10 ? "0" : "") + min;
    var str = hours + ":" + min;
    this.clock.text(str);
  }
}

App.yesButton.on('click', function() {
  App.like(true);
});

App.noButton.on('click', function() {
  App.like(false);
});

$(document).ready(function() {
  fetch("/memes").then(img => {
    console.log("Test")
    Person.add(img)
    Phone.updateClock();
    setInterval('Phone.updateClock()', 1000);
  })
});
