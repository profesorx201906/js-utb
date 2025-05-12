function changeColor(color) {
  let parrafo = document.getElementById("para");
  parrafo.innerHTML=color;  
  parrafo.style.color = color;
}

const changeColor1 = (color) => {
  let parrafo = document.getElementById("para");
  parrafo.style.color = color;
}