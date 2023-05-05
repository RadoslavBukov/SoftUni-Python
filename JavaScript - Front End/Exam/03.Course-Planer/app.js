function attachCourses() {

    const BASE_URL = "http://localhost:3030/jsonstore/tasks/";
    const loadCoursesBtn = document.getElementById('load-course');
    const titleInput = document.getElementById('course-name');
    const typeInput = document.getElementById('course-type');
    const descriptionInput = document.getElementById('description');
    const teacherNameInput = document.getElementById('teacher-name');

    const addCourseBtn = document.getElementById('add-course');
    const editCourseMainBtn = document.getElementById('edit-course');

    const coursesSection = document.getElementById('list');

    loadCoursesBtn.addEventListener('click', loadBoardHandler);
    addCourseBtn.addEventListener('click', addCourseHandler);
    editCourseMainBtn.addEventListener('click', editCourseMainHandler);

    let allCourses = [];
    let courseToEdit = {};

    function loadBoardHandler(event){
        if (event) {
            event.preventDefault();
        }

        coursesSection.innerHTML = '';

        fetch(BASE_URL)
            .then((res) => res.json())
            .then((allCoursesRes) => {
                const courses = Object.values(allCoursesRes)
                allCourses = courses;
                for (const {title, type, description, teacher, _id} of courses) {
                    const div_courses = document.createElement('div');
                    div_courses.classList.add("container");
                    div_courses.id = _id;

                    const h2Title = document.createElement('h2');
                    h2Title.textContent = title;

                    const h3Teacher = document.createElement('h3');
                    h3Teacher.textContent = teacher;
                    const h3Type = document.createElement('h3');
                    h3Type.textContent = type;

                    const h4Description = document.createElement('h4');
                    h4Description.textContent = description;

                    const editBtn = document.createElement('button');
                    editBtn.textContent = 'Edit Course';
                    editBtn.classList.add("edit-btn");
                    editBtn.addEventListener('click', editCourseHandler);

                    const finishBtn = document.createElement('button');
                    finishBtn.textContent = 'Finish Course';
                    finishBtn.classList.add("finish-btn");
                    finishBtn.addEventListener('click', finishCourseHandler);

                    div_courses.appendChild(h2Title);
                    div_courses.appendChild(h3Teacher);
                    div_courses.appendChild(h3Type);
                    div_courses.appendChild(h4Description);
                    div_courses.appendChild(editBtn);
                    div_courses.appendChild(finishBtn);
                    coursesSection.appendChild(div_courses);
                }
            })
    }

    function addCourseHandler(event) {
        event.preventDefault();

        const title = titleInput.value;
        const type = typeInput.value;
        const description = descriptionInput.value;
        const teacher = teacherNameInput.value;

        if (type === "Long" || type === "Medium" || type === "Short"){
            const httpHeaders = {
                method: 'POST',
                body: JSON.stringify({title, type, description, teacher})
            }

            fetch(BASE_URL, httpHeaders)
                .then(() => {
                    loadBoardHandler();
                    clearInputFields();
                })
                .catch((err) => {
                    console.error(err)
                })
        }
    }

    function editCourseMainHandler(event) {
        event.preventDefault();

        const id = courseToEdit._id;
        console.log(id);
        const title = titleInput.value;
        const type = typeInput.value;
        const description = descriptionInput.value;
        const teacher = teacherNameInput.value;

        const httpHeaders = {
            method: 'PUT',
            body: JSON.stringify({title, type, description, teacher, _id: id})
        }
      
        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => {
                loadBoardHandler();
                editCourseMainBtn.setAttribute('disabled',true);
                addCourseBtn.removeAttribute('disabled');
                clearInputFields();
            })
            .catch((err) => {
              console.error(err);
            })
    }

    function editCourseHandler(event){
        event.preventDefault();

        const id = this.parentNode.id;
        courseToEdit = allCourses.find((p) => p._id === id);
        titleInput.value = courseToEdit.title;
        typeInput.value = courseToEdit.type;
        descriptionInput.value = courseToEdit.description;
        teacherNameInput.value = courseToEdit.teacher;

        let courseToHide = document.getElementById(id);
        courseToHide.setAttribute("hidden", true);

        addCourseBtn.setAttribute('disabled',true);
        editCourseMainBtn.removeAttribute('disabled');
    }

    function finishCourseHandler(event){
        event.preventDefault();

        const id = this.parentNode.id;
        const httpHeaders = {
            method: "DELETE",
        }
        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadBoardHandler())
            .catch((err) => {
                console.error(err)
            })
    }

    function clearInputFields() {
        titleInput.value = '';
        typeInput.value = '';
        descriptionInput.value = '';
        teacherNameInput.value = '';
    }
}

attachCourses();