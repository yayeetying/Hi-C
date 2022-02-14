//retrieve node in DOM via ID
var c = document.getElementByID("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
  console.log("toggling...");
  if (mode=="rect") {
    bToggler.innerHTML
  }
  else { //mode is "circle"
    
  }
}

c.addEventListener("click", draw);
var bToggler = document.getElementByID("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = ;
clearB.;
