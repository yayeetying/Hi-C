//retrieve node in DOM via ID
var c = document.getElementByID("slate");

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
}

//var drawCircle = funciton(e) {
var drawCircle = (e) => {
  console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
var draw = (e) => {
  if (mode == "rect") {
    drawRect;
  }
  else {
    drawCircle;
  }
}

//var wipeCanvas = function() {
var wipeCanvas = () => { //no need to have event for param

}

c.addEventListener("click", draw); //click on canvas, go go draw!
var bToggler = document.getElementByID("buttonToggle");
bToggler.addEventListener("click", toggleMode); //click on button, change mode
// var clearB = ;
// clearB.;
