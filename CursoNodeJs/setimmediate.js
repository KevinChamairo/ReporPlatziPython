function mostrarTema(tema){
    console.log(`Estoy aprendiendo ${tema}`);
}

console.log('Antes de setImmediate()');

//setImmediate() //Para ejecutar código asíncrono en la próxima iteración del ciclo de eventos (lo más pronto posible)
setImmediate(mostrarTema, 'Node,js');

console.log('Despues de setImmediate()');