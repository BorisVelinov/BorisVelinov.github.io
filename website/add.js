// Когато потребителят натисне бутона "Регистрирай се", изпълнете следния код.
function register() {
    // Изтеглете данните от формата.
    const username = document.querySelector("input[name=username]").value;
    const password = document.querySelector("input[name=password]").value;
    const email = document.querySelector("input[name=email]").value;

    // Използвайте JavaScript, за да изпратите данните към Python кода.
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/register", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({
        username,
        password,
        email,
    }));

    // Ако заявката е успешна, обновете страницата.
    if (xhr.status === 200) {
        window.location.href = "/";
    }
}

// Добавете събитие за кликване към бутона "Регистрирай се".
document.querySelector("input[type=submit]").addEventListener("click", register);
