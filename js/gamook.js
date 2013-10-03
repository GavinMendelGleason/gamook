/* 
Author: Gavin Mendel-Gleason
Copyright: Peer Production License (see http://p2pfoundation.net/Peer_Production_License)

Gamook auxiliary and library functions.
*/

function handlers(id){
    return $._data($(id).get(0), "events");
}

function showError(s){ 
    $('#status').html('<div style="color:red;">'+ s +'</div>');
}

function showStatus(s){
    $('#status').html('<div style="bgcolor:green;">' + s + '</div>');
}

function ajaxError(x,e){
    showError('Error '+x.status+' '+x.responseText);
}

