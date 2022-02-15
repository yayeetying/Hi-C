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
    bToggler.innerHTML
  }
  else { //mode is "circle"

  }
}

//traditional function
var drawRect = function (e) {
  var mouseX =
  var mouseY =
  console.log("mouseclick registered at ", mouseX, mouseY);
}

//var drawCircle = funciton(e) {
var drawCircle = (e) => {
  console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
var draw = (e) => {

}

//var wipeCanvas = function() {
var wipeCanvas = () => { //no need to have event for param

}

c.addEventListener("click", draw);
var bToggler = document.getElementByID("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = ;
clearB.;
