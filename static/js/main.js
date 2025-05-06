<!-- 🖼️ JavaScript: Live preview of the uploaded image -->
<script>
    function displayFileNameAndPreview(input) {
        const file = input.files[0];  // Get the selected file
        const fileName = document.getElementById('file-name');  // Reference to file name display
        const preview = document.getElementById('preview-image');  // Reference to preview image element

        if (file) {
            fileName.textContent = file.name;  // Show selected file name

            // Read and show image preview
            const reader = new FileReader();
            reader.onload = function (e) {
                preview.src = e.target.result;
                preview.style.display = "block";
            };
            reader.readAsDataURL(file);  // Convert file to base64 string
        } else {
            fileName.textContent = "No file chosen";
            preview.style.display = "none";
        }
    }
</script>

<!-- 👁️ JavaScript: Show/hide disease "See More" sections -->
<script>
    function toggleDetails(id, el) {
        const section = document.getElementById(id);  // Get the section by ID
        if (section.style.display === "none") {
            section.style.display = "block";
            el.textContent = "See Less";  // Update link text
        } else {
            section.style.display = "none";
            el.textContent = "See More";
        }
    }
</script>