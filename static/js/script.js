document.getElementById("icon-menu").addEventListener("click",mostrar_menu);

function mostrar_menu(){
    document.getElementById("move-content").classList.toggle('move-container-x')
    document.getElementById("show-menu").classList.toggle('show-lateral')
}



$(function () {

    var Page = (function () {

        var $navArrows = $('#nav-arrows').hide(),
            $shadow = $('#shadow').hide(),
            slicebox = $('#sb-slider').slicebox({
                onReady: function () {

                    $navArrows.show();
                    $shadow.show();
                    

                },
                orientation: 'r',
                cuboidsRandom: true,
                disperseFactor: 30
            }),

            init = function () {

                initEvents();

            },
            initEvents = function () {

                // add navigation events
                $navArrows.children(':first').on('click', function () {

                    slicebox.next();
                    return false;

                });

                $navArrows.children(':last').on('click', function () {

                    slicebox.previous();
                    return false;

                });

            };

        return {
            init: init
        };

    })();

    Page.init();

});

$("#formulario1").validate({
    rules:{
        "txtTitulo":{
            required: true,
            minlength: 4,
            maxlength : 15
        },
        "txtEtiquetas":{
            required: true,
            minlength: 4
        },
        "txtCategoria":{
            required: true
        },
        "txtImagen":{
            required:true
        },
        "txtEmail": {
            required: true,
            minlength: 8,
            email: true
        },
        "txtPassword":{
            required: true,
            minlength: 4
        },
        "txtNombre":{
            required: true,
            minlength: 4,
            maxlength: 15
        },
        "txtApellido":{
            required: true,
            minlength: 4,
            maxlength: 15
        },
        "txtEdad":{
            required: true,
            number: true,
            min:18,
            max:99
        },
        "txtRepetirPassword":{
            required: true,
            equalTo: '#id_txtPassword'
        }
    },
    messages :{
        "txtTitulo":{
            required: '---------------------Ingrese un Titulo para la publicacion!!',
            minlength: '---------------Debe tener un minimo de 4 caracteres!!',
            maxlength : '------------------Debe tener un largo maximo de 15 caracteres!!'
        },
        "txtEtiquetas":{
            required: '----------------Ingrese como minimo una etiqueta (#...)!!',
            minlength: '----------------Debe tener un minimo de 4 caracteres!!'
        },
        "txtCategoria":{
            required: '------------------Seleccione categoria!!'
        },
        "txtImagen":{
            required: '--------------Seleccione imagen!!'
        },
        "txtEmail":{
            required: '---------------Ingrese email!!',
            minlength: '--------------------El email debe tener un minimo de 8 caracteres',
            email: '---------------El formato de email es : ejemplo@gmail.com'
        },
        "txtPassword":{
            required: "------------------Ingrese su contraseña!",
            minlength: "-------------------Minimo 4 caracteres"
        },
        "txtNombre":{
            required: '---------------Ingrese su nombre!!',
            minlength: '----------------Debe tener un minimo de 4 caracteres!!',
            maxlength : '------------------Debe tener un largo maximo de 15 caracteres!!'
        },
        "txtApellido":{
            required: '---------------Ingrese su apellido!!',
            minlength: '----------------Debe tener un minimo de 4 caracteres!!',
            maxlength : '------------------Debe tener un largo maximo de 15 caracteres!!'
        },
        "txtEdad":{
            required: '---------------------Ingrese su edad!!',
            number: '-----------------------Solo se aceptan numeros!',
            min: '------------------------Edad minima 18 años',
            max: '------------------------Edad maxima 99 años'
        },
        "txtRepetirPassword":{
            required: '------------------Repita contraseña',
            equalTo: '-------------------Las contraseñas deben ser iguales!!'
        }
    }   
});


(function confirmation() {
    if(confirm("Realmente desea eliminar?"))
    {
        return true;
    }
    return false;
});