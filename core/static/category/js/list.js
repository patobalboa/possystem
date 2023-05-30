$(function() {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata',
            },
            dataSrc: ""
        },
        // {
        //     "id": 2,
        //     "nombre_categoria": "Bebidas",
        //     "descripcion": "Bebidas",
        //     "estado": true
        // }
        columns: [
            {"data": "nombre_categoria"},
            {"data": "descripcion"},
            {"data": "estado"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return data;
                }
            },
        ],
        initComplete: function(settings, json) {
                
            }
    });
});