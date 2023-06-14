let infoCurso = {
    "titulo": "Aprende Node.js",
    "numVistas": 45642,
    "numLikes": 21123,
    "temas": [
        "JavaScript",
        "Node.js"
    ],
    "esPublico": true
}

console.log(infoCurso)

let infoCursoJSON = JSON.stringify(infoCurso);

console.log(infoCursoJSON);
console.log(typeof infoCursoJSON)

//Objeto -> Cadena de Caracteres
//Cadena de caracteres en formato JSON