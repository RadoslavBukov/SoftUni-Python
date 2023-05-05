function attachEvents() {

    const BASE_URL = "http://localhost:3030/jsonstore/tasks/";
    const loadBoardBtn = document.getElementById('load-board-btn');
    const titleInput = document.getElementById('title');
    const descriptioninput = document.getElementById('description');
    const addTaskBtn = document.getElementById('create-task-btn');

    const articleToDoSection = document.querySelector('#todo-section > ul');
    const articleInProgressSection = document.querySelector('#in-progress-section > ul');
    const articleCodeReviewSection = document.querySelector('#code-review-section > ul');
    const articleDoneSection = document.querySelector('#done-section > ul');

    loadBoardBtn.addEventListener('click', loadBoardHandler);
    addTaskBtn.addEventListener('click', addTaskHandler);

    let allTasks = [];
    let taskToMove = {};
    let newStatus = "";

    function loadBoardHandler(event){
        if (event) {
            event.preventDefault();
        }

        articleToDoSection.innerHTML = '';
        articleInProgressSection.innerHTML = '';
        articleCodeReviewSection.innerHTML = '';
        articleDoneSection.innerHTML = '';

        fetch(BASE_URL)
            .then((res) => res.json())
            .then((allTasksRes) => {
                const tasks = Object.values(allTasksRes)
                allTasks = tasks;
                for (const {title, description, status, _id} of tasks) {
                    const li_task = document.createElement('li');
                    li_task.classList.add("task");
                    li_task.id = _id;
                    const heading3 = document.createElement('h3');
                    heading3.textContent = title;
                    const p = document.createElement('p');
                    p.textContent = description;
                    const button = document.createElement('button');
                    li_task.appendChild(heading3);
                    li_task.appendChild(p);
                    li_task.appendChild(button);

                    if (status === "ToDo") {
                        articleToDoSection.appendChild(li_task);
                        button.textContent = 'Move to In Progress';
                        button.addEventListener('click', moveTaskNextCategory);
                    }
                    else if (status === "In Progress") {
                        articleInProgressSection.appendChild(li_task);
                        button.textContent = 'Move to Code Review';
                        button.addEventListener('click', moveTaskNextCategory);
                    }
                    else if (status === "Code Review") {
                        articleCodeReviewSection.appendChild(li_task);
                        button.textContent = 'Move to Done';
                        button.addEventListener('click', moveTaskNextCategory);
                    }
                    else if (status === "Done") {
                        articleDoneSection.appendChild(li_task);
                        button.textContent = 'Close'
                        button.addEventListener('click', closeTaskHandler);
                    }
                }
            })
    }

    function addTaskHandler(event) {
        event.preventDefault();

        const title = titleInput.value;
        const description = descriptioninput.value;
        const status = "ToDo";

        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({title, description, status})
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

    function moveTaskNextCategory(event){
        event.preventDefault();

        const id = this.parentNode.id;
        taskToMove = allTasks.find((p) => p._id === id);
        currentTaskStatus = taskToMove.status;
        console.log(currentTaskStatus);
        if (currentTaskStatus === "ToDo") {
           newStatus = "In Progress";
        }
        else if (currentTaskStatus === "In Progress") {
            newStatus = "Code Review";
        }
        else if (currentTaskStatus === "Code Review") {
            newStatus = "Done";
        }
        
        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({status: newStatus})
          }
      
        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => {
                loadBoardHandler();
            })
            .catch((err) => {
              console.error(err);
            })


    }

    function closeTaskHandler(event){
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
        descriptioninput.value = '';
    }
}
attachEvents();