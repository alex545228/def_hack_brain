let menu_type = document.querySelectorAll('.menu')

menu_type.forEach(menu_btn =>{
    menu_btn.addEventListener("click", function(e){
        if(menu_btn.value === "positive"){
            menu_btn.innerText = "нейтральный";
            menu_btn.value = "neutral";
        }else if(menu_btn.value === "neutral") {
            menu_btn.innerText = "негативный";
            menu_btn.value = "negative";
        }
        else {
            menu_btn.innerText = "положительный";
            menu_btn.value = "positive";
        }
    });
})

