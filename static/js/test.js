
const reccommend = document.createElement("div");

reccommend.className = 'forYou';

document.body.appendChild(reccommend);


function bagan() {
    const div = document.createElement('div');
    
    div.className = 'card test';
    
    div.innerHTML = `
        <div class="caption addOn">Air Force 1</div>
        <img class="catalog" src = "/SourceIMG/AirForce1-3.png" >
        <div class="caption price ">Rp. 1.xxx.xxx</div>
    `;
        
    reccommend.appendChild(div);
}

for (i = 0; i < 15; i++){
    bagan();
}

