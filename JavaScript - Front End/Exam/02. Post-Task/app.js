window.addEventListener("load", solve);

function solve() {

    const taskTitleInput = document.getElementById('task-title');
    const categoryInput = document.getElementById('task-category');
    const contentInput = document.getElementById('task-content');
    const publishBtn = document.getElementById('publish-btn');

    const reviewList = document.getElementById('review-list');
    const publishedList = document.getElementById('published-list');
  
    publishBtn.addEventListener('click', publish);

    function publish(event) {
        event.preventDefault();

        let title = taskTitleInput.value;
        let category = categoryInput.value;
        let content = contentInput.value;

        if (
            title === "" ||
            category === "" ||
            content === ""
        ) {
        return;
        }

        let li = createElement('li', reviewList, null, ['rpost']);
        let article = createElement('article', li);
        let heading4 = createElement('h4', article, title);
        let p1 = createElement('p', article, `Category: ${category}`);
        let p2 = createElement('p', article, `Content: ${content}`);

        let editBtn = createElement('button', li, 'Edit', ['action-btn', 'edit']);
        let postBtn = createElement('button', li, 'Post', ['action-btn', 'post']);

        editBtn.addEventListener('click', editStory);
        postBtn.addEventListener('click', postStory);
        
        clearAllInputs();
        // publishBtn.setAttribute('disabled', true);

        function editStory(){
            taskTitleInput.value = title;
            categoryInput.value = category;
            contentInput.value = content;
            li.remove();
        }

        function postStory(){
            li.removeChild(editBtn);
            li.removeChild(postBtn);
            publishedList.appendChild(li);
        }
    }

    function clearAllInputs() {
        taskTitleInput.value = "";
        categoryInput.value = "";
        contentInput.value = "";
    }

    function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
      const htmlElement = document.createElement(type);
    
      if (content && useInnerHtml) {
        htmlElement.innerHTML = content;
      } else {
        if (content && type !== 'input') {
          htmlElement.textContent = content;
        }
    
        if (content && type === 'input') {
          htmlElement.value = content;
        }
      }
    
      if (classes && classes.length > 0) {
        htmlElement.classList.add(...classes);
      }
    
      if (id) {
        htmlElement.id = id;
      }
    
      // { src: 'link', href: 'http' }
      if (attributes) {
        for (const key in attributes) {
          htmlElement.setAttribute(key, attributes[key])
        }
      }
    
      if (parentNode) {
        parentNode.appendChild(htmlElement);
      }
    
      return htmlElement;
    }
}