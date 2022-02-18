const tasks = document.querySelectorAll(".task");
let selected = "";
let value = "";

resetTask = () => {
    document.querySelectorAll(".task-name").forEach((e)=> e.classList.contains("selected") ? e.classList.remove("selected") : e );
    selected = "";
    value = "";
}

init = () => {
    document.querySelector(".task-container").addEventListener("click", (e)=>{
        resetTask();
        e.target.classList.add("selected");
        selected = e.target.style.backgroundColor;
        value = e.target.id;
        e.target.id == "deselect" ? resetTask() : e ;
    });
    tasks.forEach((e)=>e.addEventListener("click", ()=>{
        e.style.backgroundColor = (selected && e.style.backgroundColor == selected) ? "" : selected;
        e.innerHTML = (value && e.innerHTML == value) ? "" : value;
    }));
    document.querySelector(".js-reset-schedule").addEventListener("click", ()=>{
        resetTask();
        tasks.forEach((e)=>{
            e.style.backgroundColor="";
            e.innerHTML = "";
        });
    });
    document.querySelector(".js-save-schedule").addEventListener("click", ()=>{
        document.querySelectorAll(".js-pass-data").forEach((e)=>{
            document.querySelectorAll(`.${e.id}`).forEach((a)=>{
                e.value += `${a.innerHTML},`;
            });
        });
    });
    tasks.forEach((e)=>{
        const color = document.getElementById(e.innerHTML)
        e.style.backgroundColor = color ? color.style.backgroundColor : "";
    });
}

init();