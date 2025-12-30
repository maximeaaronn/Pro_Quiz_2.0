const souns = new Audio("/static/sounds/soundbouton.mp3");
const retryBtn = document.getElementById("btn");
retryBtn.addEventListener("click", function (e) {
    e.preventDefault();
    souns.currentTime = 0;
    souns.volume = 1;
    souns.play();
    setTimeout(() =>{
        window.location.href = retryBtn.href;
    },800);
});
window.addEventListener("DOMContentLoaded", () =>{
    const musicwin = new Audio("/static/sounds/musicwin.mp3");
    musicwin.volume = 1;
    musicwin.play();
    setTimeout(() =>{
        musicwin.pause();
        musicwin.currentTime = 0;
    },7000);
});