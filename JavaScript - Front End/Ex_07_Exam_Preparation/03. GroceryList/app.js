function attachEvents() {

    const BASE_URL = "http://localhost:3030/jsonstore/grocery/";
    const productInput = document.getElementById('product');
    const countInput = document.getElementById('count');
    const priceInput = document.getElementById('price');
    const addBtn = document.getElementById('add-product');
    const updateBtn = document.getElementById('update-product');
    const loadAllBtn = document.getElementById('load-product');

    const tableBody = document.getElementById('tbody');

    loadAllBtn.addEventListener('click', loadAllProductsHandler);
    addBtn.addEventListener('click', addProductHandler);
    updateBtn.addEventListener('click', updateProductHandler);

    let productToEditId = '';

    function loadAllProductsHandler(event) {
        if (event) {
            event.preventDefault();
          }

        tableBody.innerHTML = '';
        
        fetch(BASE_URL)
            .then((res) => res.json())
            .then((allProductsRes) => {
                const products = Object.values(allProductsRes)
                for (const {product, count, price, _id} of products) {
                    const tableRow = createElement('tr', tableBody);
                    tableRow.id = _id;
                    const tableCellName = createElement('td', tableRow, product, ["name"]);
                    const tableCellCount = createElement('td', tableRow, count, ["count-product"]);
                    const tableCellPrice = createElement('td', tableRow, price, ["product-price"]);
                    const tableCellAction = createElement('td', tableRow, null, ["btn"]);
                    const updateTableBtn = createElement('button', tableCellAction, ["Update"], ["update"]);
                    const deleteTableBtn = createElement('button', tableCellAction, ["Delete"], ["delete"]);                    
                
                    updateTableBtn.addEventListener('click', updateTableHandler);
                    deleteTableBtn.addEventListener('click', deleteTableRowHandler);
                }
            })
            .catch((err) => {
                console.error(err);
            })
        
    }

    function updateTableHandler(event){
        event.preventDefault();
        const id = this.parentNode.parentNode.id;

        fetch(`${BASE_URL}${id}`)
            .then((res) => res.json())
            .then((allProductsRes) => {
                const {product, count, price, _id} = allProductsRes;
                productToEditId = allProductsRes._id;
                productInput.value = product;
                countInput.value = count;
                priceInput.value = price;

                addBtn.setAttribute('disabled',true);
                updateBtn.removeAttribute('disabled');

            })
            .catch((err) => {
                console.error(err)
            })
    }

    function deleteTableRowHandler(event){
        event.preventDefault();
        
        const id = this.parentNode.parentNode.id;
        const httpHeaders = {
            method: "DELETE",
        }

        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadAllProductsHandler())
            .catch((err) => {
                console.error(err)
            })
    }

    function addProductHandler(event) {
        event.preventDefault();

        const product = productInput.value;
        const count = countInput.value;
        const price = priceInput.value;
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({product, count, price})
        }
        fetch(BASE_URL, httpHeaders)
            .then(() => {
                loadAllProductsHandler();
                clearInputFields();
            })
            .catch((err) => {
                console.error(err)
            })
    }

    function updateProductHandler(event){
        event.preventDefault();

        const product = productInput;
        const count = countInput;
        const price = priceInput;        

        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({
                product: product.value,
                count: count.value,
                price: price.value,
            })
        }

        fetch(`${BASE_URL}${productToEditId}`, httpHeaders)
            .then(() => {
                loadAllProductsHandler();
                updateBtn.setAttribute('disabled',true);
                addBtn.removeAttribute('disabled');
                clearInputFields();
            })
            .catch((err) => {
                console.error(err)
            })
    }


    function clearInputFields() {
        productInput.value = '';
        countInput.value = '';
        priceInput.value = '';
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
  
  attachEvents();