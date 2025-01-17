document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector("body"),
        sidebar = document.querySelector(".sidebar"),
        toggle = document.querySelector(".toggle"),
        modeSwitch = document.querySelector(".toggle-switch"),
        modeText = document.querySelector(".mode-text"),
        dropdownBtn = document.querySelector(".dropdown-btn .dropdown-toggle"),
        dropdownContainer = document.querySelector(".dropdown-container");

    // Check if elements exist to prevent errors
    if (toggle && sidebar) {
        // Sidebar toggle functionality
        toggle.addEventListener("click", () => {
            sidebar.classList.toggle("close");
        });
    }

    if (modeSwitch && body && modeText) {
        // Mode switch functionality
        modeSwitch.addEventListener("click", () => {
            body.classList.toggle("dark");

            // Update mode text
            if (body.classList.contains("dark")) {
                modeText.innerText = "Light Mode";
            } else {
                modeText.innerText = "Dark Mode";
            }
        });
    }

    if (dropdownBtn && dropdownContainer) {
        // Dropdown toggle functionality
        dropdownBtn.addEventListener("click", (e) => {
            e.preventDefault(); // Prevent default action
            dropdownContainer.classList.toggle("show");
        });
    }
});


