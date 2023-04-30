function addItem() {
    const ulContainer = document.getElementById('items');
    const input = document.getElementById('newItemText');
    const newLi = document.createElement('li');
    const deleteLink = document.createElement('a');
    deleteLink.textContent = '[Delete]';
    deleteLink.setAttribute('href','#');
    // or
    // deleteLink.href('#');
    newLi.textContent = input.value;
    ulContainer.appendChild(newLi);
    newLi.appendChild(deleteLink);
    input.value = '';

    deleteLink.addEventListener('click', clickDelete);

    function clickDelete(e) {
        const anchor = e.currentTarget;
        anchor.parentElement.remove();
    }
}   