//catch() --> Método de promesa que solo se ejecuta si la promesa es rechazada
const estatusPedido = () => {
    const estatus = Math.random() < 0.8;
    console.log(estatus);
    return estatus;
};

// for(let i=0; i<10; i++){
//     console.log('ads')
// }

const miPedidoDePizza = new Promise((resolve, reject) =>{
    setTimeout(() => {
        if(estatusPedido())
        {
            resolve('¡Pedido exitoso! Su pizza esta en cambio.');
        } else {
            reject('Ocurrio un error. Por favor intente nuevamente.')
        }
    }, 2000)
})

miPedidoDePizza.then((mensajeDeConfirmacion) => {
    console.log(mensajeDeConfirmacion)
    })
    .catch((mensajeDeError) => {
        console.log(mensajeDeError);
    })