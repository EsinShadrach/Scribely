const search_cont = document.querySelector(".search_cont");

search_cont.addEventListener("click", () => {
    document.addEventListener('click', (e)=>{
        let tar = e.target
        if (search_cont.children[0] != tar){
            search_cont.classList.remove('input_active')
        }else{
            search_cont.classList.add("input_active");
        }
    })
});
