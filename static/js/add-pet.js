var value = 0;

floatLabels = () => {
    document.querySelectorAll("input").forEach((e)=>{e.addEventListener("blur", ()=>{
        if(e.tagName == "INPUT" && e.type != "date")
            (e.value) ? e.classList.add("hasInput") : e.classList.remove("hasInput");
    })});
}

showNext = (currentForm) => {
    const currStep = Number(currentForm.dataset.step);
    const nextForm = document.querySelector(`[data-step='${currStep+1}']`);
    currentForm.classList.add("leftOut");
	setTimeout(()=>currentForm.classList.add("hidden"), 500);
    nextForm.classList.add("coming");
    nextForm.classList.remove("hidden");
	setTimeout(()=>{
        currentForm.classList.replace("leftOut", "waitingLeft");
        nextForm.classList.remove("waitingRight", "coming");
    }, 500);
    value += 33;
    if(value<100){
        const progressIndicators = document.querySelectorAll(".form-progress-indicator.active");
        progressIndicators[progressIndicators.length-1].nextElementSibling.classList.add("active");
        document.querySelector("progress").value = value;
    }
}

showPrevious = (currentForm) =>{
    const currStep = Number(currentForm.dataset.step);
    const nextForm = document.querySelector(`[data-step='${currStep-1}']`);
    currentForm.classList.add("rightOut");
    setTimeout(()=>currentForm.classList.add("hidden"), 500);
    nextForm.classList.add("coming");
    nextForm.classList.remove("hidden");
    setTimeout(()=>{
        currentForm.classList.replace("rightOut", "waitingRight");
        nextForm.classList.remove("waitingLeft", "coming");
    }, 500);
    value -= 33;
    if(value<100){
        const progressIndicators = document.querySelectorAll(".form-progress-indicator.active");
        progressIndicators[progressIndicators.length-1].classList.remove("active");
        document.querySelector("progress").value = value;
    }
}

buttonHandler = () => {
    document.querySelectorAll(".js-continue").forEach((e)=>e.addEventListener("click", (event)=>{
        event.preventDefault();
        showNext(e.parentElement.parentElement);
    }));
    document.querySelectorAll(".js-back").forEach((e)=>e.addEventListener("click", (event)=>{
        event.preventDefault();
        showPrevious(e.parentElement.parentElement);
    }));
}

init = () => {
    floatLabels();
    buttonHandler();
}

init();