

const cardProduct = () =>{
    let forYou = document.querySelector(".forYou");
    
    let card = document.createElement("div");
    card.className = "card test";
    
    card.innerHTML = `
    <div class="caption addOn">Air Force 1</div>
    <img class="catalog" src = "/SourceIMG/AirForce1-3.png" >
    <div class="caption price ">Rp. 1.xxx.xxx</div>
    `;
    
    forYou.appendChild(card)
}
for (let i = 0; i < 5; i++) {
    cardProduct(); 
}