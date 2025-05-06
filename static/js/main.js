// 📦 Handles the "See More" and "See Less" toggle behavior
function toggleDetails(id, el) {
    const section = document.getElementById(id);
    if (section.style.display === "none") {
        section.style.display = "block";
        el.textContent = "See Less";
    } else {
        section.style.display = "none";
        el.textContent = "See More";
    }
}

// 📤 Shows selected filename and image preview
function displayFileNameAndPreview(input) {
    const file = input.files[0];
    const fileName = document.getElementById('file-name');
    const preview = document.getElementById('preview-image');

    if (file) {
        fileName.textContent = file.name;

        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = "block";
        };
        reader.readAsDataURL(file);
    } else {
        fileName.textContent = "No file chosen";
        preview.style.display = "none";
    }
}
