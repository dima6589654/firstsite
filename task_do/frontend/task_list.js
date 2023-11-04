const domain = 'http://127.0.0.1:8000/';

const username = 'admin';
const password = 'qwe123';
const credentials = window.btoa(username + ':' + password);

const userForm = document.getElementById('user_form');

async function loadUserList() {
    try {
        const response = await fetch(domain + 'api/users/', {
            method: 'GET',
            headers: {
                'Authorization': 'Basic ' + credentials,
            },
        });

        if (response.status === 200) {
            const data = await response.json();
            const userListUl = document.getElementById('user-list-ul');
            userListUl.innerHTML = '';

            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = user.username;
                userListUl.appendChild(li);
            });
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
}

userForm.addEventListener('submit', async (evt) => {
    evt.preventDefault();

    const username = document.getElementById('username').value;
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const email = document.getElementById('email').value;
    const password1 = document.getElementById('password_1').value;
    const password2 = document.getElementById('password_2').value;
    const isActive = document.getElementById('is_active').checked;
    const isStaff = document.getElementById('is_staff').checked;
    const isSuperuser = document.getElementById('is_superuser').checked;
    const bio = document.getElementById('bio').value;
    const profilePicture = document.getElementById('profile_picture').files[0];
    const groups = document.getElementById('groups').value; // Получаем выбранную группу

    if (password1 !== password2) {
        console.error('Пароли не совпадают.');
        return;
    }

    const formData = new FormData();
    formData.append('username', username);
    formData.append('first_name', firstName);
    formData.append('last_name', lastName);
    formData.append('email', email);
    formData.append('password_1', password1);
    formData.append('password_2', password2);
    formData.append('is_active', isActive);
    formData.append('is_staff', isStaff);
    formData.append('is_superuser', isSuperuser);
    formData.append('bio', bio);
    formData.append('groups', groups); // Добавляем выбранную группу
    if (profilePicture) {
        formData.append('profile_picture', profilePicture);
    }

    try {
        const response = await fetch(domain + 'api/users/', {
            method: 'POST',
            body: formData,
            headers: {
                'Authorization': 'Basic ' + credentials,
            },
        });

        if (response.status === 201) {
            await loadUserList();
            userForm.reset();
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
});

loadUserList();

