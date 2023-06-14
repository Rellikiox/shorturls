
async function shortenUrl() {
    var inputField = document.getElementById('url');
    var url = inputField.value;
    if (!url) {
        console.log('No URL provided');
        return;
    }

    try {
        const response = await fetch('http://local.api/api/v1/shorten-url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'url': url })
        });

        const result = await response.json();
        if (response.ok) {
            addShortUrlToDom(result.url, result.short_url);
        } else {
            console.error(result);
        }

    } catch (error) {
        console.error('Error: ', error);
    }
}

function addShortUrlToDom(url, short_url) {
    var listElement = document.getElementById('generated-links');
    var newEntry = `<li>${url} -> <a href="${short_url}" target="_blank">${short_url}</a></li>`;
    listElement.innerHTML += newEntry;
}