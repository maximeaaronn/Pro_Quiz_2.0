const music = new Audio("/static/sounds/me.mp3");
window.addEventListener("load", () =>{
    music.currentTime = 0;
    music.volume = 0.5;
    music.play();
   
});