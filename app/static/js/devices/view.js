var $view = (function(){
    var refreshSoftwareBtn = $('#refreshSoftwareBtn');
    var testBtn = $('#testBtn');

    function debugUserID(){
        console.log("$user_id is: " + $user_id);
    }

    function changeControl(e){
        var check = e.attr('disabled');

        if (check) {
            e.attr('disabled', false);
        }
        e.attr('disabled', true);
    }

    function netmikoGetSoftware(){
        $.ajax({
            method: "PATCH",
            dataType: "json",
            url: 'http://localhost:5000/api/devices/' + $device_id + '/show_version',
            success: function(data, textStatus, jqXHR)
            {
                console.log(data, textStatus);
                $('#dd_hostname').html('<p id="dd_hostname"><strong>Hostname: </strong>' + data["hostname"] +'</p>');
                $('#dd_hardware').html('<p id="dd_hardware"><strong>Hardware: </strong>' + data["hardware"] + '</p>');
                $('#dd_version').html('<p id="dd_version"><strong>Version: </strong>' + data["version"] + '</p>');
                $('#dd_uptime').html('<p id="dd_uptime"><strong>Uptime: </strong>' + data["uptime"] + '</p>');
                $('#dd_runningimage').html('<p id="dd_runningimage"><strong>Image: </strong>' + data["running_image"] + '</p>');
                $('#dd_serial').html('<p id="serial"><strong>Serial: </strong>' + data["serial"] + '</p>');
                changeControl(refreshSoftwareBtn);
                refreshSoftwareBtn.html('Refresh');
            },
            error: function(jqXHR, textStatus, errorThrown)
            {
                console.log(errorThrown);
                changeControl(refreshSoftwareBtn);
                refreshSoftwareBtn.html('Refresh');
            }
        });
    }

    refreshSoftwareBtn.on('click', function(e){
        e.preventDefault();
        changeControl(refreshSoftwareBtn);
        refreshSoftwareBtn.html('<i class="fa fa-spinner fa-spin"></i> SSH...');
        netmikoGetSoftware();
    });
    
    testBtn.on('click', function (e) {
        e.preventDefault();
        changeControl(testBtn);
        debugUserID();
    });
})();