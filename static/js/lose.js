const sounds = new Audio("/static/sounds/soundbouton.mp3");
const retryBtn = document.getElementById("btn");
retryBtn.addEventListener("click", function (e) {
    e.preventDefault();
    sounds.currentTime = 0;
    sounds.volume = 1;
    sounds.play();
    setTimeout(() =>{
        window.location.href = retryBtn.href;
    },800);
});
window.addEventListener("DOMContentLoaded", () =>{
    const musiclose = new Audio("/static/sounds/musiclose.mp3");
    musiclose.volume = 1;
    musiclose.play();
    setTimeout(() =>{
        musiclose.pause();
        musiclose.currentTime = 0;
    },7000);
});