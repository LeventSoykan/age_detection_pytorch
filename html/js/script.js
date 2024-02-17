const dropArea = document.getElementById('drop-area');
const fileSelector = document.getElementById('select-file');
const resultArea = document.getElementById('result-area');
let req_id = 0;

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop', 'submit'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when a file is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

// Remove highlight when a file is dragged out of the drop area
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

dropArea.addEventListener('click', handleClick, false)

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function handleClick(e) {
    fileSelector.click()
}

fileSelector.addEventListener('change', async function(e) {
    if (e.target.files[0]) {
        await sendToAD(e.target.files);
        fileSelector.value = null;
        console.log('Files received');
    }
})

function highlight() {
    dropArea.classList.add('highlight');
}



function unhighlight() {
    dropArea.classList.remove('highlight');
}

async function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;

    await sendToAD(files);
    fileSelector.value = null
    console.log('Files received');
}

async function sendToAD(files) {
    if (files.length > 0) {
        const formData = new FormData();
        for (const file of files) {
            formData.append('files', file);
        }

        try {
            const response = await fetch('http://localhost:8000/api/age', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                for (const [key, value] of Object.entries(data.result)) {
                    const h3 = document.createElement('h3');
                    h3.innerHTML = `${key}: ${value}`
                    resultArea.appendChild(h3);
                }
            })
        } catch (error) {
            console.error('Error:', error);
        }
	// window.location = 'request.html';

    }
}


