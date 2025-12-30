const btn = document.getElementById("btn");
const form = document.getElementById("Formget");
const btnSound = new Audio("/static/sounds/soundbouton.mp3");
const btnSounds = new Audio("/static/sounds/soundcheckbox.mp3");
btn.addEventListener("click", () => {
    btnSound.currentTime = 0;
    btnSound.volume = 1;
    btnSound.play();
    setTimeout(() =>{
        form.submit();
    }, 400);
});
const chexboxes = document.querySelectorAll(".choice");
chexboxes.forEach(box => {
    box.addEventListener("change", () => {
        btnSounds.currentTime = 0;
        btnSounds.play();
    });
});