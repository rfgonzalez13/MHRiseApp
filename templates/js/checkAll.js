function ComprobarDescripciones(n) {

    var toret = false;
    var index = 1;

    const edNombre = document.getElementById( "edNombre" );
    const edNvmax = document.getElementById( "edNvmax" );

    if( edNombre.value.trim().length > 0
              && edNvmax.value.trim().length > 0 ){
        toret = true;
    }else{
        toret = false;
    }

    while (index < n + 1 && toret) {
        var edDescrip = document.getElementById("edDescrip" + index)
        if (edDescrip.value.trim().length <= 0) {
            toret = false;
        }
        n++;
    }
    if(!toret){
        alert("Existen campos vacíos");
    }
     return toret;
}
