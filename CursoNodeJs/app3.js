function mostrarTema(tema) {
    console.log(`Esty aprendiendo ${tema}`)
}

// mostrarTema('Node Js')

setTimeout(mostrarTema, 5000, 'Node Js') //Demora 5 segundos en compilar

function sumar(a, b){
    console.log(a+b)
}

setTimeout(sumar, 10000, 5, 6);

