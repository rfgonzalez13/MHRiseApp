 function check()
    {

        const edNombre = document.getElementById( "edNombre" );
        const edNvmax = document.getElementById( "edNvmax" );

        if ( edNombre.value.trim().length > 0
              && edNvmax.value.trim().length > 0 ){
            return true;
        }else{
            alert("Existen campos vacíos");
            return false;
        }
    }
