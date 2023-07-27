// var baseHost = "http://192.168.0.196:8000"
var baseHost = "http://127.0.0.1:8000"

function _axios(method, url, data=null) {
    return axios({
        method: method,
        url: baseHost + url,
        data: data
    }).then((res) => {
        return res;
    })
}

function _xhr(method, url, data=null) {
    var xhr = new XMLHttpRequest();
    var adjUrl = baseHost + url;
    xhr.open(method, adjUrl, false);
    if (data !== null) {
        xhr.send(JSON.stringify(data));
    } else {
        xhr.send();
    }
    return xhr;
}