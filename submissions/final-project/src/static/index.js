const updateBtns = document.querySelectorAll(".update-btn");
const deleteBtns = document.querySelectorAll(".delete-btn");
const updatePassBtn = document.getElementById("updatePassBtn");

const updateWebsite = document.getElementById("updateWebsite");
const updateEmail = document.getElementById("updateEmail");
const updatePassword = document.getElementById("updatePassword");
let id;

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", (event) => {
        const parentNode = event.target.parentNode.parentNode;
        id = parentNode.dataset.id;
        updateWebsite.value = parentNode.querySelector('span:nth-child(2)').textContent;
        updateEmail.value = parentNode.querySelector('span:nth-child(4)').textContent;
        updatePassword.value = parentNode.dataset.password;
    });

    deleteBtns[i].addEventListener("click", (event) => {
        id = event.target.parentNode.parentNode.dataset.id;
        fetch(`delete/${id}`, {
            method: "DELETE"
        }).then(data => data.json()).then(_ => window.location.href = "/")
    })
}

updatePassBtn.addEventListener("click", () => {
    fetch(`update/${id}`, {
        body: JSON.stringify({website: updateWebsite.value, email: updateEmail.value, password: updatePassword.value}),
        headers: {
            "Content-Type": "application/json"
        },
        method: "PATCH"
    }).then(data => data.json()).then(_ => window.location.href = "/")
}); 