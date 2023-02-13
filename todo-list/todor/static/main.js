// console.log("Editar todo")
const edit = document.querySelector(".edit");
const srcValue = imageElement.getAttribute("src");
console.log(elements)
document.querySelector('#d1').addEventListener('click', function () {
    let id = this.getAttribute('data-id');

    console.log(id)

    fetch("/todo/get_todo/" + id)
        .then(response => response.json())
        .then(todo => {
            document.querySelector('#title').value = todo.title;
            document.querySelector('#desc').value = todo.desc;
            //document.querySelector('#state').value = todo.state;
        });
});