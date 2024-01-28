var animationEndEvent = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

var Images = {
  wrap: $('#images'),
  img: null,
  add: function(res){
    res.text().then(img => {
      Images.img = img
      this.wrap.append("<div class='person'><img src='static\/memes\/"+img+"' /></div>");
    })
  }
}

var App = {
  blocked: false,
  like: async function(liked){
    var animate = liked ? 'animateYes' : 'animateNo';
    var self = this;
    await fetch("/memes", {
      method: "PUT",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({liked: liked, img: Images.img})
    })
    var meme = await fetch("/memes");
    Images.add(meme);
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

$(".button.yes").on("click", function() {
    App.like(true);
  });
$(".button.no").on("click", function() {
    App.like(false);
  });

$(document).ready(function() {
  fetch("/memes").then(img => {
    Images.add(img)
    Phone.updateClock();
    setInterval('Phone.updateClock()', 1000);
  })
});
