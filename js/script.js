const videoContainer = document.getElementById('videoContainer');

function createElements(data) {
  const dataArray = Object.values(data);

  dataArray.forEach(item => {
    if (item.iFrameURL !== '' && item.iFrameURL !== NaN) {
      const card = document.createElement('div');
      card.className = 'card border-dark mb-3';
      card.style.width = '22rem';
      const iframe = document.createElement('iframe');
      iframe.src = item.iFrameURL;
      iframe.className = 'card-img-top';
      iframe.width = 560;
      iframe.height = 300;
      iframe.frameBorder = 0;
      iframe.scrolling = 'yes';
      iframe.allowFullscreen = true;
      card.appendChild(iframe);
      if (item.name !== '' && item.name !== NaN) {
        const cardBody = document.createElement('div');
        cardBody.className = 'card-body';
        const text = document.createElement('p');
        text.className = 'card-text';
        text.textContent = item.name;
        cardBody.appendChild(text);
        card.appendChild(cardBody);
      }
      videoContainer.appendChild(card);
    }
  });
}

fetch('./data/data.json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    createElements(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
