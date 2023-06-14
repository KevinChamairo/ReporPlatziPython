const EventEmitter = require('events');

const emisorProductos = new EventEmitter();

/**Ejemplo 1 */
// emisorProductos.on('compra', () => {
//     console.log('Se realizo una compra.')
// })

// emisorProductos.emit('compra');
// emisorProductos.emit('compra');
// emisorProductos.emit('compra');

emisorProductos.on('compra', (total, numProductos) => {
    console.log(`Se realizo una compra $${total}.`)
    console.log(`Numero de productos: ${numProductos}.`)
})

emisorProductos.emit('compra', 500, 5);
emisorProductos.emit('compra', 500, 5);
emisorProductos.emit('compra', 500, 5);