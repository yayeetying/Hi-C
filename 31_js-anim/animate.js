// Team ApesTogetherStrong :: Yaying Liangli, Joshua Kloepfer
// SoftDev pd1
// K31 -- canvas based JS animation
// 2022-02-17

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground");// GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "blue";// YOUR CODE HERE

var requestID = null;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...");
  ctx.clearRect(0,0,c.width, c.height);
  // OUR CODE HERE
};


var radius = 0;
var growing = true; //is the circle growing?

//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...");

  clear();
  if (growing == true && radius >= 250) { //250 = max radius of canvas (500/2)
    growing = false;
  }
  else if (growing == false && radius <= 1) { //1 is min radius of canvas
    growing = true;
  }
  if (growing == true) {
    radius += 5;
  }
  else {
    radius -= 5;
  }
  ctx.beginPath();
  ctx.arc(250, 250, radius, 0, 2*Math.PI); //summon a circle!: (x,y,radius,startAngle,endAngle)
  ctx.fill();

  requestID = window.requestAnimationFrame(drawDot); //before browser renders the next frame, call the function held at the variable drawDot

  // OUR CODE HERE
  /*
    ...to
    Wipe the canvas,
    Repaint the circle,
    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
   */
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  requestID = window.cancelAnimationFrame(requestID); //previous requestID was requestAnimationFrame; cancel this previous requestID
  //requestID is now null
  console.log( requestID );

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
};


dotButton.addEventListener( "click", function() {if (requestID == null) {drawDot()}} );
//if requestID != null, then it means the circle is growing / animating --> even if user clicks button, the fxn drawDot won't be called
stopButton.addEventListener( "click",  stopIt );
