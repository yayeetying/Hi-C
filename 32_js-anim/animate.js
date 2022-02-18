/*
Haotian Gan, Yaying
SoftDev
K32 -- More Moving Parts
2022-02-18
Time spent: 1h
*/

const canvas = document.getElementById("slate");
const animate = document.getElementById("animate");
const stopButton = document.getElementById("stop");
const ctx = canvas.getContext("2d");
const dvdLogo = document.getElementById("dvdLogo");
const randomPosButton = document.getElementById("randomPosButton");

let rect = canvas.getBoundingClientRect();
canvas.width = rect.width;
canvas.height = rect.height;

function clearScreen() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

let vx = 300;
let vy = 300;
let x = canvas.width / 2;
let y = canvas.height / 2;

let freeHeight = canvas.height - dvdLogo.height;
let freeWidth = canvas.width - dvdLogo.width;

window.addEventListener("resize", () => {
  let rect = canvas.getBoundingClientRect();
  canvas.width = rect.width;
  canvas.height = rect.height;
  freeHeight = canvas.height - dvdLogo.height;
  freeWidth = canvas.width - dvdLogo.width;
});

const dvdLogoWidth = dvdLogo.width;
const dvdLogoHeight = dvdLogo.height;

function tick(callback) {
  let currentTime;
  let id;
  function animate(timestamp) {
    if (currentTime === undefined) currentTime = timestamp;
    callback(timestamp - currentTime);
    currentTime = timestamp;
    id = requestAnimationFrame(animate);
  }
  id = requestAnimationFrame(animate);
  return {
    stop() {
      cancelAnimationFrame(id);
    },
  };
}

function simulate(deltaTime) {
  //This code assumes that the dvd logo does not bounces more than twice in one axis during the duration of deltaTime
  let seconds = deltaTime / 1000;
  const xChange = seconds * vx;
  const yChange = seconds * vy;
  const xDist = Math.abs(xChange);
  const yDist = Math.abs(yChange);
  //Calculate position after bounce
  const remainingWidth = vx > 0 ? freeWidth - x : x;
  const remainingHeight = vy > 0 ? freeHeight - y : y;
  if (remainingWidth < xDist) {
    vx *= -1;
    x = vx > 0 ? xDist - remainingWidth : freeWidth - (xDist - remainingWidth);
  }
  if (remainingHeight < yDist) {
    vy *= -1;
    y =
      vy > 0 ? yDist - remainingHeight : freeHeight - (yDist - remainingHeight);
  }
  if (!(remainingWidth < xDist || remainingHeight < yDist)) {
    x += xChange;
    y += yChange;
  }
  clearScreen();
  ctx.drawImage(dvdLogo, x, y, dvdLogo.width, dvdLogo.height);
}

let ticker;
animate.addEventListener("click", () => {
  if (ticker) {
    x = canvas.width / 2;
    y = canvas.height / 2;
    return;
  }
  ticker = tick(simulate);
});

stopButton.addEventListener("click", () => {
  if (!ticker) return;
  ticker.stop();
  ticker = undefined;
});

randomPosButton.addEventListener("click", () => {
  if (!ticker) return;
  x = Math.random() * freeWidth + dvdLogo.width / 2;
  y = Math.random() * freeHeight + dvdLogo.height / 2;
});
