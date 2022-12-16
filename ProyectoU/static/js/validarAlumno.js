const $formulario = document.getElementById('Alumno');
const $runTxt = document.getElementById('rut');
const $nombreTxt = document.getElementById('nombre');
$mensaje = "";

const botonesEliminar = document.querySelectorAll('.btnEliminar');

(function(){
    $formulario.addEventListener('submit',function(e){
        let run = String($runTxt.value).trim();
        if (run.length===0){
            $mensaje = "Rut Obligatorio";
            document.getElementById('msgRut').classList.add('text-danger');
            document.getElementById('msgRut').innerHTML = $mensaje;
            e.preventDefault();
        }else{
            document.getElementById('msgRut').innerHTML = "";
        }
        let nombre = String($nombreTxt.value).trim();
        if (nombre.length===0){
            $mensaje = "Nombre Obligatorio";
            document.getElementById('msgNombre').classList.add('text-danger');
            document.getElementById('msgNombre').innerHTML = $mensaje;
            e.preventDefault();
        }else{
            document.getElementById('msgNombre').innerHTML = "";
        }  
    });
/* Esto seria una confirmación para eliminar simple de javaScript

    botonesEliminar.forEach(boton =>{
        boton.addEventListener('click',function(e){
            let respuesta = confirm("Esta seguro que desea eliminar?");
            if(!respuesta){
                e.preventDefault();
            }
        })
    });
*/

    botonesEliminar.forEach(boton =>{
        boton.addEventListener('click',function(e){
            e.preventDefault();
            Swal.fire({
                title: "¿Estas seguro de querer Eliminar el registro?",
                showCancelButton: true,
                confirmButtonText: "Eliminar Registro",
                cancelButtonText: "Mejor no",
                confirmButtonColor: '#d00',
                backdrop: true,
                preConfirm: () => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: ()  => false,
            });
        });
    });

})();





