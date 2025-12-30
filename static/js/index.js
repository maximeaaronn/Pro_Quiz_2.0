setTimeout(function() {
                document.getElementById("container").style.display = "none";
                document.getElementById("bloc").style.display = "block";
            },4000);
const sound = new Audio("/static/sounds/soundbouton.mp3");
const btn = document.getElementById("btn");
const form = document.getElementById("Formget");
btn.addEventListener("click", () => {
    sound.currentTime = 0;
    sound.play();
    if(!form.checkValidity()){
        form.reportValidity();
        return;
    };
    sound.currentTime = 0;
    sound.volume = 1;
    sound.play();
    setTimeout(() =>{
        form.submit();
    },700);
});
