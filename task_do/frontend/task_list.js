document.addEventListener('DOMContentLoaded', function () {
    const domain = 'http://127.0.0.1:8000/';
    const userList = document.getElementById('user-list');
    const userLoader = new XMLHttpRequest();
    let nameInput = document.querySelector('#name');
    let userUpdater = new XMLHttpRequest();
    let userDeleter = new XMLHttpRequest();

    userLoader.addEventListener('readystatechange', () => {
        if (userLoader.readyState == 4) {
            if (userLoader.status == 200) {
                let data = JSON.parse(userLoader.responseText);
                let s = '<ul>';
                for (let i = 0; i < data.length; i++) {
                    let user = data[i];
                    s += `<li>${user.name} <a href="${domain}api/users/${user.id}/" class="detail">Вывести</a> <a href="${domain}api/users/${user.id}/" class="delete">Удалить</a></li>`;
                }
                s += '</ul>';
                userList.innerHTML = s;

                let links = userList.querySelectorAll('ul li a.detail');
                links.forEach(link => {
                    link.addEventListener('click', userLoad);
                });

                links = userList.querySelectorAll('ul li a.delete');
                links.forEach(link => {
                    link.addEventListener('click', userDelete);
                });
            } else {
                console.log(userLoader.status, userLoader.statusText);
            }
        }
    });

    userUpdater.addEventListener('readystatechange', () => {
        if (userUpdater.readyState == 4) {
            if (userUpdater.status == 200 || userUpdater.status == 201) {
                listLoad();
                nameInput.value = '';
            } else {
                console.log(userUpdater.status, userUpdater.statusText);
            }
        }
    });

    document.getElementById('user_form').addEventListener('submit', evt => {
        evt.preventDefault();
        let url = 'api/users/';
        let method = 'POST';
        let data = JSON.stringify({ name: nameInput.value });
        userUpdater.open(method, domain + url, true);
        userUpdater.setRequestHeader('Content-Type', 'application/json');
        userUpdater.send(data);
    });

    userDeleter.addEventListener('readystatechange', () => {
        if (userDeleter.readyState == 4) {
            if (userDeleter.status == 204) {
                listLoad();
            } else {
                console.log(userDeleter.status, userDeleter.statusText);
            }
        }
    });

    function listLoad() {
        userLoader.open('GET', domain + 'api/users/', true);
        userLoader.send();
    }

    function userLoad(evt) {
        evt.preventDefault();
        userLoader.open('GET', evt.target.href, true);
        userLoader.send();
    }

    function userDelete(evt) {
        evt.preventDefault();
        userDeleter.open('DELETE', evt.target.href, true);
        userDeleter.send();
    }

    listLoad();
});

