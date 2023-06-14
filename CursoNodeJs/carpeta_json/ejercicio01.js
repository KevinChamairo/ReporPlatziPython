let Numero = 10;

let array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];

for(let element in array)
{
    console.log(element, "->", array[element*2])
}

for(let i = 0; i < array.length; i++)
{
    console.log("Posicion: ", i,"->",array[i])
}