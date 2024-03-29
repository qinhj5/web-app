window.onload = function () {
    google.accounts.id.initialize({
        client_id: "356901971367-h22g9eks5kr5lh09hdulnk5cdse410vl.apps.googleusercontent.com",
        callback: onLoginCallback
    });

    var credential = localStorage.getItem("credential");
    if (credential === null) {
        displayLogin();
    } else {
        var user_id = localStorage.getItem("user_id");
        var name = localStorage.getItem("name");
        var email = localStorage.getItem("email");
        fetch("/status", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + credential
            },
            body: JSON.stringify(
                {
                    user_id: user_id,
                    name: name,
                    email: email,
                    credential: credential
                }
            )
        })
            .then(response => response.json())
            .then(data => {
                const is_valid = data.is_valid;
                if (is_valid === true) {
                    displayLogout();
                } else {
                    displayLogin();
                }
            })
            .catch(error => console.error(error));
    }
};

function showUsers() {
    fetch('/users')
        .then(response => response.json())
        .then(data => {
            const table_body = document.getElementById("table_body");
            table_body.innerHTML = "";
            data.forEach(member => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${member.name}</td>
                    <td>${member.email}</td>
                `;
                table_body.appendChild(row);
            });
        })
        .catch(error => console.error(error));
}

function displayLogin() {
    document.getElementById("render_button").style.display = "block";
    document.getElementById("logout_button").style.display = "none";
    document.getElementById("user_name").textContent = "";

    document.cookie = "";
    var render_button = document.getElementById("render_button");
    google.accounts.id.renderButton(render_button, {width: 180});

    showUsers();
};

function displayLogout() {
    document.getElementById("render_button").style.display = "none";
    document.getElementById("logout_button").style.display = "block";
    document.getElementById("user_name").textContent = localStorage.getItem("name");

    showUsers();
};

function onClickLogout() {
    var user_id = localStorage.getItem("user_id");
    google.accounts.id.revoke(user_id, done => {
        console.log(done.error);
    });

    localStorage.removeItem("user_id");
    localStorage.removeItem("name");
    localStorage.removeItem("email");
    localStorage.removeItem("credential");

    displayLogin();
};

function onLoginCallback(response) {
    var credential = response.credential,
        sub_credential = credential.split(".")[1].replace(/-/g, "+").replace(/_/g, "/"),
        profile = JSON.parse(decodeURIComponent(escape(window.atob(sub_credential))));

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + credential
        },
        body: JSON.stringify(
            {
                user_id: profile.sub,
                name: profile.name,
                email: profile.email,
                credential: credential
            }
        )
    })
        .then(response => response.json())
        .then(data => {
            const is_login = data.is_login;
            if (is_login === true) {
                localStorage.setItem("user_id", profile.sub);
                localStorage.setItem("name", profile.name);
                localStorage.setItem("email", profile.email);
                localStorage.setItem("credential", credential);
                displayLogout();
            } else {
                displayLogin();
            }
        })
        .catch(error => console.error(error));
};
