// const saludo = require("./saludo");

// console.log(saludo.saludar("freeCodeCamp")); 
// console.log(saludo.saludarHolaMundo()); 

const { saludar, saludarHolaMundo } = require('./saludo')

console.log(saludarHolaMundo())
console.log(saludar('freeKevin'))

console.log('console 1');
console.warn('console 2');
// console.error(new Error('console 3'));

console.log(process)

for (let i = 2; i < process.argv.length; i++)
{
    console.log(process.argv[i]);
}