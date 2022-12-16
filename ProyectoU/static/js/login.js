var attempt =3;
 function validate(){
     var usuar=document.getElementById("usuar").value;
     var password=document.getElementById("password").value;
    if(usuar=="DAE" && password=="dae123"){
         alert("Ingreso exitosamente");
         window.location="HorarioDae.html";
         return false;
     } if(usuar =="Alumno" && password =="alumno123"){
         alert("Ingreso exitosamente");
         window.location="HorarioAlumno.html";
         return false;
    }
     else{
     attempt--;
     }
     alert("Te queda" +attempt+ "intentos mas")
     if(attempt==0){
    document.getElementById("usuar").disable=true;
    document.getElementById("password").disable=true;
    document.getElementById("sumbit").disable=true;
 }
}
