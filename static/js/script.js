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

(function confirmation() {
    if(confirm("Realmente desea eliminar?"))
    {
        return true;
    }
    return false;
});


function notificacionError(mensaje){
    Swal.fire({
        title:'Error!',
        text: mensaje,
        icon: 'error'
    })
}

function notificacionSuccess(mensaje){
    Swal.fire({
        title:'Felicitaciones!',
        text: mensaje,
        icon: 'success'
    })
}