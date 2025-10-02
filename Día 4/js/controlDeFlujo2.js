let edad = 16;
let calificacion = 4.1;


if (edad < 18) {
    console.log("Eres menor de edad");
    if (calificacion >= 4.5) {
        console.log("Aprobado");
    } else {
        console.log("Rechazado");
    }
} else {
    console.log("Eres adulto");
}

console.log("\n")
console.log("Primera prueba de Js en el navegador")

alert("Este un mensaje desde JS");
let nombre = prompt("Como te llamas?");
console.log("Tu nombre es: " +nombre);
