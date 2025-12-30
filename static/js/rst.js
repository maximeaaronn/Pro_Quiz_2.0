const soun = new Audio("/static/sounds/soundbouton.mp3");
const selec = document.querySelectorAll(".btn-nav");
selec.forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();
        soun.currentTime = 0;
        soun.volume = 1;
        soun.play();
        const url = this.href;
        setTimeout( () => {
            window.location.href = url;
        }, 800);
    });
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