//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//arrow function -- more limited; param => expression
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
//var toggleMode = function(e) {
var toggleMode = (e) => {
  console.log("toggling...");
  if (mode=="rect") {
    mode = "circle"; //change mode from rect to circle
    bToggler.innerHTML = "rect"; //if user clicks button again, it'll be rect
  }
  else { //mode is "circle"
    mode = "rect";
    bToggler.innerHTML = "circle";
  }
}

//traditional function
var drawRect = function (e) {
  //(x,y) coords of upper-left hand corner of rectangle
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseclick registered at ", mouseX, mouseY);

  ctx.beginPath(); //called everytime before each line so they can be drawn with different color
  ctx.fillStyle = 'red';
  ctx.fillRect(mouseX, mouseY, 100, 200); //(x,y,width,height);
  //if use fillStyle, use fill<shape>?
  ctx.stroke(); //actually draw the rect on canvas
}

//var drawCircle = funciton(e) {
var drawCircle = (e) => {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
var draw = (e) => {
  if (mode == "rect") {
    drawRect(e);
  }
  else {
    drawCircle(e);
  }
}

//var wipeCanvas = function() {
var wipeCanvas = () => { //no need to have event for param

}

c.addEventListener("click", draw); //click on canvas, go go draw!
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode); //click on button, change mode
// var clearB = ;
// clearB.;
