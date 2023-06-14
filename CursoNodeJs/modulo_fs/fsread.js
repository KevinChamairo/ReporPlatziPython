const fs = require('fs');
//Leer un archivo
// fs.readFile('index.html', 'utf-8', (err, contenido) => {
//     if(err){
//         console.log(err);
//     } else {
//         console.log(contenido);
//     }
//     console.log('Continua la funcion....')
// })


//Cambia el archivo index.html por main.html
// fs.rename('index.html', 'main.html', (err) => {
//     if(err){
//         throw err;
//     }
//     console.log('Nombre cambiado exitosamente.');
// });

//Agrega contenido al final de un archivo
// fs.appendFile('index.html', '<p>Hola</p>', (err) => {
//     if(err){
//         throw err;
//     }
//     console.log('Archivo actualizado.');
// })

//Reemplaza contenido
// fs.writeFile('index.html', 'Contenido nuevo', (err) =>{
//     if(err){
//         throw err;
//     }
//     console.log('Contenido reemplazado exitosamente.')
// })

//Elimina archivo
// fs.unlink('index.html', (err)=>{
//     if(err){
//         throw err;
//     }
//     console.log('Archivo eliminado.');
// })