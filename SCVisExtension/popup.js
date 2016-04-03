/**
 * Created by Johnny on 4/2/16.
 */
document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('checkPage');
    checkPageButton.addEventListener('click', function() {

        chrome.tabs.getSelected(null, function(tab) {
            d = document;

            var f = d.createElement('form');
            f.action = 'http://www.bing.com/';
            f.method = 'post';
            var i = d.createElement('input');
            i.type = 'hidden';
            i.name = 'url';
            i.value = tab.url;
            f.appendChild(i);
            d.body.appendChild(f);
            f.submit();
        });
        document.tabs.query({active: true, currentWindow: true}, function(tabs) {
            document.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
                console.log(response.farewell);
            });
        });
    }, false);

}, false);
