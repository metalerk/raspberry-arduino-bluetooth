function on() {
  console.log('on');

  $.ajax({
    url: "http://localhost:8000/",
    type: "post", // or "get"
    // data: '{"action":"on"}',
    data: JSON.stringify({
      "command": "on",
      "mac": "00:21:13:01:FA:CA",
    }),
    success: function(data) {
      alert(data.result);
    }});
}

function off() {
  console.log('off');

  $.ajax({
    url: "http://localhost:8000/",
    type: "post", // or "get"
    // data: '{"action":"on"}',
    data: JSON.stringify({
      "command": "off",
      "mac": "00:21:13:01:FA:CA",
    }),
    success: function(data) {
      alert(data.result);
    }});
}

function onChangeMAC(e) {
  console.log(e);
}
