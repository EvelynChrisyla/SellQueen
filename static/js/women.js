const container = document.querySelector(".women-container")
const menContainer = document.querySelector(".men-container")


function fill(destination) {
    /* anchor ini supaya ketika catalogProduct di klik akan menuju ke halaman dtailProduct */
    let anchor = document.createElement("a")
    anchor.href = "/SourceHTML/detailProduct.html"

    const card = document.createElement('div')
    card.className = "card test"

    /*  ini array untuk randomIMG */
    // let imageUrls = [
    //     "/SourceIMG/AirForce1-2.png",
    //     "/SourceIMG/AirForce1-3.png",
    //     "/SourceIMG/AirForce1-4.png"
    // ];

    // // Memilih URL gambar secara acak dari daftar imageUrls
    // let randomImageUrl = imageUrls[Math.floor(Math.random() * imageUrls.length)];
    
    card.innerHTML = `
    <div class="caption addOn">Air Force 1 - Low</div>
    <img class="catalog" src = "/SourceIMG/AirForce1-3.png" >
    <div class="caption price ">Rp. 1.xxx.xxx</div>
    `;

    /* Assign si div catalog ke dalam <a href > yg tadi dibuat */
    anchor.appendChild(card)
    destination.appendChild(anchor)
}

for (let i = 0; i < 10; i++) {
    fill(container)
}

for (let i = 0; i < 10; i++) {
    fill(menContainer)
}