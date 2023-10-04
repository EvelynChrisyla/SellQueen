const list = document.getElementById("list")
const list2 = document.getElementById("list2")
const list3 = document.getElementById("list3")
const detailInfo = document.querySelector(".personalProfile-container")
const usrLoc = document.querySelector(".userLocation-container")

list.addEventListener("click",
    e => { 
    detailInfo.style.display = "flex";
    usrLoc.style.display = "none"
    }
);

list2.addEventListener("click",
    e => { 
        detailInfo.style.display = "none"
        usrLoc.style.display = "flex"
    }
);

list3.addEventListener("click",
    e => { 
        detailInfo.style.display = "none"
        usrLoc.style.display = "none"
    }
)

