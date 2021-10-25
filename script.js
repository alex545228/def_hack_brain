let menu_type = document.querySelectorAll('.menu')
let period_choice = document.querySelectorAll('.period-choice-btn')

menu_type.forEach(menu_btn =>{
    menu_btn.addEventListener("click", function(e){
        if(menu_btn.value === "positive"){
            menu_btn.innerText = "средний";
            menu_btn.value = "neutral";
            menu_btn.style.backgroundColor = "#48CAE4";
            menu_btn.style.color = "black"
        }else if(menu_btn.value === "neutral") {
            menu_btn.innerText = "отрицательный";
            menu_btn.value = "negative";
            menu_btn.style.backgroundColor = "#03045E";
            menu_btn.style.color = "#48CAE4"
        }
        else {
            menu_btn.innerText = "положительный";
            menu_btn.value = "positive";
            menu_btn.style.backgroundColor = "#0297C7";
            menu_btn.style.color = "black"
        }
    });
})

period_choice.forEach(chosen =>{
    chosen.addEventListener("onmousedown", function(e){
        period_choice.forEach(opt =>{
            if (opt.classList.contains('chosen')){
                opt.classList.remove('chosen');
            }    
        });
        chosen.classList.add('chosen');
    });
})
