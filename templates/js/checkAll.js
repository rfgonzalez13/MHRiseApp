function ComprobarDescripciones(n) {

    let toret;
    let index = 1;

    const edNombre = document.getElementById("edNombre");
    const edNvmax = document.getElementById("edNvmax");
    const edGen = document.getElementById("edDescrip");

    toret = edNombre.value.trim().length > 0
        && edNvmax.value.trim().length > 0
        && edGen.value.trim().length > 0;

    while (index < n + 1 && toret) {
        let edDescrip = document.getElementById("edDescrip" + index)
        if (edDescrip.value.trim().length <= 0) {
            toret = false;
        }
        n++;
    }
    if (!toret) {
        alert("Existen campos vacíos");
    }
     return toret;
}
